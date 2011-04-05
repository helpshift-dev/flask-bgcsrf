#!/usr/bin/env python
# bgcsrf.py -- BG's own bad-ass CSRF Flask Extension
# Author: Baishampayan Ghose <b.ghose@qotd.co>
# Copyright (C), 2011 Qotd, Inc.
# License: MIT-X11

"""
flaskext.bgcsrf
---------------

BG's own CSRF middleware for Flask
This will probably protect your ass from CSRF attacks

Based on - http://sjl.bitbucket.org/flask-csrf/
"""

import uuid
import binascii
from flask import abort, request, session, g
from werkzeug.routing import NotFound


_exempt_views = []

def __get_header(header):
    """Get the requested header from the request object
    """
    return request.headers.get(header, None)


def __constant_time_compare(val1, val2):
    """
    Returns True if the two strings are equal, False otherwise.

    The time taken is independent of the number of characters that match.
    """
    if not (val1 and val2):
        return False
    if len(val1) != len(val2):
        return False
    result = 0
    for x, y in zip(val1, val2):
        result |= ord(x) ^ ord(y)
    return result == 0


def csrf_exempt(view):
    _exempt_views.append(view)
    return view


def csrf(app, on_csrf=None):
    @app.before_request
    def _csrf_check_exemptions():
        try:
            dest = app.view_functions.get(request.endpoint)
            g._csrf_exempt = dest in _exempt_views
        except NotFound:
            g._csrf_exempt = False
    
    @app.before_request
    def _csrf_protect():
        if not g._csrf_exempt:
            if request.method in ["POST", "PUT", "DELETE"]:
                csrf_token = session.get("_csrf_token")
                
                token = (request.form.get("_csrf_token") or \
                             __get_header("X-CSRF-TOKEN") or \
                             __get_header("X-XSRF-TOKEN"))
                
                if not csrf_token or not __constant_time_compare(csrf_token, token):
                    if on_csrf:
                        on_csrf(*app.match_request())
                    session.pop("_csrf_token", None) # need to delete the token
                    abort(400)
    
    def generate_csrf_token():
        if "_csrf_token" not in session:
            token = binascii.b2a_hex(uuid.uuid4().bytes)
            session["_csrf_token"] = str(token)
        return session["_csrf_token"]
    

    app.jinja_env.globals["csrf_token"] = generate_csrf_token

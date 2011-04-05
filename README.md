Flask BGCSRF
=============

Flask-BGCSRF (`flask-bgcsrf`) is a simple CSRF middleware that helps
you in preventing Cross Site Request Forgery (CSRF) attacks.

Usage
-----

You'll need to enable the middleware like this -

       from flaskext.bgcsrf import csrf
       csrf(app) # assuming app is your Flask app

Once that is done, you'll have to add the CSRF token in every form in
your app that makes a `POST`, `PUT` or `DELETE` request to the app.

     <input type="hidden" value="{{ csrf_token() }}">

If you want to disable CSRF protection in any specific view, you can
do so by using the `csrf_exempt` decorator on your view.

      from flaskext import csrf_exempt

      @csrf_exempt
      @route("/nambla/")
      def nambla_view():
          pass

Acknowledgements
----------------

Flask-BGCSRF is based on the work of [Steve Losh](https://bitbucket.org/sjl/flask-csrf/src).

                         / Lighthouse-web /

                 a Lighthouse web application


    ~ What is it?

      A Webserver to control the LEDs in a Lightbox. Its running on an raspi

    ~ How do I use it?

      1. edit the configuration in the factory.py file or
         export a LIGHTHOUSE_SETTINGS environment variable
         pointing to a configuration file or pass in a
         dictionary with config values using the create_app
         function.

      2. install the app from the root of the project directory

         sudo pip install --editable .

      3. instruct flask to use the right application

         export FLASK_APP="lighthouse_web"

      4. initialize the database with this command:

         --flask initdb--

      5. now you can run flaskr:

         flask run --host=0.0.0.0

         the application will greet you on
         http://raspberrypi:5000/

    ~ Is it tested?

      You betcha.  Run `python setup.py test` to see
      the tests pass.
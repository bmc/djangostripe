# Running this critter

## Stripe API

The Python Stripe API must be installed for this demo to work.

    $ pip install --index-url https://code.stripe.com --upgrade stripe

See <https://stripe.com/docs/libraries>.

## Database

The code currently assumes a MySQL database, so you'll need all the usual
Python and Django MySQL nonsense. The MySQL configuration parameters are in
`mysql.cnf`. Once you have MySQL set up, create the database and set the
permissions, as shown below:

    create database stripe character set utf8;
    grant all privileges on stripe.* to stripe @'localhost' identified by 'stripe';

## Environment

The `settings.py` file assumes the existence of the following environment
variables:

* STRIPE_PUBLISHABLE_KEY should be set to the test-mode Stripe publishable key.
* STRIPE_API_KEY should be set to the test-mode Stripe API key.

See your Stripe account for details.

These values *can* be configured directly in `settings.py`. The Stripe keys are
currently pulled from the environment for security reasons--namely, I don't
want to give *my* keys to *you*.

## Admin

I haven't enabled any of the admin screens. To create users, use the Django
shell. e.g.:

    $ python manage.py shell                   
    >>> User.objects.create_user('joeblow', 'joeblow@example.org', 'foobar')

## Stylesheet

The style sheet is maintained in SASS. Make sure there's a Ruby on your
system, as well as Ruby Gems, and then run the following:

    $ sudo gem install sass

### Before running

Generate `static/style.css` from `static/style.scss` as follows:

    $ sass static/style.scss

### While developing

During development, run this command:

    $ sass --watch static/style.scss

SASS will then detect when the `style.scss` file changes and automatically
regenerate `style.css`.


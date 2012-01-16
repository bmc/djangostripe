# Running this critter

## Stripe API

The Python Stripe API must be installed for this demo to work.

    $ pip install --index-url https://code.stripe.com --upgrade stripe

See <https://stripe.com/docs/libraries>.

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


# Django Stripe

This repository contains a sample [Django][] application that demonstrates
one way to integrate Django with the [Stripe][] payment gateway.

[Django]: http://www.djangoproject.com/
[Stripe]: http://stripe.com/

# Prerequisites

You'll need the following software:

* Python 2.5 or better.
* The Stripe Python API. (See below.)
* PyYAML. (See below.)
* Ruby and Sass, for stylesheet handling. (See below.)

## Stripe API

The Python Stripe API must be installed for this demo to work.

    $ pip install --index-url https://code.stripe.com --upgrade stripe

See <https://stripe.com/docs/libraries>.

## PyYAML

The fixtures (for initial data) use YAML, and they require PyYAML.

    $ pip install PyYAML

## Stripe

You must create a Stripe account to run this software.

# Database

## Create the MySQL Database

The code currently assumes a MySQL database, so you'll need all the usual
Python and Django MySQL nonsense. The MySQL configuration parameters are in
`mysql.cnf`. Once you have MySQL set up, create the database and set the
permissions, as shown below:

    mysql> create database stripe character set utf8;
    mysql> grant all privileges on stripe.* to stripe @'localhost' identified by 'stripe';

## Create the Database Tables and Initial Data

The `fixtures/stripetest-data.json` file contains some initial test products.
Sync'ing the Django database will load the fixture, as well.

    $ python manage.py syncdb

# Configuration

## Environment

The `settings.py` file assumes the existence of the following environment
variables:

* `STRIPE_PUBLISHABLE_KEY` should be set to your Stripe publishable key (test
  mode or live).
* `STRIPE_API_KEY` should be set to the Stripe API key (test mode or live).

See your Stripe account for details.

These values *can* be configured directly in `settings.py`. The Stripe keys are
currently pulled from the environment for security reasons--namely, I don't
want to give *my* keys to *you*.

## Administrators

You'll want to change the `ADMINS` value in `settings.py`.

# Admin

I haven't enabled any of the admin screens. To create users, use the Django
shell. e.g.:

    $ python manage.py shell                   
    >>> User.objects.create_user('joeblow', 'joeblow@example.org', 'foobar')

# Stylesheet

The style sheet is maintained in [Sass][]. Make sure there's a Ruby on your
system, as well as Ruby Gems, and then run the following:

    $ gem install sass

If you're using the system Ruby, you may have to run that command under `sudo`.

If you'd prefer to use [LESS][], or just straight CSS, it's not terribly
difficult to convert the `static/style.scss`.

[Sass]: http://sass-lang.com/
[LESS]: http://lesscss.org/

## Before running

Generate `static/style.css` from `static/style.scss` as follows:

    $ sass static/style.scss >static/style.css

## While developing

During development, run this command:

    $ sass --watch static/style.scss

SASS will then detect when the `style.scss` file changes and automatically
regenerate `style.css`.

# Miscellaneous

## jQuery

The code uses [jQuery][] and [jQuery-UI][], and this repo contains local copies
of both, located in the `static` directory. If you'd rather use CDN-hosted
copies, just edit the appropriate `<script>` element in the
`stripetest/templates/layouts/page.html` template.

[jQuery]: http://jquery.org
[jQuery-UI]: http://jqueryui.com


# Acknowledgements

I developed this software as a demonstration, while under contract to
[Alphabuyer][], LLC.

**Plug**: Alphabuyer is a group buying portal. To quote the Alphabuyer website:

> We research local suppliers and evaluate their current offerings. Then we
> negotiate special group deals (e.g. "What kind of deal will you give us if
> 100 people sign up?") We ask them to waive cancellation fees and other
> nonsense.

Check 'em out.

**Disclaimer**: While I have done consulting for Alphabuyer, this isn't a paid
plug. I happen to think they have a good product. Having worked with them, I
_know_ they're good people.

[Alphabuyer]: http://alphabuyer.com

# License and Copyright

This code is copyright &copy; [Alphabuyer][], LLC, and [ArdenTex][] Inc., and
is released under the [Creative Commons Attribution 3.0 Unported][] (CC BY 3.0)
license. Please see <http://creativecommons.org/licenses/by/3.0/legalcode>
for the complete license terms.

[ArdenTex]: http://www.ardentex.com/
[Creative Commons Attribution 3.0 Unported]: http://creativecommons.org/licenses/by/3.0/

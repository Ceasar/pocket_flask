
================================================================================
Pocket Flask
================================================================================

Tool to scaffold for Flask apps.

The primary design goal is speed of development; application setup time should
be minimized.

Installation
================================================================================

- Install [pip](http://www.pip-installer.org/en/latest/installing.html)

- Install [virtualenv](http://www.virtualenv.org/en/latest/#installation)

Bootstrapping
================================================================================

::

    git clone https://github.com/Ceasar/pocket_flask
    cd pocket_flask
    git remote rm origin
    git remote add origin <the location of my new git repository>
    git push -u origin master

Usage
================================================================================

Run the project via ``make server``, then navigate to http://localhost:5000/ to
see the running app.

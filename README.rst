================================================================================
pyexcel-odsw - Let you focus on data, instead of file formats
================================================================================

.. image:: https://raw.githubusercontent.com/pyexcel/pyexcel.github.io/master/images/patreon.png
   :target: https://www.patreon.com/pyexcel

.. image:: https://api.bountysource.com/badge/team?team_id=288537
   :target: https://salt.bountysource.com/teams/chfw-pyexcel

.. image:: https://travis-ci.org/pyexcel/pyexcel-odsw.svg?branch=master
   :target: http://travis-ci.org/pyexcel/pyexcel-odsw

.. image:: https://codecov.io/gh/pyexcel/pyexcel-odsw/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/pyexcel/pyexcel-odsw

.. image:: https://img.shields.io/gitter/room/gitterHQ/gitter.svg
   :target: https://gitter.im/pyexcel/Lobby

.. image:: https://readthedocs.org/projects/pyexcel-odsw/badge/?version=latest
   :target: http://pyexcel-odsw.readthedocs.org/en/latest/

Support the project
================================================================================

If your company has embedded pyexcel and its components into a revenue generating
product, please support me on `patreon <https://www.patreon.com/bePatron?u=5537627>`_
or `bounty source <https://salt.bountysource.com/teams/chfw-pyexcel>`_ to maintain
the project and develop it further.

If you are an individual, you are welcome to support me too and for however long
you feel like. As my backer, you will receive
`early access to pyexcel related contents <https://www.patreon.com/pyexcel/posts>`_.

And your issues will get prioritized if you would like to become my patreon as `pyexcel pro user`.

With your financial support, I will be able to invest
a little bit more time in coding, documentation and writing interesting posts.



Introduction
================================================================================
**pyexcel-odsw** does write an ods file using constant memory.



Installation
================================================================================

You can install pyexcel-odsw via pip:

.. code-block:: bash

    $ pip install pyexcel-odsw


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/pyexcel/pyexcel-odsw.git
    $ cd pyexcel-odsw
    $ python setup.py install



Development guide
================================================================================

Development steps for code changes

#. git clone https://github.com/pyexcel/pyexcel-odsw.git
#. cd pyexcel-odsw

Upgrade your setup tools and pip. They are needed for development and testing only:

#. pip install --upgrade setuptools pip

Then install relevant development requirements:

#. pip install -r rnd_requirements.txt # if such a file exists
#. pip install -r requirements.txt
#. pip install -r tests/requirements.txt

Once you have finished your changes, please provide test case(s), relevant documentation
and update CHANGELOG.rst.

.. note::

    As to rnd_requirements.txt, usually, it is created when a dependent
    library is not released. Once the dependecy is installed
    (will be released), the future
    version of the dependency in the requirements.txt will be valid.


How to test your contribution
------------------------------

Although `nose` and `doctest` are both used in code testing, it is adviable that unit tests are put in tests. `doctest` is incorporated only to make sure the code examples in documentation remain valid across different development releases.

On Linux/Unix systems, please launch your tests like this::

    $ make

On Windows systems, please issue this command::

    > test.bat

How to update test environment and update documentation
---------------------------------------------------------

Additional steps are required:

#. pip install moban
#. git clone https://github.com/moremoban/setupmobans.git # generic setup
#. git clone https://github.com/pyexcel/pyexcel-commons.git commons
#. make your changes in `.moban.d` directory, then issue command `moban`

What is pyexcel-commons
---------------------------------

Many information that are shared across pyexcel projects, such as: this developer guide, license info, etc. are stored in `pyexcel-commons` project.

What is .moban.d
---------------------------------

`.moban.d` stores the specific meta data for the library.

Acceptance criteria
-------------------

#. Has Test cases written
#. Has all code lines tested
#. Passes all Travis CI builds
#. Has fair amount of documentation if your change is complex
#. Please update CHANGELOG.rst
#. Please add yourself to CONTRIBUTORS.rst
#. Agree on NEW BSD License for your contribution



License
================================================================================

New BSD License

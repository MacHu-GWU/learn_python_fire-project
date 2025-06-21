
.. image:: https://readthedocs.org/projects/learn-python-fire/badge/?version=latest
    :target: https://learn-python-fire.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/learn_python_fire-project/actions/workflows/main.yml/badge.svg
    :target: https://github.com/MacHu-GWU/learn_python_fire-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/learn_python_fire-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/learn_python_fire-project

.. image:: https://img.shields.io/pypi/v/learn-python-fire.svg
    :target: https://pypi.python.org/pypi/learn-python-fire

.. image:: https://img.shields.io/pypi/l/learn-python-fire.svg
    :target: https://pypi.python.org/pypi/learn-python-fire

.. image:: https://img.shields.io/pypi/pyversions/learn-python-fire.svg
    :target: https://pypi.python.org/pypi/learn-python-fire

.. image:: https://img.shields.io/badge/✍️_Release_History!--None.svg?style=social&logo=github
    :target: https://github.com/MacHu-GWU/learn_python_fire-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/⭐_Star_me_on_GitHub!--None.svg?style=social&logo=github
    :target: https://github.com/MacHu-GWU/learn_python_fire-project

------

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://learn-python-fire.readthedocs.io/en/latest/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/learn_python_fire-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/learn_python_fire-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/learn_python_fire-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/learn-python-fire#files


Welcome to ``learn_python_fire`` Documentation
==============================================================================
.. image:: https://learn-python-fire.readthedocs.io/en/latest/_static/learn_python_fire-logo.png
    :target: https://learn-python-fire.readthedocs.io/en/latest/


Method 1. Python File as CLI
------------------------------------------------------------------------------
`app.py <https://github.com/MacHu-GWU/learn_python_fire-project/blob/main/app.py>`_

.. code-block:: bash

    $ python app.py
    Hello World!


Method 2. Python Package as CLI
------------------------------------------------------------------------------
First, put business logic implementation in a separate module `learn_python_fire/app1_impl.py <https://github.com/MacHu-GWU/learn_python_fire-project/blob/main/learn_python_fire/app1_impl.py>`_

Then, create a new Python file that use absolute import to import the python package, and put `fire.Fire` on top of the business logic implementation, like this `learn_python_fire/app1.py </Users/sanhehu/Documents/GitHub/learn_python_fire-project/learn_python_fire/app1.py>`_.

At the end, register the `learn_python_fire.app1:main` function in `pyproject.toml <https://github.com/MacHu-GWU/learn_python_fire-project/blob/main/pyproject.toml#L109>`_.

Then you can use ``lpf1`` as a command line interface (CLI).

.. code-block:: bash

    $ lpf1
    Hello World!

Or you can run it directly with Python for local testing.

.. code-block:: bash

    $ python learn_python_fire/app1.py
    Hello World!


.. _install:

Install
------------------------------------------------------------------------------

``learn_python_fire`` is released on PyPI, so all you need is to:

.. code-block:: console

    $ pip install learn-python-fire

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade learn-python-fire

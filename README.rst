stringcase
==========

Convert string cases between camel case, pascal case, snake case etc...

|Build Status| |PyPI Version|

Usage
~~~~~

.. code:: python

    import stringcase
    stringcase.camelcase('foo_bar_baz') # => "fooBarBaz"
    stringcase.camelcase('FooBarBaz') # => "fooBarBaz"
    stringcase.capitalcase('foo_bar_baz') # => "Foo_bar_baz"
    stringcase.capitalcase('FooBarBaz') # => "FooBarBaz"
    stringcase.constcase('foo_bar_baz') # => "FOO_BAR_BAZ"
    stringcase.constcase('FooBarBaz') # => "_FOO_BAR_BAZ"
    stringcase.lowercase('foo_bar_baz') # => "foo_bar_baz"
    stringcase.lowercase('FooBarBaz') # => "foobarbaz"
    stringcase.pascalcase('foo_bar_baz') # => "FooBarBaz"
    stringcase.pascalcase('FooBarBaz') # => "FooBarBaz"
    stringcase.pathcase('foo_bar_baz') # => "foo/bar/baz"
    stringcase.pathcase('FooBarBaz') # => "/foo/bar/baz"
    stringcase.sentencecase('foo_bar_baz') # => "Foo bar baz"
    stringcase.sentencecase('FooBarBaz') # => "Foo bar baz"
    stringcase.snakecase('foo_bar_baz') # => "foo_bar_baz"
    stringcase.snakecase('FooBarBaz') # => "_foo_bar_baz"
    stringcase.spinalcase('foo_bar_baz') # => "foo-bar-baz"
    stringcase.spinalcase('FooBarBaz') # => "-foo-bar-baz"
    stringcase.titlecase('foo_bar_baz') # => "Foo Bar Baz"
    stringcase.titlecase('FooBarBaz') # => " Foo Bar Baz"
    stringcase.trimcase('foo_bar_baz') # => "foo_bar_baz"
    stringcase.trimcase('FooBarBaz') # => "FooBarBaz"
    stringcase.uppercase('foo_bar_baz') # => "FOO_BAR_BAZ"
    stringcase.uppercase('FooBarBaz') # => "FOOBARBAZ"

 ### Install

::

    $ pip install stringcase

 License ------- This software is released under the `MIT
License <https://github.com/okunishinishi/python-stringcase/blob/master/LICENSE>`__.

 About this project --------

|Bitdeli Badge|

 ### Author

-  `Taka Okunishi <http://okunishitaka.com>`__

 ### Donation

Support this project and `others by
okunishinishi <https://gratipay.com/okunishinishi/>`__ via
`gratipay <https://gratipay.com/okunishinishi/>`__.

` <https://gratipay.com/okunishinishi/>`__

.. raw:: html

   <!-- Links start -->

.. raw:: html

   <!-- Links end-->

.. |Build Status| image:: http://img.shields.io/travis/okunishinishi/python-stringcase.svg?style=flat
   :target: http://travis-ci.org/okunishinishi/python-stringcase
.. |PyPI Version| image:: https://img.shields.io/pypi/v/stringcase.svg
   :target: https://pypi.python.org/pypi/stringcase
.. |Bitdeli Badge| image:: https://d2weczhvl823v0.cloudfront.net/okunishinishi/python-stringcase/trend.png
   :target: https://bitdeli.com/free

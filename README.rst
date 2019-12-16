stringcase
==========

Convert string cases between camel case, pascal case, snake case etc...

|build_status_badge| |coverage_badge| |pypi_version_badge|

Usage
-----

.. code:: python

    import stringcase
    stringcase.camelcase('foo_bar_baz') # => "fooBarBaz"
    stringcase.camelcase("_me") # => "me"
    stringcase.camelcase("__me") # => "me"
    stringcase.camelcase("-_me") # => 'me'
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
    stringcase.snakecase('FooBarBaz') # => "foo_bar_baz"
    stringcase.spinalcase('foo_bar_baz') # => "foo-bar-baz"
    stringcase.spinalcase('FooBarBaz') # => "-foo-bar-baz"
    stringcase.titlecase('foo_bar_baz') # => "Foo Bar Baz"
    stringcase.titlecase('FooBarBaz') # => " Foo Bar Baz"
    stringcase.trimcase('foo_bar_baz') # => "foo_bar_baz"
    stringcase.trimcase('FooBarBaz') # => "FooBarBaz"
    stringcase.uppercase('foo_bar_baz') # => "FOO_BAR_BAZ"
    stringcase.uppercase('FooBarBaz') # => "FOOBARBAZ"
    stringcase.alphanumcase('_Foo., Bar') # =>'FooBar'
    stringcase.alphanumcase('Foo_123 Bar!') # =>'Foo123Bar'
    stringcase.alphanumcase('Foo_123 Bar!', upper=False) # =>'foobar'
    


Install
-------

::

    $ pip install stringcase

License
-------

This software is released under the `MIT License <https://github.com/okunishinishi/python-stringcase/blob/master/LICENSE>`__.


Author
------

-  `Taka Okunishi <http://okunishitaka.com>`__

.. |build_status_badge| image:: http://img.shields.io/travis/okunishinishi/python-stringcase.svg?style=flat
   :target: http://travis-ci.org/okunishinishi/python-stringcase
.. |coverage_badge| image:: http://img.shields.io/coveralls/apeman-repo/apeman-task-contrib-coz.svg?style=flat
   :target: https://coveralls.io/github/apeman-repo/apeman-task-contrib-coz
.. |pypi_version_badge| image:: https://img.shields.io/pypi/v/stringcase.svg
   :target: https://pypi.python.org/pypi/stringcase


stringcase
=====

Convert string cases between camel case, pascal case, snake case etc...

[![Build Status][my_travis_badge_url]][my_travis_url]


### Usage


```Python
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

```

<a name="01-howto--install"></a>
### Install

```
$ pip install stringcase
```

<a name="10-license"></a>
License
-------
This software is released under the [MIT License][my_license_url].

<a name="11-project"></a>
About this project
--------

[![Bitdeli Badge][my_bitdeli_badge_url]][bitdeli_url]

<a name="11-project--author"></a>
### Author

+ [Taka Okunishi](http://okunishitaka.com)

<a name="11-project--donation"></a>
### Donation

Support this project and [others by okunishinishi][my_gratipay_url] via [gratipay][my_gratipay_url].

[<img src="https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.svg" alt="Support via Gratipay"/>][my_gratipay_url]


<!-- Links start -->

[bitdeli_url]: https://bitdeli.com/free
[my_bitdeli_badge_url]: https://d2weczhvl823v0.cloudfront.net/okunishinishi/python-stringcase/trend.png
[my_repo_url]: https://github.com/okunishinishi/python-stringcase
[my_travis_url]: http://travis-ci.org/okunishinishi/python-stringcase
[my_travis_badge_url]: http://img.shields.io/travis/okunishinishi/python-stringcase.svg?style=flat
[my_license_url]: https://github.com/okunishinishi/python-stringcase/blob/master/LICENSE
[my_gratipay_budge_url]: http://img.shields.io/gratipay/okunishinishi.svg?style=flat
[my_tag_url]: http://github.com/okunishinishi/python-stringcase/releases/tag/
[my_tag_badge_url]: http://img.shields.io/github/tag/okunishinishi/python-stringcase.svg?style=flat

<!-- Links end-->


"""Unit test for stringcase
"""

from unittest import TestCase
from os import path
import sys

sys.path.append(path.dirname(__file__))
import stringcase

print("here")


class StringcaseTest(TestCase):
    def test_camelcase(self):
        from stringcase import camelcase

        eq = self.assertEqual

        eq('fooBar', camelcase('foo_bar'))
        eq('fooBar', camelcase('FooBar'))
        eq('fooBar', camelcase('foo-bar'))
        eq('fooBar', camelcase('foo.bar'))
        eq('barBaz', camelcase('_bar_baz'))
        eq('barBaz', camelcase('.bar_baz'))
        eq('', camelcase(''))
        eq('none', camelcase(None))

    def test_capitalcase(self):
        from stringcase import capitalcase

        eq = self.assertEqual

        eq('', capitalcase(''))
        eq('FooBar', capitalcase('fooBar'))

    def test_constcase(self):
        from stringcase import constcase

        eq = self.assertEqual

        eq('FOO_BAR', constcase('fooBar'))
        eq('FOO_BAR', constcase('foo_bar'))
        eq('FOO_BAR', constcase('foo-bar'))
        eq('FOO_BAR', constcase('foo.bar'))
        eq('_BAR_BAZ', constcase('_bar_baz'))
        eq('_BAR_BAZ', constcase('.bar_baz'))
        eq('', constcase(''))
        eq('NONE', constcase(None))

    def test_lowercase(self):
        from stringcase import lowercase

        eq = self.assertEqual

        eq('none', lowercase(None))
        eq('', lowercase(''))
        eq('foo', lowercase('Foo'))

    def test_pascalcase(self):
        from stringcase import pascalcase

        eq = self.assertEqual

        eq('FooBar', pascalcase('foo_bar'))
        eq('FooBar', pascalcase('foo-bar'))
        eq('FooBar', pascalcase('foo.bar'))
        eq('BarBaz', pascalcase('_bar_baz'))
        eq('BarBaz', pascalcase('.bar_baz'))
        eq('', pascalcase(''))
        eq('None', pascalcase(None))

    def test_pathcase(self):
        from stringcase import pathcase

        eq = self.assertEqual

        eq('foo/bar', pathcase('fooBar'))
        eq('foo/bar', pathcase('foo_bar'))
        eq('foo/bar', pathcase('foo-bar'))
        eq('foo/bar', pathcase('foo.bar'))
        eq('/bar/baz', pathcase('_bar_baz'))
        eq('/bar/baz', pathcase('.bar_baz'))
        eq('', pathcase(''))
        eq('none', pathcase(None))

    def test_sentencecase(self):
        from stringcase import sentencecase

        eq = self.assertEqual
        eq('Foo bar', sentencecase('fooBar'))
        eq('Foo bar', sentencecase('foo_bar'))
        eq('Foo bar', sentencecase('foo-bar'))
        eq('Foo bar', sentencecase('foo.bar'))
        eq('Bar baz', sentencecase('_bar_baz'))
        eq('Bar baz', sentencecase('.bar_baz'))
        eq('', sentencecase(''))
        eq('None', sentencecase(None))

    def test_uppercase(self):
        from stringcase import uppercase

        eq = self.assertEqual

        eq('NONE', uppercase(None))
        eq('', uppercase(''))
        eq('FOO', uppercase('foo'))

    def test_snakecase(self):
        from stringcase import snakecase

        eq = self.assertEqual

        eq('foo_bar', snakecase('fooBar'))
        eq('foo_bar', snakecase('foo_bar'))
        eq('foo_bar', snakecase('foo-bar'))
        eq('foo_bar', snakecase('foo.bar'))
        eq('_bar_baz', snakecase('_bar_baz'))
        eq('_bar_baz', snakecase('.bar_baz'))
        eq('', snakecase(''))
        eq('none', snakecase(None))

    def test_spinalcase(self):
        from stringcase import spinalcase

        eq = self.assertEqual

        eq('foo-bar', spinalcase('fooBar'))
        eq('foo-bar', spinalcase('foo_bar'))
        eq('foo-bar', spinalcase('foo-bar'))
        eq('foo-bar', spinalcase('foo.bar'))
        eq('-bar-baz', spinalcase('_bar_baz'))
        eq('-bar-baz', spinalcase('.bar_baz'))
        eq('', spinalcase(''))
        eq('none', spinalcase(None))

    def test_titlecase(self):
        from stringcase import titlecase

        eq = self.assertEqual

        eq('Foo Bar', titlecase('fooBar'))
        eq('Foo Bar', titlecase('foo_bar'))
        eq('Foo Bar', titlecase('foo-bar'))
        eq('Foo Bar', titlecase('foo.bar'))
        eq(' Bar Baz', titlecase('_bar_baz'))
        eq(' Bar Baz', titlecase('.bar_baz'))
        eq('', titlecase(''))
        eq('None', titlecase(None))

    def test_trimcase(self):
        from stringcase import trimcase

        eq = self.assertEqual

        eq('foo bar baz', trimcase(' foo bar baz '))
        eq('', trimcase(''))

    def test_alphanumcase(self):
        from stringcase import alphanumcase

        eq = self.assertEqual

        eq('FooBar', alphanumcase('_Foo., Bar'))
        eq('Foo123Bar', alphanumcase('Foo_123 Bar!'))
        eq('', alphanumcase(''))
        eq('None', alphanumcase(None))


if __name__ == '__main__':
    from unittest import main

    main()
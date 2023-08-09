import unittest

from src.engine.card_maker import card_maker


class Test__card_maker(unittest.TestCase):

    def test_no_title(self):

        entries = [
            ['foo', '43%', '323,123 lines', 'XXXXXXXXXXXXXXX'],
            ['foooooooo', '3%', '323 lines', 'XXXXXXX'],
            ['a', '100%', '3 lines', 'XXXX'],
        ]
        align = [-1, 1, 1, -1]
        lang = 'yml'
        result = card_maker('', entries, align, lang)
        expected = (
            f'```{lang}\n'
            'foo         43%  323,123 lines  XXXXXXXXXXXXXXX\n'
            'foooooooo    3%      323 lines  XXXXXXX        \n'
            'a          100%        3 lines  XXXX           \n'
            '```'
        )
        self.assertEqual(result, expected)

    def test_with_title(self):

        title = '# Foo bar'
        entries = [
            ['foo', '43%', '323,123 lines', 'XXXXXXXXXXXXXXX'],
            ['foooooooo', '3%', '323 lines', 'XXXXXXX'],
            ['a', '100%', '3 lines', 'XXXX'],
        ]
        align = [-1, 1, 1, -1]
        lang = 'python'
        result = card_maker(title, entries, align, lang)
        expected = (
            f'{title}\n\n'
            f'```{lang}\n'
            'foo         43%  323,123 lines  XXXXXXXXXXXXXXX\n'
            'foooooooo    3%      323 lines  XXXXXXX        \n'
            'a          100%        3 lines  XXXX           \n'
            '```'
        )
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
import unittest

from src.constants import PB_CHAR, PB_LEN
from src.engine.get_line_card import LANG, writer
from src.engine.pb_maker import progress_bars


LINE_PER_REPO = {
    'foo-bar-baz': 1500,
    'foo': 500,
    'foo-bar': 50,
    'bar': 5,
}
TOTAL = 2055

PB1 = progress_bars(1500, TOTAL, PB_CHAR, PB_LEN)
PB2 = progress_bars(500, TOTAL, PB_CHAR, PB_LEN)
PB3 = progress_bars(50, TOTAL, PB_CHAR, PB_LEN)
SPACES2 = ' '*(len(PB1) - len(PB2))
SPACES3 = ' '*(len(PB1) - len(PB3))


class Test__writer(unittest.TestCase):

    def test_no_title(self):

        result = writer(3, False, '', LINE_PER_REPO)
        expected = (
            f'```{LANG}\n'
            f'foo-bar-baz  1,500 lines  73%  {PB1}\n'
            f'foo            500 lines  24%  {PB2}{SPACES2}\n'
            f'foo-bar         50 lines   2%  {PB3}{SPACES3}\n'
            '```'
        )
        self.assertEqual(result, expected)

    def test_with_title(self):

        title = '## Foo bar baz'
        result = writer(3, False, title, LINE_PER_REPO)
        expected = (
            f'{title}\n\n'
            f'```{LANG}\n'
            f'foo-bar-baz  1,500 lines  73%  {PB1}\n'
            f'foo            500 lines  24%  {PB2}{SPACES2}\n'
            f'foo-bar         50 lines   2%  {PB3}{SPACES3}\n'
            '```'
        )
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
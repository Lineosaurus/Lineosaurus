import unittest

from src.constants import PB_CHAR, PB_LEN, TYPE_TO_NAME
from src.engine.get_type_card import LANG, writer
from src.engine.pb_maker import progress_bars


NUM_SHOWN = 3
SHOW_APPROX = False
PREFER_EXTENSION = False
TITLE = 'foo'
LINE_PER_EXT = {
    '.py': 1500,
    '.css': 500,
    '.swift': 50,
    '.c': 5,
}
TOTAL = 2055

PB1 = progress_bars(1500, TOTAL, PB_CHAR, PB_LEN)
PB2 = progress_bars(500, TOTAL, PB_CHAR, PB_LEN)
PB3 = progress_bars(50, TOTAL, PB_CHAR, PB_LEN)


class Test__writer(unittest.TestCase):

    def test_prefer_extension_false(self):

        result = writer(NUM_SHOWN, SHOW_APPROX, PREFER_EXTENSION, TITLE, LINE_PER_EXT)
        expected = (
            f'{TITLE}\n\n'
            f'```{LANG}\n'
            f'1,500  lines of Python  73%  {PB1}\n'
            f'500    lines of CSS     24%  {PB2}\n'
            f'50     lines of Swift    2%  {PB3}\n'
            '```'
        )
        self.assertEqual(result, expected)

    def test_prefer_extension_true(self):

        PREFER_EXTENSION = True
        result = writer(NUM_SHOWN, SHOW_APPROX, PREFER_EXTENSION, TITLE, LINE_PER_EXT)
        expected = (
            f'{TITLE}\n\n'
            f'```{LANG}\n'
            f'1,500  lines of .py files     73%  {PB1}\n'
            f'500    lines of .css files    24%  {PB2}\n'
            f'50     lines of .swift files   2%  {PB3}\n'
            '```'
        )
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
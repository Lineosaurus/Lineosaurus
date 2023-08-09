import unittest

from src.constants import PB_CHAR, PB_LEN
from src.engine.get_line_card import LANG, writer


LINE_PER_REPO = {
    'foo-bar-baz': 1500,
    'foo': 500,
    'foo-bar': 50,
    'bar': 5,
}
TOTAL = 2055


class Test__writer(unittest.TestCase):

    def test_(self):

        pass


if __name__ == '__main__':
    unittest.main()
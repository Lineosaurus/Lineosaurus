import unittest

from src.engine.get_star_card import LANG, writer


PACK = {
    'foo-bar-baz': 1500,
    'foo': 500,
    'foo-bar': 50,
    'bar': 5,
}
TOTAL = 2055


class Test__writer(unittest.TestCase):

    def test_num_shown(self):
        
        pass


if __name__ == '__main__':
    unittest.main()
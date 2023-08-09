import unittest

from src.constants import PB_LEN
from src.engine.get_star_card import LANG, writer
from src.engine.pb_maker import progress_bars_alternating


PACK = {
    'foo-bar-baz': 1500,
    'foo': 500,
    'foo-bar': 50,
    'bar': 5,
}
TOTAL = 2055


class Test__writer(unittest.TestCase):

    def test_num_shown(self):

        pb1 = progress_bars_alternating(1500, TOTAL, '⭐️', '🌟', PB_LEN)
        pb2 = progress_bars_alternating(500, TOTAL, '⭐️', '🌟', PB_LEN)
        pb3 = progress_bars_alternating(50, TOTAL, '⭐️', '🌟', PB_LEN)
        pb4 = progress_bars_alternating(5, TOTAL, '⭐️', '🌟', PB_LEN)
        spaces2 = ' '*(len(pb1) - len(pb2))  # Note, '⭐️' counts as 2 chars in length
        spaces3 = ' '*(len(pb1) - len(pb3))
        spaces4 = ' '*(len(pb1) - len(pb4))
        
        result = writer(1, False, '', TOTAL, PACK)
        expected = (
            f'```{LANG}\n'
            f'foo-bar-baz  1,500 stargazers  73%  {pb1}\n'
            '```'
        )
        self.assertEqual(result, expected)

        result = writer(3, False, '', TOTAL, PACK)
        expected = (
            f'```{LANG}\n'
            f'foo-bar-baz  1,500 stargazers  73%  {pb1}\n'
            f'foo            500 stargazers  24%  {pb2}{spaces2}\n'
            f'foo-bar         50 stargazers   2%  {pb3}{spaces3}\n'
            '```'
        )
        self.assertEqual(result, expected)

        result = writer(5, False, '', TOTAL, PACK)
        expected = (
            f'```{LANG}\n'
            f'foo-bar-baz  1,500 stargazers  73%  {pb1}\n'
            f'foo            500 stargazers  24%  {pb2}{spaces2}\n'
            f'foo-bar         50 stargazers   2%  {pb3}{spaces3}\n'
            f'bar              5 stargazers   0%  {pb4}{spaces4}\n'
            '```'
        )
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
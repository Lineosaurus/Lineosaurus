import unittest

from src.engine.pb_maker import progress_bars, progress_bars_alternating


class Test__progress_bars(unittest.TestCase):

    def test(self):

        result = progress_bars(1, 10, 'X', 10)
        expected = 'X'
        self.assertEqual(result, expected)

        result = progress_bars(0, 10, 'X', 10)
        expected = ''
        self.assertEqual(result, expected)

        result = progress_bars(10, 10, 'X', 10)
        expected = 'X'*10
        self.assertEqual(result, expected)

        result = progress_bars(5, 10, 'X', 100)
        expected = 'X'*50
        self.assertEqual(result, expected)


class Test__progress_bars_alternating(unittest.TestCase):

    def test(self):

        result = progress_bars_alternating(0, 10, 'X', 'Y', 10)
        expected = ''
        self.assertEqual(result, expected)

        result = progress_bars_alternating(1, 10, 'X', 'Y', 10)
        expected = 'X'
        self.assertEqual(result, expected)

        result = progress_bars_alternating(2, 10, 'X', 'Y', 10)
        expected = 'XY'
        self.assertEqual(result, expected)

        result = progress_bars_alternating(5, 10, 'X', 'Y', 10)
        expected = 'XYXYX'
        self.assertEqual(result, expected)

        result = progress_bars_alternating(10, 10, 'X', 'Y', 10)
        expected = 'XY'*5
        self.assertEqual(result, expected)

        result = progress_bars_alternating(5, 10, 'X', 'Y', 100)
        expected = 'XY'*25
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
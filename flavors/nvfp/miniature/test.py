import unittest

from src.emulator import emulator_engine


class Test__compact_by_nvfp(unittest.TestCase):

    def test(self):
        result = emulator_engine('flavors/nvfp/miniature/emulate_nvfp_miniature.json')
        expected = """
"""
        self.assertEqual(result, expected.strip())


if __name__ == '__main__':
    unittest.main()
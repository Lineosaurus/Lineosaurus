import unittest

from src.emulator import emulator_engine


class Test__compact_by_nvfp(unittest.TestCase):

    def test(self):
        result = emulator_engine('flavors/nvfp/miniature/emulate_nvfp_miniature.json')
        ## Note: All variables with a (*) prefix can't be tested, as their values can't be reliably determined during testing at the moment.
        expected = """
_*OWNER_'s repos (3,500 lines of code, 12 commits, 99.9K chars)

```txt
test_data_dummyrepo1       6 commits  50%  ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆
test_data_dummypythonrepo  5 commits  42%  ▆▆▆▆▆▆▆▆▆▆▆▆
test_data_dummyasmrepo     1 commits   8%  ▆▆
```

*last update: _*DATE_ - _*CREDIT_*
"""
        self.assertEqual(result, expected.strip())


if __name__ == '__main__':
    unittest.main()
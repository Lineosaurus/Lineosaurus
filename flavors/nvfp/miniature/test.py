import unittest

from src.emulator import emulator_engine


class Test__compact_by_nvfp(unittest.TestCase):

    def test_20230809_1(self):
        result = emulator_engine('tests/emulate_engine_20230809_1.json')
        expected = """
## This a header

## This is also a header

### This is custom title

a

```txt
test_data_dummypythonrepo  1.3K lines  37%  ▆▆▆▆▆▆▆▆▆▆▆
test_data_dummyrepo1       1.2K lines  34%  ▆▆▆▆▆▆▆▆▆▆
test_data_dummyasmrepo       1K lines  29%  ▆▆▆▆▆▆▆▆▆
```

b

```txt
2.6K  lines of .sample files  75%  ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆
210   lines of .py files       6%  ▆▆
182   lines of .ipynb files    5%  ▆▆
140   lines of  files          4%  ▆
65    lines of .ts files       2%  ▆
58    lines of .c files        2%  
52    lines of .asm files      1%  
27    lines of .swift files    1%  
27    lines of .rb files       1%  
26    lines of .cpp files      1%  
25    lines of .js files       1%  
25    lines of .rs files       1%  
19    lines of .md files       1%  
15    lines of .ld files       0%  
13    lines of .sh files       0%  
```

c

```txt
test_data_dummypythonrepo  37 KiB  38%  ▆▆▆▆▆▆▆▆▆▆▆
test_data_dummyrepo1       31 KiB  32%  ▆▆▆▆▆▆▆▆▆▆
test_data_dummyasmrepo     29 KiB  30%  ▆▆▆▆▆▆▆▆▆
```

e

```txt
77.5K  characters of .sample files  78%  ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆
6K     characters of .py files       6%  ▆▆
5.2K   characters of  files          5%  ▆▆
4.4K   characters of .ipynb files    4%  ▆
1.6K   characters of .asm files      2%  
1.1K   characters of .ts files       1%  
865    characters of .c files        1%  
616    characters of .md files       1%  
487    characters of .rs files       0%  
441    characters of .swift files    0%  
422    characters of .js files       0%  
394    characters of .cpp files      0%  
380    characters of .rb files       0%  
301    characters of .sh files       0%  
200    characters of .ld files       0%  
```

g

```txt
test_data_dummyrepo1       6 commits  50%  ▆▆▆▆▆▆▆▆▆▆▆▆▆▆▆
test_data_dummypythonrepo  5 commits  42%  ▆▆▆▆▆▆▆▆▆▆▆▆
test_data_dummyasmrepo     1 commits   8%  ▆▆
```

h

```txt
test_data_dummypythonrepo  35 files  35%  ▆▆▆▆▆▆▆▆▆▆▆
test_data_dummyrepo1       34 files  34%  ▆▆▆▆▆▆▆▆▆▆
test_data_dummyasmrepo     30 files  30%  ▆▆▆▆▆▆▆▆▆
```

### This one is a footer
"""
        self.assertEqual(result, expected.strip())


if __name__ == '__main__':
    unittest.main()
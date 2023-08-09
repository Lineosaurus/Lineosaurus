import unittest

from src.engine.variables_pool import Vars, replace_vars


class Test__replace_vars(unittest.TestCase):

    def test1(self):

        Vars._LINE_ = 200
        Vars._LINES_ = 300
        text = '_LINE_ foo _LINE_ foo _LINES_ foo _LINE_ foo _LINES_'

        result = replace_vars(text)
        expected = '200 foo 200 foo 300 foo 200 foo 300'
        self.assertEqual(result, expected)

    def test2(self):

        Vars._LINE_ = 200
        Vars._OWNER_ = 'FooBar'
        text = 'foo _OWNER__LINE_'

        result = replace_vars(text)
        expected = 'foo FooBar200'
        self.assertEqual(result, expected)

    def test3(self):

        Vars._OWNER_ = 'FooBar'
        Vars._LINE_ = 10
        Vars._LINES_ = 20
        text = 'foo _OWNER_ _LINE_ foo _LINES_'
        
        result = replace_vars(text)
        expected = 'foo FooBar 10 foo 20'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
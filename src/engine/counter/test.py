import unittest

import os

from src.engine.counter import counter


## Note: these tests should be run on Linux because file sizes differ
##       between Windows and Linux due to the newline characters (\r\n and \n).


TEST_DIR = os.path.join(os.path.dirname(__file__), 'test_data')


class Test__counter(unittest.TestCase):

    def test_count_all(self):

        line_per_ext, size_per_ext, char_per_ext, file_per_ext = counter(None, None, TEST_DIR)

        expected = {
            '.txt': 4 + 2,
            '.md': 3,
            '.js': 1,
        }
        self.assertEqual(line_per_ext, expected)
        
        expected = {
            '.txt': 28 + 5,
            '.md': 12,
            '.js': 6,
        }
        self.assertEqual(size_per_ext, expected)

        expected = {
            '.txt': 28 + 5,
            '.md': 12,
            '.js': 6,
        }
        self.assertEqual(char_per_ext, expected)
        
        expected = {
            '.txt': 2,
            '.md': 1,
            '.js': 1,
        }
        self.assertEqual(file_per_ext, expected)

    def test_only_type_1(self):

        ONLY_TYPE = ['.txt']
        line_per_ext, size_per_ext, char_per_ext, file_per_ext = counter(ONLY_TYPE, None, TEST_DIR)

        expected = {
            '.txt': 4 + 2,
        }
        self.assertEqual(line_per_ext, expected)
        
        expected = {
            '.txt': 28 + 5,
        }
        self.assertEqual(size_per_ext, expected)
        
        expected = {
            '.txt': 28 + 5,
        }
        self.assertEqual(char_per_ext, expected)
        
        expected = {
            '.txt': 2,
        }
        self.assertEqual(file_per_ext, expected)

    def test_only_type_2(self):

        ONLY_TYPE = ['.txt', '.js']
        line_per_ext, size_per_ext, char_per_ext, file_per_ext = counter(ONLY_TYPE, None, TEST_DIR)

        expected = {
            '.txt': 4 + 2,
            '.js': 1,
        }
        self.assertEqual(line_per_ext, expected)
        
        expected = {
            '.txt': 28 + 5,
            '.js': 6,
        }
        self.assertEqual(size_per_ext, expected)
        
        expected = {
            '.txt': 28 + 5,
            '.js': 6,
        }
        self.assertEqual(char_per_ext, expected)
        
        expected = {
            '.txt': 2,
            '.js': 1,
        }
        self.assertEqual(file_per_ext, expected)

    def test_only_type_3(self):

        ONLY_TYPE = ['.txt', '.js', '.py']
        line_per_ext, size_per_ext, char_per_ext, file_per_ext = counter(ONLY_TYPE, None, TEST_DIR)

        expected = {
            '.txt': 4 + 2,
            '.js': 1,
        }
        self.assertEqual(line_per_ext, expected)
        
        expected = {
            '.txt': 28 + 5,
            '.js': 6,
        }
        self.assertEqual(size_per_ext, expected)
        
        expected = {
            '.txt': 28 + 5,
            '.js': 6,
        }
        self.assertEqual(char_per_ext, expected)
        
        expected = {
            '.txt': 2,
            '.js': 1,
        }
        self.assertEqual(file_per_ext, expected)
    
    def test_ignore_type_1(self):

        IGNORE_TYPE = ['.txt']
        line_per_ext, size_per_ext, char_per_ext, file_per_ext = counter(None, IGNORE_TYPE, TEST_DIR)

        expected = {
            '.md': 3,
            '.js': 1,
        }
        self.assertEqual(line_per_ext, expected)
        
        expected = {
            '.md': 12,
            '.js': 6,
        }
        self.assertEqual(size_per_ext, expected)
        
        expected = {
            '.md': 12,
            '.js': 6,
        }
        self.assertEqual(char_per_ext, expected)
        
        expected = {
            '.md': 1,
            '.js': 1,
        }
        self.assertEqual(file_per_ext, expected)
    
    def test_ignore_type_2(self):

        IGNORE_TYPE = ['.txt', '.js']
        line_per_ext, size_per_ext, char_per_ext, file_per_ext = counter(None, IGNORE_TYPE, TEST_DIR)

        expected = {
            '.md': 3,
        }
        self.assertEqual(line_per_ext, expected)
        
        expected = {
            '.md': 12,
        }
        self.assertEqual(size_per_ext, expected)
        
        expected = {
            '.md': 12,
        }
        self.assertEqual(char_per_ext, expected)
        
        expected = {
            '.md': 1,
        }
        self.assertEqual(file_per_ext, expected)
    
    def test_ignore_type_3(self):

        IGNORE_TYPE = ['.py']
        line_per_ext, size_per_ext, char_per_ext, file_per_ext = counter(None, IGNORE_TYPE, TEST_DIR)

        expected = {
            '.txt': 4 + 2,
            '.md': 3,
            '.js': 1,
        }
        self.assertEqual(line_per_ext, expected)
        
        expected = {
            '.txt': 28 + 5,
            '.md': 12,
            '.js': 6,
        }
        self.assertEqual(size_per_ext, expected)

        expected = {
            '.txt': 28 + 5,
            '.md': 12,
            '.js': 6,
        }
        self.assertEqual(char_per_ext, expected)
        
        expected = {
            '.txt': 2,
            '.md': 1,
            '.js': 1,
        }
        self.assertEqual(file_per_ext, expected)
    
    def test_only_type_and_ignore_type(self):

        ONLY_TYPE = ['.txt']
        IGNORE_TYPE = ['.py']  # Will be ignored
        line_per_ext, size_per_ext, char_per_ext, file_per_ext = counter(ONLY_TYPE, IGNORE_TYPE, TEST_DIR)

        expected = {
            '.txt': 4 + 2,
        }
        self.assertEqual(line_per_ext, expected)
        
        expected = {
            '.txt': 28 + 5,
        }
        self.assertEqual(size_per_ext, expected)
        
        expected = {
            '.txt': 28 + 5,
        }
        self.assertEqual(char_per_ext, expected)
        
        expected = {
            '.txt': 2,
        }
        self.assertEqual(file_per_ext, expected)


if __name__ == '__main__':
    unittest.main()
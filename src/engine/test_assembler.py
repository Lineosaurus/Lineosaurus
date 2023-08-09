import unittest

from src.engine.assembler import CREDIT, assembler


HEADER = 'header'
CUSTOM_TITLE = 'custom_title'
CARDS = 'cards'
FOOTER = 'footer'
SHOW_CREDIT = True
AUTO_LINE_BREAK = True


class Test__assembler(unittest.TestCase):

    def test_normal(self):
        result = assembler(HEADER, CUSTOM_TITLE, CARDS, FOOTER, SHOW_CREDIT, AUTO_LINE_BREAK)
        expected = (
            f'{HEADER}\n\n'
            f'{CUSTOM_TITLE}\n\n'
            f'{CARDS}\n\n'
            f'{FOOTER}\n\n'
            f'{CREDIT}'
        )
        self.assertEqual(result, expected)

    def test_no_header(self):
        result = assembler('', CUSTOM_TITLE, CARDS, FOOTER, SHOW_CREDIT, AUTO_LINE_BREAK)
        expected = (
            f'{CUSTOM_TITLE}\n\n'
            f'{CARDS}\n\n'
            f'{FOOTER}\n\n'
            f'{CREDIT}'
        )
        self.assertEqual(result, expected)
    
    def test_no_custom_title(self):
        result = assembler(HEADER, '', CARDS, FOOTER, SHOW_CREDIT, AUTO_LINE_BREAK)
        expected = (
            f'{HEADER}\n\n'
            f'{CARDS}\n\n'
            f'{FOOTER}\n\n'
            f'{CREDIT}'
        )
        self.assertEqual(result, expected)
    
    def test_no_cards(self):
        result = assembler(HEADER, CUSTOM_TITLE, '', FOOTER, SHOW_CREDIT, AUTO_LINE_BREAK)
        expected = (
            f'{HEADER}\n\n'
            f'{CUSTOM_TITLE}\n\n'
            f'{FOOTER}\n\n'
            f'{CREDIT}'
        )
        self.assertEqual(result, expected)
    
    def test_no_footer(self):
        result = assembler(HEADER, CUSTOM_TITLE, CARDS, '', SHOW_CREDIT, AUTO_LINE_BREAK)
        expected = (
            f'{HEADER}\n\n'
            f'{CUSTOM_TITLE}\n\n'
            f'{CARDS}\n\n'
            f'{CREDIT}'
        )
        self.assertEqual(result, expected)

    def test_no_credit(self):
        SHOW_CREDIT = False
        result = assembler(HEADER, CUSTOM_TITLE, CARDS, FOOTER, SHOW_CREDIT, AUTO_LINE_BREAK)
        expected = (
            f'{HEADER}\n\n'
            f'{CUSTOM_TITLE}\n\n'
            f'{CARDS}\n\n'
            f'{FOOTER}'
        )
        self.assertEqual(result, expected)
    
    def test_no_auto_line_break(self):
        AUTO_LINE_BREAK = False
        result = assembler(HEADER, CUSTOM_TITLE, CARDS, FOOTER, SHOW_CREDIT, AUTO_LINE_BREAK)
        expected = HEADER + CUSTOM_TITLE + CARDS + FOOTER + CREDIT
        self.assertEqual(result, expected)
    
    def test_just_header(self):
        result = assembler(HEADER, '', '', '', False, AUTO_LINE_BREAK)
        expected = HEADER
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
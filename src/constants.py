

__version__ = '1.0'


PB_CHAR = '▆'  # Default progress bars character
PB_LEN = 30  # Progress bars length

"""
Cards
-----
line: lines of code per repository
type: lines of code per extension (across entire owner's repositories)
size: file sizes per repository
stat: summary
char: number of characarter per extension
star: number of stargazers per repository
cmit: number of commits per repository
file: number of files per repository
"""
CARDS = ['line', 'type', 'size', 'stat', 'char', 'star', 'cmit', 'file']

NON_TEXT_TYPE = [

    ## Images
    '.jpg', '.jpeg', '.png', '.gif',

    ## Videos
    '.mp4',

    ## Audios
    '.mp3',

    ## .git/
    '.idx', '.pack', '.rev',
]
NON_TEXT_FILENAME = [

    ## .git/
    'index',
]

TYPE_TO_NAME = {
    '.py': 'Python',
    '.js': 'JavaScript',
    '.java': 'Java',
    '.cpp': 'C++',
    '.html': 'HTML',
    '.css': 'CSS',
    '.rb': 'Ruby',
    '.php': 'PHP',
    '.swift': 'Swift',
    '.kt': 'Kotlin',
    '.pl': 'Perl',
    '.sh': 'Shell',
    '.xml': 'XML',
    '.json': 'JSON',
    '.sql': 'SQL',
    '.md': 'Markdown',
    '.txt': 'Plain Text',
    '.c': 'C',
    '.h': 'C Header',
    '.go': 'Go',
    '.ts': 'TypeScript',
    '.pyc': 'Python Compiled File',
    '.jar': 'Java Archive',
    '.exe': 'Executable',
    '.dll': 'Dynamic Link Library',
    '.ppt': 'PowerPoint',
    '.pdf': 'PDF',
    '.jpg': 'JPEG Image',
    '.png': 'PNG Image',
    '.mp3': 'MP3 Audio',
    '.mp4': 'MP4 Video',
}
"""

"""

from vyapp.tools.misc import get_file_extension
from re import escape

DEFAULT = '#'
TABLE   = { 
              'py'   :'#',
              'sh'   :'#',
              'c'    :'//',
              'c++'  :'//',
              'java' : '//'
          }

def add_inline_comment(area):
    """
    It adds inline comment to selected lines based on the file extesion.
    """

    comment = TABLE.get(get_file_extension(area.filename), DEFAULT)
    def rep(index0, index1):
        return '%s%s ' % (area.get(index0, index1), comment)
    area.tag_replace_ranges('sel', '^ +|^', rep)

def rm_inline_comment(area):
    """
    It removes the inline comments.
    """

    comment = TABLE.get(get_file_extension(area.filename), DEFAULT)
    def rep(index0, index1):
        chk = area.get(index0, index1)
        chk = chk.replace('%s ' % comment, '')
        chk = chk.replace(comment, '')
        return chk
    area.tag_replace_ranges('sel', '^ *%s ?' % comment, rep)


INSTALL = [(2, '<Key-r>', lambda event: rm_inline_comment(event.widget)),
           (2, '<Key-e>', lambda event: add_inline_comment(event.widget))]

def install(area):
    area.install(*INSTALL)

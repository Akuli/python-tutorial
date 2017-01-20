#!/usr/bin/env python3

# This is free and unencumbered software released into the public
# domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a
# compiled binary, for any purpose, commercial or non-commercial, and
# by any means.

# In jurisdictions that recognize copyright laws, the author or
# authors of this software dedicate any and all copyright interest in
# the software to the public domain. We make this dedication for the
# benefit of the public at large and to the detriment of our heirs
# and successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to
# this software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <http://unlicense.org>

"""Create HTML files of the tutorial."""

import os
import shutil
import string
import sys
import webbrowser

import common

try:
    import mistune
except ImportError:
    print("mistune isn't installed. You can install it like this:")
    print()
    print(">>> import pip")
    print(">>> pip.main(['install', '--user', 'mistune'])")
    sys.exit(1)

try:
    import pygments.formatters
    import pygments.lexers
except ImportError:
    # we can work without pygments, but we won't get colors
    pygments = None


HTML_TEMPLATE = """\
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>{title}</title>
  </head>
  <body>
    {body}
  </body>
</html>
"""


def mkdir_slashfix_open(filename, mode):
    """Like common.slashfix_open(), but make directories as needed."""
    filename = common.slashfix(filename)
    directory = os.path.dirname(filename)
    os.makedirs(directory, exist_ok=True)
    return open(filename, mode)


def fix_filename(filename):
    if filename == 'README.md' or filename.endswith('/README.md'):
        # 'README.md' -> 'index.html'
        # 'some/place/README.md' -> 'some/place/index.html'
        return filename[:-9] + 'index.html'
    if filename.endswith('.md'):
        return filename[:-3] + '.html'
    return filename


class TutorialRenderer(mistune.Renderer):

    def __init__(self):
        super().__init__()
        self.title = None   # will be set by header()
        self._headercounts = {}

    def _get_header_link(self, title):
        """Return a github-style link target for a title.

        >>> r = TutorialRenderer()
        >>> r._get_header_link('Hello there!')
        'hello-there'
        >>> r._get_header_link('Hello there!')
        'hello-there-1'
        >>> r._get_header_link('Hello there!')
        'hello-there-2'
        >>>
        """
        result = ''
        for character in title:
            if character in string.whitespace:
                result += '-'
            elif character in string.punctuation:
                pass
            else:
                result += character.lower()

        if result not in self._headercounts:
            # this title appears in this file for the first time
            self._headercounts[result] = 1
            return result
        # there has been already a link with the same text on this page,
        # we need to do thetitle, thetitle-1, thetitle-2, etc.
        real_result = '%s-%d' % (result, self._headercounts[result])
        self._headercounts[result] += 1
        return real_result

    def header(self, text, level, raw):
        """Create a header that is also a link and a # link target."""
        # "# raw"
        if level == 1:
            self.title = text
        target = self._get_header_link(raw)
        content = super().header(text, level, raw)
        return '<a name="{0}" href="#{0}">{1}</a>'.format(target, content)

    def link(self, link, title, text):
        """Return a link that points to the correct file."""
        # "[text](link)"
        if link.startswith('#'):
            # it's like "#title", no need to do anything
            pass
        elif '#' in link:
            # it's like "some-file#title", we need to fix some-file
            before, after = link.split('#', 1)
            link = fix_filename(before) + '#' + after
        else:
            # it's like "some-file"
            link = fix_filename(link)
        return super().link(link, title, text)

    def block_code(self, code, lang=None):
        """Highlight Python code blocks with Pygments if it's installed."""
        if lang == 'py' and pygments is not None:
            # we can highlight it
            if code.startswith('>>> '):
                lexer = pygments.lexers.PythonConsoleLexer()
            else:
                lexer = pygments.lexers.PythonLexer()
            formatter = pygments.formatters.HtmlFormatter(
                style='tango',
                noclasses=True)
            return pygments.highlight(code, lexer, formatter)
        # we can't highlight it
        return super().block_code(code, lang)

    def image(self, src, title, text):
        """Return an image inside a link."""
        result = super().image(src, title, text)
        return self.link(src, title, result)

    def table(self, header, body):
        """Return a table with a border."""
        result = super().table(header, body)
        return result.replace('<table>', '<table border="1">', 1)


def main():
    if pygments is None:
        print("Pygments isn't installed. You can install it like this:")
        print()
        print(">>> import pip")
        print(">>> pip.main(['install', '--user', 'Pygments'])")
        print()
        print("You can also continue without Pygments, but the code examples")
        print("will not be in color.")
        if not common.askyesno("Continue without pygments?"):
            print("Interrupt.")
            return

    if os.path.exists('html'):
        if not common.askyesno("html exists. Do you want to remove it?"):
            print("Interrupt.")
            return
        if os.path.isdir('html'):
            shutil.rmtree('html')
        else:
            os.remove('html')

    print("Generating HTML files...")
    for markdownfile in common.get_markdown_files():
        htmlfile = os.path.join('html', fix_filename(markdownfile))
        print(' ', markdownfile, '->', htmlfile)
        with common.slashfix_open(markdownfile, 'r') as f:
            markdown = f.read()
        renderer = TutorialRenderer()
        body = mistune.markdown(markdown, renderer=renderer)
        html = HTML_TEMPLATE.format(title=renderer.title, body=body)
        with mkdir_slashfix_open(htmlfile, 'w') as f:
            print(html, file=f)

    print("Copying other files...")
    shutil.copytree('images', os.path.join('html', 'images'))
    shutil.copy('LICENSE', os.path.join('html', 'LICENSE'))

    print("\n*********************\n")
    print("Ready! The files are in the html directory.")
    print("Go to html and double-click index.html to read the tutorial.")
    print()
    if common.askyesno("Do you want to view the tutorial now?", default=False):
        print("Opening the tutorial...")
        webbrowser.open(os.path.join('html', 'index.html'))


if __name__ == '__main__':
    main()

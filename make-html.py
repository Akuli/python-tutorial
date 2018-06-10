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

import argparse
import os
import posixpath
import shutil
import sys
import textwrap
import webbrowser

try:
    import mistune
except ImportError:
    import platform
    if platform.system() == 'Windows':
        python = 'py'
    else:
        python = 'python3'
    print("mistune isn't installed.", file=sys.stderr)
    print("You can install it by running this command on a terminal or ")
    print("command prompt:")
    print()
    print("    %s -m pip install --user mistune" % python)
    sys.exit(1)

try:
    import pygments.formatters
    import pygments.lexers
    import pygments.style
    import pygments.styles
    import pygments.token
except ImportError:
    # we can work without pygments, but we won't get colors
    pygments = None

import common


if pygments is not None:
    class TutorialStyle(pygments.style.Style):
        background_color = '#111111'
        styles = {
            pygments.token.Comment: 'italic #336666',
            pygments.token.Keyword: 'bold #6699cc',
            pygments.token.Name.Builtin: '#9966ff',
            pygments.token.String: '#ffff33',
            pygments.token.Name.Exception: 'bold #ff0000',
        }


HTML_TEMPLATE = """\
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="stylesheet" type="text/css" href="{stylefile}">
  </head>
  <body>
    {body}
  </body>
</html>
"""


def mkdir_slashfix_open(filename, mode):
    """Like common.slashfix_open(), but make directories as needed."""
    real_filename = common.slashfix(filename)
    directory = os.path.dirname(real_filename)
    os.makedirs(directory, exist_ok=True)
    return open(real_filename, mode)


def fix_filename(filename):
    renames = [('README.md', 'index.html'),
               ('LICENSE', 'LICENSE.txt')]
    for before, after in renames:
        if posixpath.basename(filename) == before:
            # BEFORE -> AFTER
            # some/place/BEFORE -> some/place/AFTER
            return filename[:-len(before)] + after
    if filename.endswith('.md'):
        filename = filename[:-3] + '.html'
    return filename


class TutorialRenderer(mistune.Renderer):

    def __init__(self, pygments_style):
        super().__init__()
        self.pygments_style = pygments_style
        self.title = None   # will be set by header()

    def header(self, text, level, raw):
        """Create a header that is also a link and a # link target."""
        # "# raw"
        if level == 1:
            self.title = text
        target = common.header_link(raw)
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
        if lang == 'python' and pygments is not None:
            # we can highlight it
            if code.startswith('>>> '):
                lexer = pygments.lexers.PythonConsoleLexer(python3=True)
            else:
                lexer = pygments.lexers.Python3Lexer()
            formatter = pygments.formatters.HtmlFormatter(
                style=self.pygments_style, noclasses=True)
            return pygments.highlight(code, lexer, formatter)

        elif lang == 'diff':
            # http://stackoverflow.com/a/39413824
            result = []
            for line in code.split('\n'):
                line = line.strip()
                if not line:
                    continue

                if line.startswith('+'):
                    result.append('<p><font color="green">%s</font></p>'
                                  % line.strip('+'))
                elif line.startswith('-'):
                    result.append('<p><font color="red">%s</font></p>'
                                  % line.strip('-'))
                else:
                    result.append('<p>%s</p>' % line)

            return '\n'.join(result)

        else:
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


def wrap_text(text):
    """Like textwrap.fill, but respects newlines."""
    result = []
    for part in text.split('\n'):
        result.append(textwrap.fill(part))
    return '\n'.join(result)


def main():
    desc = ("Create HTML files of the tutorial.\n\n"
            "The files have light text on a dark background by "
            "default, and you can edit html-style.css to change that.")
    if pygments is not None:
        desc += (
            " Editing the style file doesn't change the colors of the "
            "code examples, but you can use the --pygments-style "
            "option. Search for 'pygments style gallery' online or see "
            "https://help.farbox.com/pygments.html to get an idea of "
            "what different styles look like.")

    parser = argparse.ArgumentParser(
        description=wrap_text(desc),
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '-o', '--outdir', default='html',
        help="write the HTML files here, defaults to %(default)r")
    if pygments is not None:
        parser.add_argument(
            '--pygments-style', metavar='STYLE', default=TutorialStyle,
            choices=list(pygments.styles.get_all_styles()),
            help=("the Pygments color style (see above), "
                  "defaults to a custom style"))
    args = parser.parse_args()

    if pygments is None:
        print("Pygments isn't installed. You can install it like this:")
        print()
        print(">>> import pip")
        print(">>> pip.main(['install', '--user', 'pygments'])")
        print()
        print("You can also continue without Pygments, but the code examples")
        print("will not be colored.")
        if not common.askyesno("Continue without pygments?"):
            print("Interrupt.")
            return
        args.pygments_style = None

    if os.path.exists(args.outdir):
        if not common.askyesno("%s exists. Do you want to remove it?"
                               % args.outdir):
            print("Interrupt.")
            return
        if os.path.isdir(args.outdir):
            shutil.rmtree(args.outdir)
        else:
            os.remove(args.outdir)

    print("Generating HTML files...")
    for markdownfile in common.get_markdown_files():
        fixed_file = fix_filename(markdownfile)
        htmlfile = posixpath.join(args.outdir, fixed_file)
        print('  %-30.30s  -->  %-30.30s' % (markdownfile, htmlfile), end='\r')

        with common.slashfix_open(markdownfile, 'r') as f:
            markdown = f.read()
        renderer = TutorialRenderer(args.pygments_style)
        body = mistune.markdown(markdown, renderer=renderer)
        stylefile = posixpath.relpath(
            'style.css', posixpath.dirname(fixed_file))

        html = HTML_TEMPLATE.format(
            title=renderer.title,
            body=body,
            stylefile=stylefile,
        )
        with mkdir_slashfix_open(htmlfile, 'w') as f:
            print(html, file=f)
    print()

    print("Copying other files...")
    shutil.copytree('images', os.path.join(args.outdir, 'images'))
    shutil.copy('LICENSE', os.path.join(args.outdir, 'LICENSE.txt'))
    shutil.copy('html-style.css', os.path.join(args.outdir, 'style.css'))

    print("\n*********************\n")
    print("Ready! The files are in %r." % args.outdir)
    print("You can go there and double-click index.html to read the tutorial.")
    print()
    if common.askyesno("Do you want to view the tutorial now?", default=False):
        print("Opening the tutorial...")
        webbrowser.open(os.path.join(args.outdir, 'index.html'))


if __name__ == '__main__':
    main()

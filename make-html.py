#!/usr/bin/env python3
"""Create HTML files of the tutorial."""

import glob
import shutil
import os
import sys
import webbrowser

try:
    import mistune
except ImportError:
    print("mistune isn't installed. You can install it like this:")
    print()
    print(">>> import pip")
    print(">>> pip.main(['install', '--user', 'mistune'])")
    sys.exit(1)


def main():
    if os.path.exists('html'):
        if input("html exists. Do you want "
                 "to remove it? [Y/n] ").upper() == 'N':
            print("Interrupt.")
            return
        if os.path.isdir('html'):
            shutil.rmtree('html')
        else:
            os.remove('html')
    os.mkdir('html')
    print("Generating HTML files...")
    for markdownfile in glob.glob('*.md'):
        htmlfile = os.path.join('html', markdownfile[:-3] + '.html')
        print(' ', markdownfile, '->', htmlfile)
        with open(markdownfile, 'r') as f1:
            with open(htmlfile, 'w') as f2:
                md = f1.read()
                md = md.replace('.md', '.html')
                html = mistune.markdown(md)
                print(html, file=f2)
    os.rename(os.path.join('html', 'README.html'),
              os.path.join('html', 'index.html'))
    shutil.copytree('images', os.path.join('html', 'images'))
    print()
    print("*********************")
    print()
    print("Ready! The files are in the html directory,")
    print("double-click html/index.html to read the tutorial.")
    print()
    if input("Do you want to view the tutorial now? [Y/n] ").upper() != 'N':
        print("Opening the tutorial...")
        webbrowser.open(os.path.join('html', 'index.html'))


if __name__ == '__main__':
    main()

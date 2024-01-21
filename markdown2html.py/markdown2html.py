#!/usr/bin/python3
"""
markdown2html.py - Convert Markdown to HTML.

Usage: ./markdown2html.py README.md README.html
"""

import sys
import os
import markdown

def convert_markdown_to_html(markdown_file, output_file):
    """Converts Markdown file to HTML."""
    if not os.path.isfile(markdown_file):
        print("Missing {}".format(markdown_file), file=sys.stderr)
        sys.exit(1)

    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.read()
        html_content = markdown.markdown(markdown_content)

    with open(output_file, 'w') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(markdown_file, output_file)
    sys.exit(0)


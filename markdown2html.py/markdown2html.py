#!/usr/bin/python3
"""
Markdown to HTML Converter

Usage:
    ./markdown2html.py input_file output_file
"""

import sys
import re

def convert_markdown_to_html(markdown_text):
    """
    Convert Markdown to HTML with support for headings.

    Args:
        markdown_text (str): Input Markdown text.

    Returns:
        str: Converted HTML text.
    """
    lines = markdown_text.split('\n')
    html_lines = []

    for line in lines:
        match = re.match(r'^(#{1,6})\s(.+)$', line)
        if match:
            heading_level = len(match.group(1))
            heading_text = match.group(2)
            html_line = f'<h{heading_level}>{heading_text}</h{heading_level}>'
            html_lines.append(html_line)
        else:
            html_lines.append(line)

    return '\n'.join(html_lines)

def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r') as file:
            markdown_text = file.read()

        html_text = convert_markdown_to_html(markdown_text)

        with open(output_file, 'w') as file:
            file.write(html_text)

        print(f"Conversion successful. HTML written to {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

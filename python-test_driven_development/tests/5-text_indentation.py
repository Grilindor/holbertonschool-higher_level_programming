#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cut_mark = [".", "?", ":"]
    lines = []
    current_line = ""

    for char in text:
        current_line += char
        if char in cut_mark:
            lines.append(current_line.strip())
            lines.append("")
            current_line = ""

    if current_line:
        lines.append(current_line.strip())

    for line in lines:
        print(line)

if __name__ == "__main__":
    import doctest
    doctest.testmod(text_indentation.txt)

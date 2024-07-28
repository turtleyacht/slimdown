import re

def is_command(line):
    return re.match(r"\s{4}", line) != None

def is_list(line):
    return re.match(r"\s{2}", line) != None

def is_paragraph(line):
    return not is_command(line) and not is_list(line) and not is_title(line) and re.match(r"\S+", line) != None

def is_title(line):
    return re.match(r"\s{5,}", line) != None

import re


def parse(markdown):
    lines = markdown.split('\n')
    result = ''
    in_list = False
    in_list_append = False
    for line in lines:
        if re.match('###### (.*)', line) is not None:
            line = '<h6>' + line[7:] + '</h6>'
        elif re.match('## (.*)', line) is not None:
            line = '<h2>' + line[3:] + '</h2>'
        elif re.match('# (.*)', line) is not None:
            line = '<h1>' + line[2:] + '</h1>'
        emphasis = re.match(r'\* (.*)', line)
        if emphasis:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                current_text = emphasis.group(1)
                bold = match_boldness(current_text)
                if bold:
                    current_text = bold.group(1) + '<strong>' + \
                        bold.group(2) + '</strong>' + bold.group(3)
                    is_bold = True
                bold = match_italicness(current_text)
                if bold:
                    current_text = bold.group(1) + '<em>' + bold.group(2) + \
                        '</em>' + bold.group(3)
                    is_italic = True
                line = '<ul><li>' + current_text + '</li>'
            else:
                is_bold = False
                is_italic = False
                current_text = emphasis.group(1)
                bold = match_boldness(current_text)
                if bold:
                    is_bold = True
                bold = match_italicness(current_text)
                if bold:
                    is_italic = True
                if is_bold:
                    current_text = bold.group(1) + '<strong>' + \
                        bold.group(2) + '</strong>' + bold.group(3)
                if is_italic:
                    current_text = bold.group(1) + '<em>' + bold.group(2) + \
                        '</em>' + bold.group(3)
                line = '<li>' + current_text + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        emphasis = re.match('<h|<ul|<p|<li', line)
        if not emphasis:
            line = '<p>' + line + '</p>'
        emphasis = match_boldness(line)
        if emphasis:
            line = emphasis.group(1) + '<strong>' + emphasis.group(2) + \
                '</strong>' + emphasis.group(3)
        emphasis = match_italicness(line)
        if emphasis:
            line = emphasis.group(1) + '<em>' + \
                emphasis.group(2) + '</em>' + emphasis.group(3)
        if in_list_append:
            line = '</ul>' + line
            in_list_append = False
        result += line
    if in_list:
        result += '</ul>'
    return result


def match_boldness(text):
    return re.match('(.*)__(.*)__(.*)', text)


def match_italicness(text):
    return re.match('(.*)_(.*)_(.*)', text)

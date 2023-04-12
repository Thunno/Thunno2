from thunno2.commands import commands, DIGRAPHS, get_a_function, Void
from thunno2.constants import CONSTANTS
from thunno2.codepage import codepage_index


"""Splits Thunno 2 code into tokens to make it easier for the interpreter"""


def tokenise(code, expected_end=''):
    index = 0
    ret = []
    while index < len(code):
        char = code[index]
        if char in commands:
            ret.append((char, 'command', commands[char]))
        elif char in DIGRAPHS:
            index += 1
            try:
                x = code[index]
                ret.append((char, 'digraph', get_a_function(char + x)))
            except:
                pass
        elif char in '0123456789.':
            s = char
            index += 1
            try:
                while code[index] in '0123456789.':
                    s += code[index]
                    index += 1
            except:
                pass
            index -= 1
            try:
                while s[0] == '0':
                    ret.append(('0', 'number', 0))
                    try:
                        s = s[1:]
                    except:
                        break
                if s == '.':
                    ret.append(('.', 'number', 0.5))
                else:
                    x = eval(s)
                    if s.endswith('.'):
                        x += 0.5
                    ret.append((s, 'number', x))
            except:
                pass
        elif char == '"':
            s = char
            index += 1
            try:
                while (code[index] != '"') or (code[index - 1] == '\\'):
                    s += code[index]
                    index += 1
                s += code[index]
            except:
                s += '"'
            try:
                ret.append((s, 'string', eval(s).replace('¶', '\n')))
            except:
                ret.append((s, 'string', s[1:-1].replace('¶', '\n')))
        elif char == '\'':
            index += 1
            try:
                x = code[index]
                ret.append(('\'' + x, 'one character', x))
            except:
                ret.append(('\'', 'one character', ''))
        elif char == '`':
            index += 2
            x = code[index - 1: index + 1]
            ret.append(('`' + x, 'two characters', x))
        elif char == 'ʋ':
            index += 3
            x = code[index - 2: index + 1]
            ret.append(('ʋ' + x, 'three characters', x))
        elif char == '[':
            s = char
            index += 1
            try:
                in_string = ''
                nests = 1
                while nests:
                    c = code[index]
                    s += c
                    if in_string == '' and c in ('"', "'"):
                        in_string = c
                    elif in_string != '' and c == in_string:
                        if code[index - 1] != '\\':
                            in_string = ''
                    if in_string == '':
                        if c == '[':
                            nests += 1
                        elif c == ']':
                            nests -= 1
                    index += 1
            except:
                s += ']'
            try:
                ret.append((s, 'list', eval(s)))
            except:
                ret.append((s, 'list', s))
        elif char == ']':
            ret.append((']', 'list', []))
        elif char == '#':
            index += 1
            try:
                if code[index] == ' ':
                    while code[index] not in '¶\n':
                        index += 1
                elif code[index] == '{':
                    while code[index] != '#' or code[index - 1] != '}':
                        index += 1
            except:
                pass
        elif char == '“':
            compressed_string = ''
            index += 1
            try:
                while code[index] != char:
                    compressed_string += code[index]
                    index += 1
            except:
                pass
            ret.append((char + compressed_string + char, 'lowercase alphabetic compression', compressed_string))
        elif char == '”':
            compressed_string = ''
            index += 1
            try:
                while code[index] != char:
                    compressed_string += code[index]
                    index += 1
            except:
                pass
            ret.append((char + compressed_string + char, 'title case alphabetic compression', compressed_string))
        elif char == '‘':
            compressed_string = ''
            index += 1
            try:
                while code[index] != char:
                    compressed_string += code[index]
                    index += 1
            except:
                pass
            ret.append((char + compressed_string + char, 'lowercase dictionary compression', compressed_string))
        elif char == '’':
            compressed_string = ''
            index += 1
            try:
                while code[index] != char:
                    compressed_string += code[index]
                    index += 1
            except:
                pass
            ret.append((char + compressed_string + char, 'title case dictionary compression', compressed_string))
        elif char == '»':
            compressed_string = ''
            index += 1
            try:
                while code[index] != char:
                    compressed_string += code[index]
                    index += 1
            except:
                pass
            ret.append((char + compressed_string + char, 'compressed number', compressed_string))
        elif char == '«':
            compressed_string = code[index + 1:index + 3]
            index += 2
            ret.append((char + compressed_string, 'small compressed number', compressed_string))
        elif char == '¿':
            compressed_string = ''
            index += 1
            try:
                while code[index] != char:
                    compressed_string += code[index]
                    index += 1
            except:
                pass
            ret.append((char + compressed_string + char, 'compressed list', compressed_string))
        elif char == '¡':
            index += 1
            try:
                var = code[index]
            except:
                var = ''
            ret.append((char + var, 'variable get', var))
        elif char == '!':
            index += 1
            try:
                var = code[index]
            except:
                var = ''
            ret.append((char + var, 'variable set', var))
        elif char == '€':
            index += 1
            cmd = code[index]
            if cmd in DIGRAPHS:
                index += 1
                cmd += code[index]
            func = get_a_function(cmd)
            ret.append((char + cmd, 'single function map', func))
        elif char == 'ȷ':
            index += 1
            cmd = code[index]
            if cmd in DIGRAPHS:
                index += 1
                cmd += code[index]
            func = get_a_function(cmd)
            ret.append((char + cmd, 'outer product', func))
        elif char == 'œ':
            index += 1
            cmd = code[index]
            if cmd in DIGRAPHS:
                index += 1
                cmd += code[index]
            func = get_a_function(cmd)
            ret.append((char + cmd, 'single function filter', func))
        elif char == 'þ':
            index += 1
            cmd = code[index]
            if cmd in DIGRAPHS:
                index += 1
                cmd += code[index]
            func = get_a_function(cmd)
            ret.append((char + cmd, 'single function sort by', func))
        elif char == 'ñ':
            index += 1
            cmd = code[index]
            if cmd in DIGRAPHS:
                index += 1
                cmd += code[index]
            func = get_a_function(cmd)
            ret.append((char + cmd, 'single function group by', func))
        elif char == 'n':
            ret.append((char, 'context variable', 0))
        elif char == 'ṅ':
            ret.append((char, 'iteration index', 0))
        elif char == 'x':
            ret.append((char, 'get x', 0))
        elif char == 'y':
            ret.append((char, 'get y', 0))
        elif char == 'X':
            ret.append((char, 'set x', 0))
        elif char == 'Y':
            ret.append((char, 'set y', 0))
        elif char == 'ẋ':
            ret.append((char, 'set x without popping', 0))
        elif char == 'ẏ':
            ret.append((char, 'set y without popping', 0))
        elif char == 'ẋ':
            ret.append((char, 'increment x', 0))
        elif char == 'ẏ':
            ret.append((char, 'increment y', 0))
        elif char == 'Ȥ':
            ret.append((char, 'get global array', 0))
        elif char == 'ȥ':
            ret.append((char, 'add to global array', 0))
        elif char == 'K':
            ret.append((char, 'stack', 0))
        elif char == 'k':
            index += 1
            try:
                if code[index] in CONSTANTS:
                    x = code[index]
                    ret.append((char + x, 'constant', CONSTANTS[x]))
            except:
                pass
        elif char == 'ṇ':
            index += 1
            try:
                x = code[index]
                ret.append((char + x, 'codepage compression', next(codepage_index(x)) + 101))
            except:
                pass
        elif char == 'q':
            ret.append((char, 'quit', 0))
        elif char == '$':
            ret.append((char, 'next input', 0))
        elif char == '¤':
            ret.append((char, 'input list', 0))
        elif char == '°':
            ret.append((char, 'first input', 0))
        elif char == '¹':
            ret.append((char, 'second input', 0))
        elif char == '⁶':
            ret.append((char, 'third input', 0))
        elif char == '⁷':
            ret.append((char, 'third last input', 0))
        elif char == '⁸':
            ret.append((char, 'second last input', 0))
        elif char == '⁹':
            ret.append((char, 'last input', 0))
        elif char == '£':
            ret.append((char, 'print', 0))
        elif char == '¢':
            ret.append((char, 'print without newline', 0))
        elif char == 'ß':
            ret.append((char, 'print without popping', 0))
        elif char == 'ı':
            i, r = tokenise(code[index + 1:], expected_end=';')
            index += i
            ret.append((char, 'map', r))
        elif char == 'æ':
            i, r = tokenise(code[index + 1:], expected_end=';')
            index += i
            ret.append((char, 'filter', r))
        elif char == 'Þ':
            i, r = tokenise(code[index + 1:], expected_end=';')
            index += i
            ret.append((char, 'sort by', r))
        elif char == 'Ñ':
            i, r = tokenise(code[index + 1:], expected_end=';')
            index += i
            ret.append((char, 'group by', r))
        elif char == '¥':
            i, r = tokenise(code[index + 1:], expected_end=';')
            index += i
            ret.append((char, 'fixed point', r))
        elif char == 'Ƙ':
            i, r = tokenise(code[index + 1:], expected_end=';')
            index += i
            ret.append((char, 'first n integers', r))
        elif char == 'Ʋ':
            i, r = tokenise(code[index + 1:], expected_end=';')
            index += i
            ret.append((char, 'cumulative reduce by', r))
        elif char == '{':
            i, r = tokenise(code[index + 1:], expected_end='}')
            index += i
            ret.append((char, 'for loop', r))
        elif char == '(':
            i, r1 = tokenise(code[index + 1:], expected_end=';)')
            index += i + 1
            r2 = []
            try:
                if code[index] == ';':
                    i, r2 = tokenise(code[index + 1:], expected_end=')')
                    index += i
            except:
                pass
            ret.append((char, 'while loop', (r1, r2)))
        elif char == '?':
            i, r1 = tokenise(code[index + 1:], expected_end=':;')
            index += i + 1
            r2 = []
            try:
                if code[index] == ':':
                    i, r2 = tokenise(code[index + 1:], expected_end=';')
                    index += i
            except:
                pass
            ret.append((char, 'if statement', (r1, r2)))
        elif char == 'Ɓ':
            index += 1
            cmd = code[index]
            if cmd in DIGRAPHS:
                index += 1
                cmd += code[index]
            func = get_a_function(cmd)
            ret.append((char + cmd, 'execute without popping', func))
        elif char == 'ç':
            try:
                index += 1
                cmd1 = code[index]
                if cmd1 in DIGRAPHS:
                    index += 1
                    cmd1 += code[index]
                func1 = get_a_function(cmd1)
            except:
                func1, cmd1 = Void, ''
            try:
                index += 1
                cmd2 = code[index]
                if cmd2 in DIGRAPHS:
                    index += 1
                    cmd2 += code[index]
                func2 = get_a_function(cmd2)
            except:
                func2, cmd2 = Void, ''
            ret.append((char + cmd1 + cmd2, 'pair apply', (func1, func2)))
        elif char == 'Ç':
            try:
                index += 1
                cmd1 = code[index]
                if cmd1 in DIGRAPHS:
                    index += 1
                    cmd1 += code[index]
                func1 = get_a_function(cmd1)
            except:
                func1, cmd1 = Void, ''
            try:
                index += 1
                cmd2 = code[index]
                if cmd2 in DIGRAPHS:
                    index += 1
                    cmd2 += code[index]
                func2 = get_a_function(cmd2)
            except:
                func2, cmd2 = Void, ''
            ret.append((char + cmd1 + cmd2, 'two function map', (func1, func2)))
        elif char in expected_end:
            return index, ret
        index += 1
    return index + 1, ret

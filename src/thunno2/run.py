from thunno2 import lexer, version, flags
import sys


def from_terminal():
    print('Thunno', version.THUNNO_VERSION, 'interpreter\n')
    print('\nFlags:')
    flags_list = input()
    code = ''
    print('\nHeader:')
    inp = input()
    while inp:
        code += inp + '\n'
        inp = input()
    print('\nCode:')
    inp = input()
    while inp:
        code += inp + '\n'
        inp = input()
    print('\nFooter:')
    inp = input()
    while inp:
        code += inp + '\n'
        inp = input()
    inputs = ''
    print('\nInput:')
    inp = input()
    while inp:
        inputs += inp + '\n'
        inp = input()
    _, tokenised = lexer.tokenise(code)
    print('\nOutput:')
    flags.run(flags_list, tokenised, inputs)


def from_cmdline():
    args = sys.argv[1:]
    if not args:
        from_terminal()
        return None
    filename = args[0]
    flags_list = args[1:]
    sys.stderr.write('Thunno, v' + version.THUNNO_VERSION + '\n')
    try:
        with open(filename) as f:
            _, tokenised = lexer.tokenise(f.read())
            flags.run(''.join(flags_list), tokenised, sys.stdin.read())
    except Exception as E:
        sys.stderr.write('An error occurred: ' + repr(E))

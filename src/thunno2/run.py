from thunno2 import lexer, version, flags, tokens, autoexplanation
import sys


def from_terminal():
    print("Thunno", version.THUNNO_VERSION, "interpreter\n")
    print("\nFlags:")
    flags_list = input()
    code = ""
    print("\nHeader:")
    inp = input()
    while inp:
        code += inp + "\n"
        inp = input()
    print("\nCode:")
    inp = input()
    while inp:
        code += inp + "\n"
        inp = input()
    print("\nFooter:")
    inp = input()
    while inp:
        code += inp + "\n"
        inp = input()
    inputs = ""
    print("\nInput:")
    inp = input()
    while inp:
        inputs += inp + "\n"
        inp = input()
    if "e" in flags_list:
        print("\nExplanation:\n\n" + autoexplanation.auto_explain(code) + "\n")
    if "v" in flags_list:
        transpiled = tokens.transpile(code)
        print("\nTranspiled:")
        print(transpiled)
        print()
        _, tokenised = lexer.tokenise(transpiled)
    else:
        _, tokenised = lexer.tokenise(code)
    print("\nOutput:")
    flags.run(flags_list, tokenised, inputs)


def from_cmdline():
    args = sys.argv[1:]
    if not args:
        from_terminal()
        return None
    filename = args[0]
    flags_list = args[1:]
    sys.stderr.write("Thunno, v" + version.THUNNO_VERSION + "\n")
    try:
        with open(filename) as f:
            code = f.read()
            if "e" in "".join(flags_list):
                sys.stderr.write(
                    "\nExplanation:\n\n" + autoexplanation.auto_explain(code) + "\n"
                )
            if "v" in "".join(flags_list):
                transpiled = tokens.transpile(code)
                print("Transpiled:", transpiled, file=sys.stderr)
                _, tokenised = lexer.tokenise(transpiled)
            else:
                _, tokenised = lexer.tokenise(code)
            flags.run("".join(flags_list), tokenised, sys.stdin.read())
    except Exception as E:
        sys.stderr.write("An error occurred: " + repr(E))

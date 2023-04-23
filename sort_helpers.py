# Inspired by Vyxal (https://github.com/Vyxal/Vyxal/blob/main/sort_element_functions.py)

import re

f = open("src/thunno2/helpers.py", "r", encoding="utf-8")
file = f.read()
f.close()

fns = [
    x.strip()
    for x in re.findall(
        "(?:@.+\n)*def +[a-zA-Z_][a-zA-Z_\d]*\s*\([\S\s]*?\)(?: *-> *.+?)?\:(?:\n(?:(?:    |\t).*)?)+",
        file,
    )[2:]
]

file = file.split("\n")

start_line = file.index(fns[0].split("\n")[0])
last_line = file.index(fns[-1].split("\n")[-1])

f = open("src/thunno2/helpers.py", "w", encoding="utf-8")

f.write(
    "\n".join(file[:start_line])
    + "\n"
    + "\n\n\n".join(sorted(fns, key=lambda x: x[x.index("def ") :])).strip()
    + "\n\n\n"
    + "\n".join(file[last_line + 1 :]).strip()
    + "\n"
)

f.close()

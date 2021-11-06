from pathlib import Path
from pprint import pprint
from re import findall
from subprocess import run
from tempfile import TemporaryDirectory


repo = 'https://github.com/freedesktop/xorg-proto-x11proto.git'
pattern = r'#define XK_(\w+)\s+0x(\w+)(?:\s+/\*\s+U\+(\w+))?'


def main():
    keysymdef = []

    with TemporaryDirectory() as temp:
        run(['git', 'clone', repo, '.'], cwd=temp)
        text = Path(temp, 'keysymdef.h').read_text()
        for name, sym, uni in findall(pattern, text):
            sym = int(sym, 16)
            uni = int(uni, 16) if uni else None
            keysymdef.append((name, sym, uni))

    with open('keysymdef.py', 'w') as f:
        f.write('keysymdef = \\\n')
        pprint(keysymdef, f)


if __name__ == '__main__':
    main()

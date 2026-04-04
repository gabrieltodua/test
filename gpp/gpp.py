#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════╗
║          G++ Programming Language            ║
║                Version 2.0.0                 ║
╚══════════════════════════════════════════════╝
"""

import sys
import re
import os
import tempfile
import subprocess

VERSION = "2.0.0"

RESET   = '\033[0m'
BOLD    = '\033[1m'
DIM     = '\033[2m'
RED     = '\033[91m'
GREEN   = '\033[92m'
YELLOW  = '\033[93m'
BLUE    = '\033[94m'
CYAN    = '\033[96m'

def print_banner():
    print(f"""
{CYAN}{BOLD}   ██████╗      ██╗  ██╗   ██╗
  ██╔════╝      ╚██╗██╔╝  ██╔╝
  ██║  ███╗      ╚███╔╝  ██╔╝ 
  ██║   ██║      ██╔██╗ ██╔╝  
  ╚██████╔╝     ██╔╝╚██╗██╔╝  
   ╚═════╝      ╚═╝  ╚═╝╚═╝   {RESET}
{BLUE}{BOLD}  G++ Language{RESET}  {CYAN}v{VERSION}{RESET}
{DIM}  ────────────────────────────────{RESET}
""")

# ─────────────────────────────────────────────────────────────────────────────
#  Runtime — injected at the top of every transpiled program
# ─────────────────────────────────────────────────────────────────────────────

RUNTIME = '''\
import time   as __time__
import sys    as __sys__
import math   as __math__
import random as __random__
import os     as __os__

# ════════════════════════════════════════════════════════
#  G++ Standard Library  v2.0
# ════════════════════════════════════════════════════════

# ── Output & Input ───────────────────────────────────────
def say(*args, sep=" ", end="\\n"):
    print(*args, sep=sep, end=end)

def ask(prompt=""):
    return input(prompt)

def clear_screen():
    __os__.system("clear" if __os__.name == "posix" else "cls")

# ── Type Checking & Conversion ────────────────────────────
def rank(x):         return type(x).__name__
def tonum(x):
    try:    return int(x)
    except: return float(x)
def totext(x):       return str(x)
def tolist(x):       return list(x)
def isnull(x):       return x is None
def isnum(x):        return isinstance(x, (int, float))
def istext(x):       return isinstance(x, str)
def islist(x):       return isinstance(x, list)

# ── Core ──────────────────────────────────────────────────
def sig(x):          return len(x)
def pa(*args):       return min(args[0]) if len(args)==1 else min(*args)
def di(*args):       return max(args[0]) if len(args)==1 else max(*args)

# ── Math ──────────────────────────────────────────────────
def abso(x):         return abs(x)
def sqrt(x):         return __math__.sqrt(x)
def floor(x):        return __math__.floor(x)
def ceil(x):         return __math__.ceil(x)
def rnd(x, d=0):     return round(x, int(d))
def even(n):         return n % 2 == 0
def odd(n):          return n % 2 != 0
def clamp(v,lo,hi):  return max(lo, min(hi, v))
def avg(lst):        return sum(lst) / len(lst)
def total(lst):      return sum(lst)
def pow_of(b, e):    return b ** e

# ── Random ────────────────────────────────────────────────
def chance():        return __random__.random()
def dice(a, b):      return __random__.randint(int(a), int(b))
def pick(lst):       return __random__.choice(lst)
def shuffle(lst):    __random__.shuffle(lst)

# ── Strings ───────────────────────────────────────────────
def upper(s):        return str(s).upper()
def lower(s):        return str(s).lower()
def trim(s):         return str(s).strip()
def split(s,sep=" "): return str(s).split(sep)
def join(sep,lst):   return sep.join(str(x) for x in lst)
def replace(s,o,n):  return str(s).replace(o,n)
def has(s,item):     return item in s
def startswith(s,p): return str(s).startswith(p)
def endswith(s,p):   return str(s).endswith(p)
def repeat(s,n):     return str(s) * int(n)
def flip(s):         return str(s)[::-1]
def chars(s):        return list(str(s))
def pad(s,w,c=" "): return str(s).center(int(w),c)
def padleft(s,w,c=" "): return str(s).rjust(int(w),c)
def padright(s,w,c=" "): return str(s).ljust(int(w),c)
def numwords(s):     return len(str(s).split())
def cut_str(s,a,b):  return str(s)[int(a):int(b)]

# ── Lists ─────────────────────────────────────────────────
def add(lst, item):  lst.append(item)
def cut(lst, item):  lst.remove(item)
def ind(lst, item):  return lst.index(item)
def __gpp_del__(lst): return lst.pop()
def cler(lst):       lst.clear()
def sort(lst,r=False): return sorted(lst, reverse=r)
def rev(lst):        lst.reverse()
def copy(lst):       return lst.copy()
def howmany(lst,item): return lst.count(item)
def flat(lst):       return [x for s in lst for x in (s if isinstance(s,list) else [s])]
def first(lst):      return lst[0]
def last(lst):       return lst[-1]
def slice_list(lst,a,b): return lst[int(a):int(b)]
def unique(lst):
    seen=[]
    [seen.append(x) for x in lst if x not in seen]
    return seen
def zip_lists(a,b):  return list(zip(a,b))
def insert(lst,i,v): lst.insert(int(i), v)
def merge(a,b):      return a + b

# ── Utility / Time ────────────────────────────────────────
def wait(ms):        __time__.sleep(ms / 1000)
def now():
    import datetime
    return str(datetime.datetime.now().strftime("%H:%M:%S"))
def today():
    import datetime
    return str(datetime.date.today())

# ── Constants ─────────────────────────────────────────────
TAR  = True
FYU  = False
PI   = __math__.pi
E    = __math__.e
NULL = None

# ═════════════════════════════════════════════════════════
'''

# ─────────────────────────────────────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────────────────────────────────────

def _string_spans(line):
    spans, i, n = [], 0, len(line)
    while i < n:
        if line[i] in ('"', "'"):
            q, j = line[i], i + 1
            while j < n:
                if line[j] == '\\': j += 2; continue
                if line[j] == q:
                    spans.append((i, j+1)); i = j+1; break
                j += 1
            else: i = j
        else: i += 1
    return spans

def in_string(pos, spans):
    return any(s <= pos < e for s,e in spans)

def safe_re_sub(pattern, repl, line, flags=0):
    spans = _string_spans(line)
    result, last = [], 0
    for m in re.finditer(pattern, line, flags):
        if in_string(m.start(), spans):
            result.append(line[last:m.end()]); last = m.end()
        else:
            result.append(line[last:m.start()])
            result.append(m.expand(repl) if isinstance(repl, str) else repl(m))
            last = m.end()
    result.append(line[last:])
    return ''.join(result)

# ─────────────────────────────────────────────────────────────────────────────
#  Line Transformer
# ─────────────────────────────────────────────────────────────────────────────

def transform_line(line):
    stripped = line.lstrip()
    indent   = line[:len(line) - len(stripped)]
    if not stripped or stripped.startswith('#'):
        return line

    c = stripped

    # Structure
    c = re.sub(r'^fuc\b',         'def',   c)
    c = re.sub(r'^con\s+loop\b',  'for',   c)
    c = re.sub(r'^won\s+loop\b',  'while', c)

    # Declarations
    c = re.sub(r'^make\s+(?:int|str|f(?:loat)?)\s+(\w)', r'\1', c)
    c = re.sub(r'^make\s+', '', c)
    c = re.sub(r'^set\s+(\w+)\s*=', r'\1 =', c)

    # Flow
    c = re.sub(r'^rt\b',   'return',   c)
    c = re.sub(r'^stop\b', 'break',    c)
    c = re.sub(r'^skip\b', 'continue', c)

    # Built-in renames
    c = safe_re_sub(r'\bdel\s*\(', '__gpp_del__(', c)
    c = safe_re_sub(r'(?<!\w)f\(', 'float(', c)

    # Literals & constants
    c = safe_re_sub(r'\bTAR\b',  'True',  c)
    c = safe_re_sub(r'\bFYU\b',  'False', c)
    c = safe_re_sub(r'\bNULL\b', 'None',  c)
    c = safe_re_sub(r'\bPI\b',   '__math__.pi', c)
    c = safe_re_sub(r'\bE\b',    '__math__.e',  c)

    # Operators
    c = safe_re_sub(r'\^',              '**',  c)
    c = safe_re_sub(r'(?<=\s)&(?=\s)',  'and', c)
    c = safe_re_sub(r'(?<=\s)\|(?=\s)', 'or',  c)
    c = safe_re_sub(r'(?<![=!<>])!(?!=)', 'not ', c)

    return indent + c

# ─────────────────────────────────────────────────────────────────────────────
#  Transpiler
# ─────────────────────────────────────────────────────────────────────────────

RUNTIME_LINES = len(RUNTIME.splitlines()) + 1

def transpile(source):
    output = [RUNTIME]
    for raw in source.splitlines():
        try:    output.append(transform_line(raw))
        except: output.append(raw)
    return '\n'.join(output)

def format_error(stderr_text):
    lines  = stderr_text.strip().splitlines()
    output = [f"\n{RED}{BOLD}  ✗  G++ Error{RESET}\n"]
    for line in lines:
        if any(x in line for x in ['__gpp', 'Traceback', 'RUNTIME', '_gpp_']): continue
        m = re.search(r'line (\d+)', line)
        if m:
            adjusted = max(1, int(m.group(1)) - RUNTIME_LINES)
            line = line[:m.start()] + f'line {adjusted}' + line[m.end():]
        output.append(f"  {DIM}{line}{RESET}")
    return '\n'.join(output)

# ─────────────────────────────────────────────────────────────────────────────
#  Runner
# ─────────────────────────────────────────────────────────────────────────────

def run_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            source = f.read()
    except FileNotFoundError:
        print(f"  {RED}✗  File not found:{RESET} {path}"); sys.exit(1)
    except Exception as e:
        print(f"  {RED}✗  Cannot read file:{RESET} {e}"); sys.exit(1)

    python_src = transpile(source)
    tmp_fd, tmp_path = tempfile.mkstemp(suffix='.py', prefix='gpp_')
    try:
        with os.fdopen(tmp_fd, 'w', encoding='utf-8') as tf:
            tf.write(python_src)
        proc = subprocess.run([sys.executable, tmp_path], stderr=subprocess.PIPE, text=True)
        if proc.returncode != 0:
            print(format_error(proc.stderr))
        return proc.returncode
    except Exception as e:
        print(f"  {RED}✗  Internal error:{RESET} {e}"); return 1
    finally:
        try: os.unlink(tmp_path)
        except: pass

# ─────────────────────────────────────────────────────────────────────────────
#  Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print_banner()
    if len(sys.argv) < 2:
        print(f"  {YELLOW}Usage:{RESET}   gpp <file.G++>")
        print(f"  {DIM}Example: gpp main.G++{RESET}\n")
        sys.exit(0)

    path = sys.argv[1]
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)

    if os.path.splitext(path)[1] not in ('.G++', '.g++'):
        print(f"  {YELLOW}⚠  Warning: Expected .G++ extension{RESET}\n")

    print(f"  {CYAN}File   {RESET} {BOLD}{os.path.basename(path)}{RESET}")
    print(f"  {CYAN}Path   {RESET} {DIM}{os.path.dirname(path)}{RESET}")
    print(f"  {DIM}{'─' * 38}{RESET}\n")

    rc = run_file(path)

    print(f"\n  {DIM}{'─' * 38}{RESET}")
    if rc == 0:
        print(f"  {GREEN}✓  Done — no errors{RESET}\n")
    else:
        print(f"  {RED}✗  Exited with error code {rc}{RESET}\n")
    sys.exit(rc)

if __name__ == '__main__':
    main()

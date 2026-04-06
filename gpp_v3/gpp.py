#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════╗
║          G++ Programming Language            ║
║                Version 3.0.0                 ║
╚══════════════════════════════════════════════╝
"""

import sys, re, os, tempfile, subprocess, glob

VERSION = "3.0.0"

RESET  = '\033[0m'
BOLD   = '\033[1m'
DIM    = '\033[2m'
RED    = '\033[91m'
GREEN  = '\033[92m'
YELLOW = '\033[93m'
BLUE   = '\033[94m'
CYAN   = '\033[96m'
PURPLE = '\033[95m'
WHITE  = '\033[97m'

# ─────────────────────────────────────────────────────────
#  Banner
# ─────────────────────────────────────────────────────────

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

# ─────────────────────────────────────────────────────────
#  Runtime — injected into every program
# ─────────────────────────────────────────────────────────

RUNTIME = '''\
import time   as __time__
import sys    as __sys__
import math   as __math__
import random as __random__
import os     as __os__
import json   as __json__

# ════════════════════════════════════════════════════════
#  G++ Standard Library  v3.0
# ════════════════════════════════════════════════════════

# ── Output & Input ───────────────────────────────────────
def say(*args, sep=" ", end="\\n"):
    print(*args, sep=sep, end=end)

def ask(prompt=""):
    return input(prompt)

def clear_screen():
    __os__.system("clear" if __os__.name == "posix" else "cls")

def print_line(char="-", width=40):
    print(char * int(width))

def say_color(text, color="white"):
    colors = {
        "red":"\033[91m","green":"\033[92m","yellow":"\033[93m",
        "blue":"\033[94m","purple":"\033[95m","cyan":"\033[96m",
        "white":"\033[97m","bold":"\033[1m","dim":"\033[2m"
    }
    print(f"{colors.get(color,'')}{text}\033[0m")

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
def isbox(x):        return isinstance(x, dict)
def parse_int(x):    return int(x)
def parse_float(x):  return float(x)
def is_empty(x):     return len(x) == 0 if hasattr(x, '__len__') else x is None

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
def sign(n):         return 1 if n > 0 else (-1 if n < 0 else 0)
def is_between(v,a,b): return a <= v <= b
def percent(part, whole): return (part / whole) * 100
def format_num(n):   return f"{n:,}"
def to_bin(n):       return bin(int(n))[2:]
def to_hex(n):       return hex(int(n))[2:].upper()
def log(x):          return __math__.log(x)
def log10(x):        return __math__.log10(x)
def sin(x):          return __math__.sin(x)
def cos(x):          return __math__.cos(x)
def tan(x):          return __math__.tan(x)

# ── Random ────────────────────────────────────────────────
def chance():        return __random__.random()
def dice(a, b):      return __random__.randint(int(a), int(b))
def pick(lst):       return __random__.choice(lst)
def shuffle(lst):    __random__.shuffle(lst)
def sample(lst, n):  return __random__.sample(lst, int(n))

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
def cap(s):          return str(s).capitalize()
def title_case(s):   return str(s).title()
def count_char(s,c): return str(s).count(c)
def remove_spaces(s): return str(s).replace(' ','')
def is_upper(s):     return str(s).isupper()
def is_lower(s):     return str(s).islower()
def is_alpha(s):     return str(s).isalpha()
def is_digit_str(s): return str(s).isdigit()
def strip_left(s):   return str(s).lstrip()
def strip_right(s):  return str(s).rstrip()
def find_in(s,sub):  return str(s).find(sub)
def slice_str(s,a,b): return str(s)[int(a):int(b)]

# ── Lists ─────────────────────────────────────────────────
def add(lst, item):  lst.append(item)
def cut(lst, item):  lst.remove(item)
def ind(lst, item):  return lst.index(item)
def __gpp_del__(lst): return lst.pop()
def cler(lst):       lst.clear()
def sort(lst,r=False): return sorted(lst, reverse=bool(r))
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
def range_list(a,b=None,step=1):
    if b is None: return list(range(int(a)))
    return list(range(int(a),int(b),int(step)))
def fill(val,n):     return [val]*int(n)
def take(lst,n):     return lst[:int(n)]
def skip_items(lst,n): return lst[int(n):]
def chunk(lst,n):
    n=int(n)
    return [lst[i:i+n] for i in range(0,len(lst),n)]
def without(lst,val): return [x for x in lst if x != val]
def any_true(lst):   return any(lst)
def all_true(lst):   return all(lst)
def count_if_true(lst): return sum(1 for x in lst if x)
def nums_only(lst):  return [x for x in lst if isinstance(x,(int,float))]
def texts_only(lst): return [x for x in lst if isinstance(x,str)]

# ── Box (Dictionary) ──────────────────────────────────────
def box():           return {}
def put(d,k,v):      d[k]=v; return d
def get_val(d,k,dft=None): return d.get(k,dft)
def drop_key(d,k):
    if k in d: del d[k]
def has_key(d,k):    return k in d
def keys_of(d):      return list(d.keys())
def vals_of(d):      return list(d.values())
def pairs_of(d):     return list(d.items())
def box_size(d):     return len(d)
def merge_boxes(a,b): return {**a,**b}

# ── JSON ──────────────────────────────────────────────────
def to_json(x):      return __json__.dumps(x, indent=2)
def from_json(s):    return __json__.loads(s)
def to_json_line(x): return __json__.dumps(x)

# ── Utility / Time ────────────────────────────────────────
def wait(ms):        __time__.sleep(ms/1000)
def now():
    import datetime
    return str(datetime.datetime.now().strftime("%H:%M:%S"))
def today():
    import datetime
    return str(datetime.date.today())
def timestamp():
    return int(__time__.time())
def time_ms():
    return int(__time__.time()*1000)

# ── File I/O ──────────────────────────────────────────────
def read_file(path):
    with open(path,'r',encoding='utf-8') as f: return f.read()
def write_file(path,text):
    with open(path,'w',encoding='utf-8') as f: f.write(text)
def append_file(path,text):
    with open(path,'a',encoding='utf-8') as f: f.write(text)
def file_exists(path): return __os__.path.exists(path)
def read_lines(path):
    with open(path,'r',encoding='utf-8') as f: return [l.rstrip('\\n') for l in f]

# ── Constants ─────────────────────────────────────────────
TAR  = True
FYU  = False
PI   = __math__.pi
E    = __math__.e
NULL = None
INF  = float('inf')
TAU  = __math__.tau

# ═════════════════════════════════════════════════════════
'''

# ─────────────────────────────────────────────────────────
#  String-span helpers (skip inside quotes)
# ─────────────────────────────────────────────────────────

def _string_spans(line):
    spans, i, n = [], 0, len(line)
    while i < n:
        if line[i] in ('"', "'"):
            q, j = line[i], i+1
            while j < n:
                if line[j] == '\\': j += 2; continue
                if line[j] == q:
                    spans.append((i, j+1)); i = j+1; break
                j += 1
            else: i = j
        else: i += 1
    return spans

def in_string(pos, spans):
    return any(s <= pos < e for s, e in spans)

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

# ─────────────────────────────────────────────────────────
#  Line Transformer
# ─────────────────────────────────────────────────────────

def transform_line(line):
    stripped = line.lstrip()
    indent   = line[:len(line) - len(stripped)]
    if not stripped or stripped.startswith('#'):
        return line

    c = stripped

    # Structure keywords
    c = re.sub(r'^fuc\b',         'def',   c)
    c = re.sub(r'^con\s+loop\b',  'for',   c)
    c = re.sub(r'^won\s+loop\b',  'while', c)

    # Declarations
    c = re.sub(r'^make\s+(?:int|str|f(?:loat)?|bool)\s+(\w)', r'\1', c)
    c = re.sub(r'^make\s+box\s+(\w+)\s*=\s*', r'\1 = ', c)
    c = re.sub(r'^make\s+box\s+(\w+)\s*$', r'\1 = {}', c)
    c = re.sub(r'^make\s+', '', c)
    c = re.sub(r'^set\s+(\w+)\s*=', r'\1 =', c)

    # Flow control — handles both start-of-statement AND inline (after colon)
    c = re.sub(r'^rt\b',   'return',   c)
    c = re.sub(r'^stop\b', 'break',    c)
    c = re.sub(r'^skip\b', 'continue', c)
    # Also handle inline: if cond: rt ...
    c = safe_re_sub(r'(?<=:\s)rt\b',   'return',   c)
    c = safe_re_sub(r'(?<=:\s)stop\b', 'break',    c)
    c = safe_re_sub(r'(?<=:\s)skip\b', 'continue', c)
    c = safe_re_sub(r'(?<=:)rt\b',     'return',   c)
    c = safe_re_sub(r'(?<=:)stop\b',   'break',    c)
    c = safe_re_sub(r'(?<=:)skip\b',   'continue', c)

    # Built-in renames
    c = safe_re_sub(r'\bdel\s*\(', '__gpp_del__(', c)
    c = safe_re_sub(r'(?<!\w)f\(', 'float(', c)

    # Literals & constants
    c = safe_re_sub(r'\bTAR\b',  'True',         c)
    c = safe_re_sub(r'\bFYU\b',  'False',        c)
    c = safe_re_sub(r'\bNULL\b', 'None',         c)
    c = safe_re_sub(r'\bINF\b',  "float('inf')", c)
    c = safe_re_sub(r'\bPI\b',   '__math__.pi',  c)
    c = safe_re_sub(r'\bE\b',    '__math__.e',   c)
    c = safe_re_sub(r'\bTAU\b',  '__math__.tau', c)

    # Operators
    c = safe_re_sub(r'\^',              '**',  c)
    c = safe_re_sub(r'(?<=\s)&(?=\s)',  'and', c)
    c = safe_re_sub(r'(?<=\s)\|(?=\s)', 'or',  c)
    c = safe_re_sub(r'(?<![=!<>])!(?!=)', 'not ', c)

    return indent + c

# ─────────────────────────────────────────────────────────
#  Transpiler
# ─────────────────────────────────────────────────────────

RUNTIME_LINES = len(RUNTIME.splitlines()) + 1

def transpile(source):
    output = [RUNTIME]
    for raw in source.splitlines():
        try:    output.append(transform_line(raw))
        except: output.append(raw)
    return '\n'.join(output)

def format_error(stderr_text, source_lines):
    lines  = stderr_text.strip().splitlines()
    output = [f"\n{RED}{BOLD}  ✗  G++ Error{RESET}\n"]
    shown  = False

    for line in lines:
        if any(x in line for x in ['__gpp','Traceback','_gpp_',
                                    'gpp_','tempfile','subprocess']): continue
        m = re.search(r'line (\d+)', line)
        if m:
            adjusted = max(1, int(m.group(1)) - RUNTIME_LINES)
            line = line[:m.start()] + f'line {adjusted}' + line[m.end():]
            # Show the offending source line
            if 0 < adjusted <= len(source_lines) and not shown:
                src = source_lines[adjusted - 1]
                output.append(f"\n  {CYAN}Line {adjusted}:{RESET}  {WHITE}{src.strip()}{RESET}")
                output.append(f"  {RED}{'~' * max(len(src.strip()), 5)}{RESET}")
                shown = True
        if line.strip():
            output.append(f"  {DIM}{line}{RESET}")

    output.append("")
    return '\n'.join(output)

# ─────────────────────────────────────────────────────────
#  Auto-find .G++ file
# ─────────────────────────────────────────────────────────

def find_gpp_file(start_dir=None):
    """Find a .G++ file: current dir, then search subdirs."""
    if start_dir is None:
        start_dir = os.getcwd()

    # Current directory first
    matches = glob.glob(os.path.join(start_dir, '*.G++')) + \
              glob.glob(os.path.join(start_dir, '*.g++'))
    if matches:
        return sorted(matches)[0]

    # Walk subdirectories (max 2 levels)
    for root, dirs, files in os.walk(start_dir):
        depth = root[len(start_dir):].count(os.sep)
        if depth >= 2:
            dirs.clear()
            continue
        for f in files:
            if f.endswith('.G++') or f.endswith('.g++'):
                return os.path.join(root, f)
    return None

# ─────────────────────────────────────────────────────────
#  Runner
# ─────────────────────────────────────────────────────────

def run_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            source = f.read()
    except FileNotFoundError:
        print(f"  {RED}✗  File not found:{RESET} {path}"); sys.exit(1)
    except Exception as e:
        print(f"  {RED}✗  Cannot read file:{RESET} {e}"); sys.exit(1)

    source_lines = source.splitlines()
    python_src   = transpile(source)
    tmp_fd, tmp_path = tempfile.mkstemp(suffix='.py', prefix='gpp_')
    try:
        with os.fdopen(tmp_fd, 'w', encoding='utf-8') as tf:
            tf.write(python_src)
        proc = subprocess.run(
            [sys.executable, tmp_path],
            stderr=subprocess.PIPE, text=True
        )
        if proc.returncode != 0:
            print(format_error(proc.stderr, source_lines))
        return proc.returncode
    except Exception as e:
        print(f"  {RED}✗  Internal error:{RESET} {e}"); return 1
    finally:
        try: os.unlink(tmp_path)
        except: pass

# ─────────────────────────────────────────────────────────
#  Help
# ─────────────────────────────────────────────────────────

HELP_TEXT = f"""
{CYAN}{BOLD}  G++ Language v{VERSION}  —  Quick Reference{RESET}

{WHITE}{BOLD}  USAGE{RESET}
    {CYAN}G++{RESET}              → auto-find & run .G++ file here
    {CYAN}G++ file.G++{RESET}     → run a specific file
    {CYAN}G++ --help{RESET}       → show this help

{WHITE}{BOLD}  VARIABLES{RESET}
    {YELLOW}make name = "Alex"{RESET}
    {YELLOW}make int age = 18{RESET}
    {YELLOW}make f score = 9.5{RESET}
    {YELLOW}make box data = {{}}{RESET}       ← dictionary

{WHITE}{BOLD}  OUTPUT / INPUT{RESET}
    {GREEN}say("Hello!", name){RESET}
    {GREEN}say_color("Warning!", "red"){RESET}
    {GREEN}make answer = ask("Your name? "){RESET}

{WHITE}{BOLD}  CONDITIONALS{RESET}
    {BLUE}if score >= 90:{RESET}
        say("A")
    {BLUE}elif score >= 80:{RESET}
        say("B")
    {BLUE}else:{RESET}
        say("F")

{WHITE}{BOLD}  LOOPS{RESET}
    {BLUE}con loop i in range(5):{RESET}     ← for loop
        say(i)
    {BLUE}won loop x < 10:{RESET}            ← while loop
        x = x + 1

{WHITE}{BOLD}  FUNCTIONS{RESET}
    {BLUE}fuc greet(name):{RESET}
        say("Hello,", name)
    {BLUE}fuc add(a, b):{RESET}
        rt a + b

{WHITE}{BOLD}  LISTS{RESET}
    {PURPLE}set nums = [1, 2, 3]{RESET}
    {PURPLE}add(nums, 4)  cut(nums, 2)  ind(nums, 3){RESET}

{WHITE}{BOLD}  BOX (Dictionary){RESET}
    {PURPLE}make box info = {{}}{RESET}
    {PURPLE}put(info, "name", "Alex"){RESET}
    {PURPLE}get_val(info, "name"){RESET}

{WHITE}{BOLD}  OPERATORS{RESET}
    {DIM}+ - * /   x ^ y (power)   x % y (mod){RESET}
    {DIM}& (and)   | (or)   ! (not){RESET}

{DIM}  Docs: https://github.com/gabrieltodua/gpp{RESET}
"""

# ─────────────────────────────────────────────────────────
#  Main
# ─────────────────────────────────────────────────────────

def main():
    print_banner()

    args = sys.argv[1:]

    # Help flag
    if not args or args[0] in ('--help', '-h', 'help'):
        if not args:
            # Try auto-find
            path = find_gpp_file()
            if path:
                pass  # fall through to run it
            else:
                print(HELP_TEXT)
                sys.exit(0)
        else:
            print(HELP_TEXT)
            sys.exit(0)

    # Version flag
    if args[0] in ('--version', '-v'):
        print(f"  G++ Language v{VERSION}\n")
        sys.exit(0)

    # Resolve path
    if args:
        path = args[0]
        if not os.path.isabs(path):
            path = os.path.join(os.getcwd(), path)
    else:
        path = find_gpp_file()
        if not path:
            print(f"  {YELLOW}⚠  No .G++ file found in this folder.{RESET}")
            print(f"  {DIM}Create a file ending in .G++ and run G++ again.{RESET}\n")
            sys.exit(0)

    # Check file exists — search subdirs if needed
    if not os.path.isfile(path):
        # Try searching from the given base name
        base = os.path.basename(path)
        found = None
        for root, _, files in os.walk(os.getcwd()):
            depth = root[len(os.getcwd()):].count(os.sep)
            if depth > 4: continue
            for f in files:
                if f == base or f == base + '.G++':
                    found = os.path.join(root, f)
                    break
            if found: break
        if found:
            path = found
        else:
            print(f"  {RED}✗  File not found:{RESET} {path}")
            print(f"  {DIM}Searched from: {os.getcwd()}{RESET}\n")
            sys.exit(1)

    if os.path.splitext(path)[1] not in ('.G++', '.g++'):
        print(f"  {YELLOW}⚠  Warning: file doesn't end in .G++{RESET}\n")

    print(f"  {CYAN}File  {RESET}  {BOLD}{os.path.basename(path)}{RESET}")
    print(f"  {CYAN}Path  {RESET}  {DIM}{os.path.dirname(path)}{RESET}")
    print(f"  {DIM}{'─' * 38}{RESET}\n")

    rc = run_file(path)

    print(f"\n  {DIM}{'─' * 38}{RESET}")
    if rc == 0:
        print(f"  {GREEN}{BOLD}✓  Done — no errors{RESET}\n")
    else:
        print(f"  {RED}✗  Exited with error code {rc}{RESET}\n")
    sys.exit(rc)

if __name__ == '__main__':
    main()

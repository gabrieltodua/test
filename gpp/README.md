# G++ Programming Language — v2.0

A clean, beginner-friendly language that runs `.G++` files from your terminal.

---

## One-Line Install (macOS / Linux)

Open your terminal and run:

```bash
curl -fsSL https://raw.githubusercontent.com/USERNAME/REPO/main/install.sh | bash
```

> Replace `USERNAME/REPO` with your actual GitHub username and repo name.

That's it. The `gpp` command will be available everywhere after install.

---

## Running Programs

```bash
gpp main.G++
gpp ~/projects/myprogram.G++
gpp /any/path/to/file.G++
```

Works from **any folder** — no need to be in a specific directory.

---

## Syntax Quick Reference

### Variables
```
make name = "Alex"
make int age = 18
make f height = 5.9
make str city = "NYC"
```

### Output & Input
```
say("Hello!")
say("Name:", name, "Age:", age)
make answer = ask("What is your name? ")
```

### If / Elif / Else
```
if score >= 90:
    say("A")
elif score >= 80:
    say("B")
else:
    say("F")
```

### Loops
```
# con loop = for loop
con loop i in range(5):
    say(i)

# won loop = while loop
make int x = 0
won loop x < 10:
    say(x)
    x = x + 1
```

### Functions
```
fuc greet(name):
    say("Hello,", name)

fuc add(a, b):
    rt a + b

greet("World")
make result = add(3, 4)
```

### Lists
```
set fruits = ["apple", "banana"]
add(fruits, "mango")
cut(fruits, "banana")
say(ind(fruits, "apple"))
```

### Booleans & Constants
```
make isOn = TAR      # True
make isDone = FYU    # False
make nothing = NULL  # None
say(PI)              # 3.14159...
say(E)               # 2.71828...
```

### Operators
```
x + y    x - y    x * y    x / y
x ^ y    # power (exponent)
x % y    # remainder (modulo)
x == y   x != y   x > y   x < y
x & y    # and
x | y    # or
! x      # not
```

### Break & Continue
```
con loop i in range(10):
    if i == 3: skip   # skip = continue
    if i == 7: stop   # stop = break
    say(i)
```

---

## All Built-in Functions

### Output
| Function | What it does |
|---|---|
| `say(...)` | Print to terminal |
| `ask("prompt")` | Get input from user |
| `clear_screen()` | Clear the terminal |

### Math
| Function | What it does |
|---|---|
| `sig(x)` | Length of string or list |
| `pa(x)` | Minimum value |
| `di(x)` | Maximum value |
| `abso(x)` | Absolute value |
| `sqrt(x)` | Square root |
| `floor(x)` | Round DOWN |
| `ceil(x)` | Round UP |
| `rnd(x, n)` | Round to N decimal places |
| `avg(list)` | Average of a list |
| `total(list)` | Sum of a list |
| `clamp(v, lo, hi)` | Keep value between min and max |
| `even(n)` | Is the number even? |
| `odd(n)` | Is the number odd? |
| `pow_of(base, exp)` | Power |

### Random
| Function | What it does |
|---|---|
| `chance()` | Random float 0.0–1.0 |
| `dice(a, b)` | Random integer between a and b |
| `pick(list)` | Pick a random item from a list |
| `shuffle(list)` | Shuffle a list randomly |

### Strings
| Function | What it does |
|---|---|
| `upper(s)` | UPPERCASE |
| `lower(s)` | lowercase |
| `trim(s)` | Remove leading/trailing spaces |
| `split(s, sep)` | Split into list |
| `join(sep, list)` | Join list into string |
| `replace(s, old, new)` | Replace text |
| `has(s, item)` | Does it contain item? |
| `startswith(s, p)` | Does it start with p? |
| `endswith(s, p)` | Does it end with p? |
| `repeat(s, n)` | Repeat n times |
| `flip(s)` | Reverse the string |
| `chars(s)` | Split into list of characters |
| `numwords(s)` | Count words |
| `pad(s, w)` | Center in width |
| `padleft(s, w)` | Right-align in width |
| `padright(s, w)` | Left-align in width |
| `cut_str(s, a, b)` | Slice characters a to b |

### Lists
| Function | What it does |
|---|---|
| `add(list, item)` | Add to end |
| `cut(list, item)` | Remove first match |
| `ind(list, item)` | Find index/position |
| `del(list)` | Remove and return last item |
| `cler(list)` | Clear everything |
| `sort(list)` | Sort ascending. `sort(list, TAR)` = descending |
| `rev(list)` | Reverse in place |
| `copy(list)` | Make a copy |
| `howmany(list, item)` | Count occurrences |
| `first(list)` | Get first item |
| `last(list)` | Get last item |
| `unique(list)` | Remove duplicates |
| `merge(a, b)` | Combine two lists |
| `insert(list, i, item)` | Insert at position i |
| `flat(list)` | Flatten nested list |
| `zip_lists(a, b)` | Combine into pairs |

### Types
| Function | What it does |
|---|---|
| `rank(x)` | Get type name |
| `tonum(x)` | Convert to number |
| `totext(x)` | Convert to string |
| `tolist(x)` | Convert to list |
| `isnull(x)` | Is it NULL? |
| `isnum(x)` | Is it a number? |
| `istext(x)` | Is it a string? |
| `islist(x)` | Is it a list? |

### Time
| Function | What it does |
|---|---|
| `wait(ms)` | Pause. 1000 = 1 second |
| `now()` | Current time as string |
| `today()` | Today's date as string |

---

## File Structure (GitHub repo)

```
repo/
├── gpp.py                              ← Interpreter
├── install.sh                          ← Installer
├── README.md                           ← This file
├── example/
│   └── main.G++                        ← Demo program
└── vscode-gpp/                         ← VS Code extension
    ├── package.json
    ├── language-configuration.json
    ├── icons/
    │   └── gpp_icon.png
    ├── snippets/
    │   └── gpp.json
    └── syntaxes/
        └── gpp.tmLanguage.json
```

---

## VS Code Color Guide

| Color | What it highlights |
|---|---|
| Blue | Keywords: `make`, `fuc`, `if`, `rt`, `stop`... |
| Cyan | Output: `say`, `ask`, `clear_screen` |
| Green | Math: `sqrt`, `avg`, `dice`, `floor`... |
| Yellow | String functions: `upper`, `trim`, `split`... |
| Purple | List functions: `add`, `sort`, `unique`... |
| Orange | String values: `"hello"` |
| Teal | Boolean/constants: `TAR`, `FYU`, `PI`, `E` |
| Gray | Comments: `# note` |
| White | Numbers: `42`, `3.14` |

---

## Uninstall

```bash
rm -rf ~/.gpp
rm -rf ~/.vscode/extensions/gpp-language-1.0.0
sudo rm -f /usr/local/bin/gpp
```

---

*G++ Language v2.0 — Built for everyone.*

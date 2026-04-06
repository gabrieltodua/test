# G++ Programming Language — v3.0

A clean, beginner-friendly language. Write `.G++` files, run them anywhere.

---

## Install (macOS / Linux)

```bash
curl -fsSL https://raw.githubusercontent.com/gabrieltodua/test/main/gpp/install.sh | bash
```

Installs: `G++` command, `gpp` command, VS Code extension (run button + error highlighting).

---

## Run Programs

```bash
G++                        # auto-finds .G++ file in this folder
G++ main.G++               # run specific file
G++ ~/projects/app.G++     # run from anywhere
G++ --help                 # show help
```

**In VS Code:** open a `.G++` file → click ▶ in top-right corner (or press `F5`).

---

## Syntax

### Variables
```
make name   = "Alex"
make int age = 20
make f score = 9.5
make box data = {}        # dictionary
set nums = [1, 2, 3]      # list
```

### Output & Input
```
say("Hello!")
say("Name:", name, "Score:", score)
say_color("Error!", "red")         # colored output
make answer = ask("Your name? ")
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
con loop i in range(5):        # for loop
    say(i)

won loop x < 10:               # while loop
    x = x + 1

con loop item in myList:       # loop over list
    say(item)
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
say(sort(fruits))
say(pick(fruits))              # random item
say(chunk(fruits, 2))          # split into groups
```

### Box (Dictionary) — NEW in v3
```
make box player = {}
put(player, "name", "Alex")
put(player, "score", 100)
say(get_val(player, "name"))
say(keys_of(player))
say(has_key(player, "score"))
```

### JSON — NEW in v3
```
make txt = to_json(player)
say(txt)
make loaded = from_json(txt)
```

### File I/O — NEW in v3
```
write_file("log.txt", "Hello!")
make txt = read_file("log.txt")
make lines = read_lines("data.txt")
if file_exists("data.txt"):
    say("Found!")
```

### Booleans & Constants
```
TAR    # True
FYU    # False
NULL   # None
PI     # 3.14159...
E      # 2.71828...
INF    # infinity
TAU    # 6.28318...
```

### Operators
```
x + y   x - y   x * y   x / y
x ^ y   # power       x % y  # modulo
x == y  x != y  x > y  x < y
x & y   # and         x | y  # or
! x     # not
```

### Colors
```
say_color("text", "red")
say_color("text", "green")
say_color("text", "yellow")
say_color("text", "blue")
say_color("text", "purple")
say_color("text", "cyan")
```

---

## All Built-in Functions

### Output
| Function | What it does |
|---|---|
| `say(...)` | Print to terminal |
| `ask("prompt")` | Get user input |
| `say_color(text, color)` | Print colored text |
| `print_line(char, width)` | Print separator line |
| `clear_screen()` | Clear terminal |

### Math
| Function | What it does |
|---|---|
| `sqrt(x)` | Square root |
| `floor(x)` | Round down |
| `ceil(x)` | Round up |
| `rnd(x, n)` | Round to N decimals |
| `abso(x)` | Absolute value |
| `avg(list)` | Average |
| `total(list)` | Sum |
| `clamp(v, lo, hi)` | Keep in range |
| `pow_of(b, e)` | Power |
| `even(n)` / `odd(n)` | Even/odd check |
| `sign(n)` | 1, -1, or 0 |
| `percent(part, whole)` | Percentage |
| `format_num(n)` | Format with commas |
| `to_bin(n)` / `to_hex(n)` | Convert base |
| `sig(x)` | Length |
| `pa(...)` / `di(...)` | Min / Max |
| `parse_int(x)` | To integer |
| `parse_float(x)` | To decimal |
| `sin(x)` / `cos(x)` / `tan(x)` | Trig |

### Random
| Function | What it does |
|---|---|
| `chance()` | Random 0.0–1.0 |
| `dice(a, b)` | Random integer a–b |
| `pick(list)` | Random item |
| `shuffle(list)` | Shuffle in place |
| `sample(list, n)` | Pick N random items |

### Strings
| Function | What it does |
|---|---|
| `upper(s)` / `lower(s)` | Case conversion |
| `trim(s)` | Remove whitespace |
| `cap(s)` | Capitalize first letter |
| `title_case(s)` | Title Case |
| `split(s, sep)` | Split to list |
| `join(sep, list)` | Join list to string |
| `replace(s, old, new)` | Replace text |
| `has(s, item)` | Contains? |
| `startswith(s, p)` | Starts with? |
| `endswith(s, p)` | Ends with? |
| `repeat(s, n)` | Repeat string |
| `flip(s)` | Reverse |
| `chars(s)` | Split to char list |
| `numwords(s)` | Word count |
| `count_char(s, c)` | Count character |
| `find_in(s, sub)` | Find substring index |
| `is_upper(s)` / `is_lower(s)` | Case check |
| `is_alpha(s)` / `is_digit_str(s)` | Content check |
| `pad/padleft/padright` | Alignment |
| `cut_str(s, a, b)` | Slice |

### Lists
| Function | What it does |
|---|---|
| `add(list, item)` | Append |
| `cut(list, item)` | Remove |
| `ind(list, item)` | Index of |
| `del(list)` | Pop last |
| `sort(list, TAR?)` | Sort |
| `rev(list)` | Reverse in place |
| `copy(list)` | Copy |
| `unique(list)` | Remove duplicates |
| `merge(a, b)` | Combine |
| `first(list)` / `last(list)` | First/last item |
| `flat(list)` | Flatten |
| `howmany(list, item)` | Count occurrences |
| `insert(list, i, item)` | Insert at index |
| `fill(val, n)` | Create filled list |
| `take(list, n)` | First N items |
| `chunk(list, n)` | Split into groups |
| `without(list, val)` | Remove all |
| `range_list(a, b, step?)` | Number range as list |
| `zip_lists(a, b)` | Pair two lists |
| `any_true(list)` | Any item truthy? |
| `all_true(list)` | All items truthy? |

### Box (Dictionary)
| Function | What it does |
|---|---|
| `box()` | Create empty box |
| `put(box, key, val)` | Set value |
| `get_val(box, key)` | Get value |
| `drop_key(box, key)` | Delete key |
| `has_key(box, key)` | Key exists? |
| `keys_of(box)` | All keys |
| `vals_of(box)` | All values |
| `pairs_of(box)` | All key-value pairs |
| `merge_boxes(a, b)` | Combine two boxes |

### JSON
| Function | What it does |
|---|---|
| `to_json(x)` | Convert to JSON string |
| `from_json(s)` | Parse JSON string |

### Types
| Function | What it does |
|---|---|
| `rank(x)` | Type name |
| `tonum(x)` / `totext(x)` / `tolist(x)` | Convert type |
| `isnull/isnum/istext/islist/isbox` | Type check |
| `is_empty(x)` | Empty check |

### Time
| Function | What it does |
|---|---|
| `wait(ms)` | Pause (1000 = 1s) |
| `now()` | Current time string |
| `today()` | Today's date string |
| `timestamp()` | Unix timestamp |

### File I/O
| Function | What it does |
|---|---|
| `read_file(path)` | Read file as string |
| `write_file(path, text)` | Write to file |
| `append_file(path, text)` | Add to file |
| `read_lines(path)` | Read as list of lines |
| `file_exists(path)` | Check if file exists |

---

## VS Code Color Guide

| Color | What it highlights |
|---|---|
| Blue | Keywords: `make`, `fuc`, `if`, `rt`, `stop` |
| Cyan | Output: `say`, `ask`, `clear_screen`, `say_color` |
| Green | Math: `sqrt`, `avg`, `dice`, `floor`, `sign` |
| Yellow | Strings: `upper`, `trim`, `split`, `cap` |
| Purple | Lists + Box: `add`, `sort`, `put`, `get_val` |
| Orange | String literals: `"hello"` |
| Teal | Constants: `TAR`, `FYU`, `PI`, `NULL`, `INF` |
| Gray | Comments: `# note` |
| White | Numbers: `42`, `3.14` |

---

## Uninstall

```bash
rm -rf ~/.gpp
rm -rf ~/.vscode/extensions/gpp-language-3.0.0
sudo rm -f /usr/local/bin/gpp /usr/local/bin/G++
```

---

*G++ Language v3.0 — Built for everyone.*

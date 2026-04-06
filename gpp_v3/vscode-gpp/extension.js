// G++ VS Code Extension — extension.js
// Provides: ▶ Run button, red-underline errors, hover docs, auto-complete
"use strict";

const vscode = require("vscode");
const path   = require("path");
const fs     = require("fs");
const os     = require("os");

// ─────────────────────────────────────────────────────────
//  Function documentation (hover + autocomplete)
// ─────────────────────────────────────────────────────────

const DOCS = {
  // Output
  say:          { sig:"say(...values)",              desc:"Print values to the terminal.",                       ex:'say("Hello, World!")\nsay("Score:", 42, "pts")' },
  ask:          { sig:"ask(prompt)",                 desc:"Ask the user to type something. Returns their input.",ex:'make name = ask("Your name? ")\nsay("Hi,", name)' },
  clear_screen: { sig:"clear_screen()",              desc:"Clear all text from the terminal.",                  ex:'clear_screen()' },
  say_color:    { sig:'say_color(text, color)',       desc:'Print colored text. Colors: "red","green","yellow","blue","purple","cyan".',ex:'say_color("Error!", "red")\nsay_color("Done!", "green")' },
  print_line:   { sig:"print_line(char, width)",     desc:"Print a separator line.",                            ex:'print_line("-", 30)\nprint_line("=")' },

  // Math
  sqrt:     { sig:"sqrt(x)",          desc:"Square root of a number.",           ex:"say(sqrt(16))   # → 4.0" },
  floor:    { sig:"floor(x)",         desc:"Round DOWN to nearest integer.",      ex:"say(floor(3.9)) # → 3" },
  ceil:     { sig:"ceil(x)",          desc:"Round UP to nearest integer.",        ex:"say(ceil(3.1))  # → 4" },
  rnd:      { sig:"rnd(x, decimals)", desc:"Round to N decimal places.",          ex:"say(rnd(3.14159, 2)) # → 3.14" },
  abso:     { sig:"abso(x)",          desc:"Absolute (positive) value.",          ex:"say(abso(-5))   # → 5" },
  avg:      { sig:"avg(list)",        desc:"Average of all numbers in a list.",   ex:"say(avg([10, 20, 30])) # → 20.0" },
  total:    { sig:"total(list)",      desc:"Sum of all numbers in a list.",       ex:"say(total([1,2,3,4])) # → 10" },
  clamp:    { sig:"clamp(v, lo, hi)", desc:"Keep a value between min and max.",   ex:"say(clamp(150, 0, 100)) # → 100" },
  pow_of:   { sig:"pow_of(base, exp)",desc:"Raise base to the power of exp.",     ex:"say(pow_of(2, 10)) # → 1024" },
  even:     { sig:"even(n)",          desc:"Is the number even? Returns TAR/FYU.",ex:"say(even(4)) # → True" },
  odd:      { sig:"odd(n)",           desc:"Is the number odd? Returns TAR/FYU.", ex:"say(odd(7))  # → True" },
  sign:     { sig:"sign(n)",          desc:"Returns 1, -1, or 0 for the number's sign.", ex:"say(sign(-5)) # → -1" },
  percent:  { sig:"percent(part, whole)", desc:"Calculate percentage.",           ex:"say(percent(25, 200)) # → 12.5" },
  format_num:{ sig:"format_num(n)",   desc:"Format number with commas.",          ex:'say(format_num(1000000)) # → "1,000,000"' },
  sig:      { sig:"sig(x)",           desc:"Length of a string or list.",         ex:"say(sig(\"hello\"))  # → 5\nsay(sig([1,2,3]))   # → 3" },
  pa:       { sig:"pa(list_or_a, b)", desc:"Minimum value.",                      ex:"say(pa([5,2,8])) # → 2" },
  di:       { sig:"di(list_or_a, b)", desc:"Maximum value.",                      ex:"say(di([5,2,8])) # → 8" },
  parse_int:  { sig:"parse_int(x)",   desc:"Convert to integer (whole number).",  ex:"say(parse_int(\"42\")) # → 42" },
  parse_float:{ sig:"parse_float(x)", desc:"Convert to decimal number.",          ex:'say(parse_float("3.14")) # → 3.14' },

  // Random
  chance:   { sig:"chance()",         desc:"Random decimal between 0.0 and 1.0.",ex:"say(chance()) # → 0.734..." },
  dice:     { sig:"dice(a, b)",        desc:"Random whole number between a and b.",ex:"say(dice(1, 6)) # → 1 to 6" },
  pick:     { sig:"pick(list)",        desc:"Pick a random item from a list.",    ex:'say(pick(["red","blue","green"]))' },
  shuffle:  { sig:"shuffle(list)",     desc:"Randomly shuffle a list in place.",  ex:"shuffle(myList)\nsay(myList)" },
  sample:   { sig:"sample(list, n)",   desc:"Pick N random items from a list.",   ex:"say(sample([1,2,3,4,5], 3))" },

  // Strings
  upper:      { sig:"upper(s)",          desc:"Convert to UPPERCASE.",            ex:'say(upper("hello")) # → "HELLO"' },
  lower:      { sig:"lower(s)",          desc:"Convert to lowercase.",            ex:'say(lower("HELLO")) # → "hello"' },
  trim:       { sig:"trim(s)",           desc:"Remove spaces from both ends.",    ex:'say(trim("  hi  ")) # → "hi"' },
  split:      { sig:'split(s, sep=" ")', desc:"Split string into a list.",        ex:'say(split("a,b,c", ",")) # → ["a","b","c"]' },
  join:       { sig:"join(sep, list)",   desc:"Join list items into a string.",   ex:'say(join(", ", ["a","b","c"])) # → "a, b, c"' },
  replace:    { sig:"replace(s, old, new)", desc:"Replace all occurrences.",      ex:'say(replace("hi ho", "ho", "hey")) # → "hi hey"' },
  has:        { sig:"has(s, item)",      desc:"Check if string/list contains item.",ex:'say(has("hello", "ell")) # → True' },
  flip:       { sig:"flip(s)",           desc:"Reverse a string.",                ex:'say(flip("hello")) # → "olleh"' },
  cap:        { sig:"cap(s)",            desc:"Capitalize first letter.",          ex:'say(cap("hello world")) # → "Hello world"' },
  title_case: { sig:"title_case(s)",     desc:"Title Case every word.",           ex:'say(title_case("hello world")) # → "Hello World"' },
  repeat:     { sig:"repeat(s, n)",      desc:"Repeat a string N times.",         ex:'say(repeat("ha", 3)) # → "hahaha"' },
  chars:      { sig:"chars(s)",          desc:"Split string into list of characters.", ex:'say(chars("abc")) # → ["a","b","c"]' },
  count_char: { sig:"count_char(s, c)",  desc:"Count how many times a char appears.", ex:'say(count_char("hello", "l")) # → 2' },
  numwords:   { sig:"numwords(s)",        desc:"Count the words in a string.",    ex:'say(numwords("one two three")) # → 3' },
  is_upper:   { sig:"is_upper(s)",       desc:"Is the string all uppercase?",     ex:'say(is_upper("HELLO")) # → True' },
  is_lower:   { sig:"is_lower(s)",       desc:"Is the string all lowercase?",     ex:'say(is_lower("hello")) # → True' },
  is_alpha:   { sig:"is_alpha(s)",       desc:"Contains only letters?",           ex:'say(is_alpha("abc")) # → True' },
  find_in:    { sig:"find_in(s, sub)",   desc:"Find index of substring (-1 if not found).", ex:'say(find_in("hello", "ll")) # → 2' },
  startswith: { sig:"startswith(s, p)",  desc:"Does string start with prefix?",   ex:'say(startswith("hello", "he")) # → True' },
  endswith:   { sig:"endswith(s, p)",    desc:"Does string end with suffix?",      ex:'say(endswith("hello", "lo")) # → True' },
  pad:        { sig:"pad(s, width)",     desc:"Center string in given width.",     ex:'say(pad("hi", 10)) # → "    hi    "' },
  padleft:    { sig:"padleft(s, width)", desc:"Right-align string in given width.",ex:'say(padleft("5", 4)) # → "   5"' },
  padright:   { sig:"padright(s, width)",desc:"Left-align string in given width.", ex:'say(padright("hi", 6)) # → "hi    "' },

  // Lists
  add:      { sig:"add(list, item)",       desc:"Add item to end of list.",        ex:"add(fruits, \"mango\")\nsay(fruits)" },
  cut:      { sig:"cut(list, item)",       desc:"Remove first matching item.",      ex:"cut(nums, 5)" },
  ind:      { sig:"ind(list, item)",       desc:"Get index/position of item.",      ex:'say(ind(["a","b","c"], "b")) # → 1' },
  sort:     { sig:"sort(list, reverse?)", desc:"Return sorted list. sort(l,TAR)=descending.", ex:"say(sort([3,1,2]))      # → [1,2,3]\nsay(sort([3,1,2], TAR)) # → [3,2,1]" },
  rev:      { sig:"rev(list)",            desc:"Reverse list in place.",            ex:"rev(myList)\nsay(myList)" },
  copy:     { sig:"copy(list)",           desc:"Make a copy of a list.",            ex:"make b = copy(a)" },
  unique:   { sig:"unique(list)",         desc:"Remove duplicate items.",           ex:"say(unique([1,2,2,3,3])) # → [1,2,3]" },
  merge:    { sig:"merge(a, b)",          desc:"Combine two lists into one.",       ex:"say(merge([1,2],[3,4])) # → [1,2,3,4]" },
  first:    { sig:"first(list)",          desc:"Get the first item.",               ex:"say(first([10,20,30])) # → 10" },
  last:     { sig:"last(list)",           desc:"Get the last item.",                ex:"say(last([10,20,30]))  # → 30" },
  flat:     { sig:"flat(list)",           desc:"Flatten one level of nesting.",     ex:"say(flat([[1,2],[3,4]])) # → [1,2,3,4]" },
  howmany:  { sig:"howmany(list, item)",  desc:"Count how many times item appears.",ex:"say(howmany([1,2,1,1], 1)) # → 3" },
  insert:   { sig:"insert(list, i, item)",desc:"Insert item at position i.",        ex:"insert(nums, 0, 99)" },
  fill:     { sig:"fill(val, n)",         desc:"Create list of N identical values.",ex:"say(fill(0, 5)) # → [0,0,0,0,0]" },
  take:     { sig:"take(list, n)",        desc:"Get first N items.",                ex:"say(take([1,2,3,4,5], 3)) # → [1,2,3]" },
  chunk:    { sig:"chunk(list, n)",       desc:"Split list into groups of N.",      ex:"say(chunk([1,2,3,4], 2)) # → [[1,2],[3,4]]" },
  without:  { sig:"without(list, val)",   desc:"Remove all occurrences of val.",    ex:"say(without([1,2,1,3], 1)) # → [2,3]" },
  range_list:{ sig:"range_list(a, b, step?)", desc:"Create a list of numbers.",   ex:"say(range_list(1,6))    # → [1,2,3,4,5]\nsay(range_list(0,10,2)) # → [0,2,4,6,8]" },
  zip_lists:{ sig:"zip_lists(a, b)",      desc:"Combine two lists into pairs.",    ex:"say(zip_lists([1,2],[\"a\",\"b\"])) # → [(1,'a'),(2,'b')]" },

  // Box (Dict)
  box:       { sig:"box()",              desc:"Create an empty dictionary (box).",  ex:"make box info = {}\nput(info, \"name\", \"Alex\")" },
  put:       { sig:"put(box, key, val)", desc:"Set a value in a box.",              ex:'put(data, "score", 100)' },
  get_val:   { sig:"get_val(box, key, default?)", desc:"Get a value from a box.",  ex:'say(get_val(data, "score"))' },
  drop_key:  { sig:"drop_key(box, key)",desc:"Remove a key from a box.",            ex:'drop_key(data, "old_key")' },
  has_key:   { sig:"has_key(box, key)", desc:"Check if key exists in box.",         ex:'say(has_key(data, "name")) # → True' },
  keys_of:   { sig:"keys_of(box)",      desc:"Get all keys as a list.",             ex:'say(keys_of(data))' },
  vals_of:   { sig:"vals_of(box)",      desc:"Get all values as a list.",           ex:'say(vals_of(data))' },
  pairs_of:  { sig:"pairs_of(box)",     desc:"Get list of (key, value) pairs.",     ex:'con loop pair in pairs_of(data):\n    say(pair)' },
  merge_boxes:{ sig:"merge_boxes(a, b)",desc:"Combine two boxes into one.",         ex:"make c = merge_boxes(a, b)" },

  // JSON
  to_json:   { sig:"to_json(x)",        desc:"Convert list/box to JSON string.",    ex:'make txt = to_json({"a":1,"b":2})\nsay(txt)' },
  from_json: { sig:"from_json(s)",      desc:"Parse JSON string into a box/list.",  ex:'make data = from_json(\'{"x":1}\')' },

  // Types
  rank:      { sig:"rank(x)",           desc:"Get the type name of a value.",       ex:'say(rank(42))      # → "int"\nsay(rank("hi"))    # → "str"\nsay(rank([1,2]))   # → "list"' },
  tonum:     { sig:"tonum(x)",          desc:"Convert to number.",                  ex:'say(tonum("99"))  # → 99' },
  totext:    { sig:"totext(x)",         desc:"Convert to string.",                  ex:"say(totext(42))   # → \"42\"" },
  tolist:    { sig:"tolist(x)",         desc:"Convert to list.",                    ex:'say(tolist("abc")) # → ["a","b","c"]' },
  isnull:    { sig:"isnull(x)",         desc:"Is the value NULL?",                  ex:"say(isnull(NULL)) # → True" },
  isnum:     { sig:"isnum(x)",          desc:"Is the value a number?",              ex:"say(isnum(3.14)) # → True" },
  istext:    { sig:"istext(x)",         desc:"Is the value a string?",              ex:'say(istext("hi")) # → True' },
  islist:    { sig:"islist(x)",         desc:"Is the value a list?",                ex:"say(islist([1,2])) # → True" },
  is_empty:  { sig:"is_empty(x)",       desc:"Is the string/list empty?",           ex:'say(is_empty(""))  # → True\nsay(is_empty([]))  # → True' },

  // Time
  wait:      { sig:"wait(ms)",          desc:"Pause the program. 1000 = 1 second.", ex:"say(\"Starting...\")\nwait(2000)\nsay(\"Done!\")" },
  now:       { sig:"now()",             desc:"Current time as HH:MM:SS string.",    ex:'say(now()) # → "14:30:01"' },
  today:     { sig:"today()",           desc:"Today's date as YYYY-MM-DD string.",  ex:'say(today()) # → "2025-01-01"' },

  // File I/O
  read_file:   { sig:"read_file(path)",       desc:"Read entire file as a string.",  ex:'make txt = read_file("data.txt")\nsay(txt)' },
  write_file:  { sig:"write_file(path, text)",desc:"Write text to a file (overwrites).", ex:'write_file("out.txt", "Hello!")' },
  append_file: { sig:"append_file(path, text)",desc:"Add text to end of file.",      ex:'append_file("log.txt", "new line\\n")' },
  read_lines:  { sig:"read_lines(path)",      desc:"Read file as a list of lines.",  ex:'make lines = read_lines("data.txt")\ncon loop l in lines:\n    say(l)' },
  file_exists: { sig:"file_exists(path)",     desc:"Check if a file exists.",        ex:'if file_exists("data.txt"):\n    say("Found!")' },
};

// ─────────────────────────────────────────────────────────
//  G++ keywords for diagnostic checks
// ─────────────────────────────────────────────────────────

const VALID_KEYWORDS = new Set([
  "make","set","fuc","rt","stop","skip","con","won","loop","in",
  "if","elif","else","TAR","FYU","NULL","PI","E","INF","TAU","range"
]);

// ─────────────────────────────────────────────────────────
//  Diagnostics
// ─────────────────────────────────────────────────────────

function validateDocument(document, collection) {
  if (document.languageId !== "gpp") return;
  const diags = [];
  const lines = document.getText().split("\n");

  for (let i = 0; i < lines.length; i++) {
    const raw     = lines[i];
    const trimmed = raw.trim();
    if (!trimmed || trimmed.startsWith("#")) continue;

    // ── Unclosed string ──────────────────────────────────
    let inStr = false, strChar = "";
    for (let j = 0; j < raw.length; j++) {
      const ch = raw[j];
      if (ch === "#" && !inStr) break; // comment
      if (!inStr && (ch === '"' || ch === "'")) {
        inStr = true; strChar = ch;
      } else if (inStr && ch === "\\") {
        j++; // skip escape
      } else if (inStr && ch === strChar) {
        inStr = false;
      }
    }
    if (inStr) {
      diags.push(new vscode.Diagnostic(
        new vscode.Range(i, 0, i, raw.length),
        "Unclosed string — missing closing quote",
        vscode.DiagnosticSeverity.Error
      ));
    }

    // ── Unbalanced parentheses ────────────────────────────
    let depth = 0, firstClose = -1;
    let scanInStr = false, scanChar = "";
    for (let j = 0; j < raw.length; j++) {
      const ch = raw[j];
      if (ch === "#" && !scanInStr) break;
      if (!scanInStr && (ch === '"' || ch === "'")) { scanInStr = true; scanChar = ch; continue; }
      if (scanInStr && ch === "\\") { j++; continue; }
      if (scanInStr && ch === scanChar) { scanInStr = false; continue; }
      if (scanInStr) continue;
      if (ch === "(") depth++;
      else if (ch === ")") {
        depth--;
        if (depth < 0 && firstClose === -1) firstClose = j;
      }
    }
    if (depth !== 0 || firstClose !== -1) {
      const msg = depth > 0 ? "Unclosed parenthesis '('" : "Extra closing parenthesis ')'";
      const col = firstClose !== -1 ? firstClose : raw.length;
      diags.push(new vscode.Diagnostic(
        new vscode.Range(i, col, i, col + 1),
        msg,
        vscode.DiagnosticSeverity.Error
      ));
    }

    // ── Python keywords used instead of G++ ──────────────
    const pythonBoolMatch = /\b(true|false|none|True|False|None)\b/.exec(trimmed);
    if (pythonBoolMatch) {
      const map = { true:"TAR", false:"FYU", none:"NULL", True:"TAR", False:"FYU", None:"NULL" };
      const col = raw.indexOf(pythonBoolMatch[0]);
      diags.push(new vscode.Diagnostic(
        new vscode.Range(i, col, i, col + pythonBoolMatch[0].length),
        `Use '${map[pythonBoolMatch[0]]}' instead of '${pythonBoolMatch[0]}' in G++`,
        vscode.DiagnosticSeverity.Warning
      ));
    }

    // ── Python print/input instead of say/ask ────────────
    const printMatch = /\bprint\s*\(/.exec(raw);
    if (printMatch) {
      diags.push(new vscode.Diagnostic(
        new vscode.Range(i, printMatch.index, i, printMatch.index + 5),
        "Use 'say(...)' instead of 'print(...)' in G++",
        vscode.DiagnosticSeverity.Warning
      ));
    }
    const inputMatch = /\binput\s*\(/.exec(raw);
    if (inputMatch) {
      diags.push(new vscode.Diagnostic(
        new vscode.Range(i, inputMatch.index, i, inputMatch.index + 5),
        "Use 'ask(...)' instead of 'input(...)' in G++",
        vscode.DiagnosticSeverity.Warning
      ));
    }

    // ── def instead of fuc ────────────────────────────────
    const defMatch = /^\s*def\s+/.exec(raw);
    if (defMatch) {
      diags.push(new vscode.Diagnostic(
        new vscode.Range(i, defMatch.index, i, defMatch.index + 3),
        "Use 'fuc name():' instead of 'def name():' in G++",
        vscode.DiagnosticSeverity.Warning
      ));
    }

    // ── Missing colon after if/elif/else/fuc/loop ─────────
    const blockMatch = /^\s*(if|elif|else|fuc\s+\w+\([^)]*\)|con\s+loop.*|won\s+loop.*)/.exec(raw);
    if (blockMatch && trimmed !== "else:" && !trimmed.endsWith(":") && !trimmed.endsWith("\\")) {
      diags.push(new vscode.Diagnostic(
        new vscode.Range(i, 0, i, raw.length),
        "Block statement should end with ':'",
        vscode.DiagnosticSeverity.Warning
      ));
    }
  }

  collection.set(document.uri, diags);
}

// ─────────────────────────────────────────────────────────
//  Hover Provider
// ─────────────────────────────────────────────────────────

const hoverProvider = {
  provideHover(document, position) {
    const range = document.getWordRangeAtPosition(position, /[\w_]+/);
    if (!range) return;
    const word = document.getText(range);
    const doc  = DOCS[word];
    if (!doc) return;

    const md = new vscode.MarkdownString(undefined, true);
    md.isTrusted = true;
    md.appendCodeblock(doc.sig, "gpp");
    md.appendMarkdown(`\n${doc.desc}\n\n**Example:**\n`);
    md.appendCodeblock(doc.ex, "gpp");
    return new vscode.Hover(md, range);
  }
};

// ─────────────────────────────────────────────────────────
//  Completion Provider
// ─────────────────────────────────────────────────────────

const completionProvider = {
  provideCompletionItems(document, position) {
    const line = document.lineAt(position).text.substring(0, position.character);
    const wordMatch = /[\w_]*$/.exec(line);
    const prefix    = wordMatch ? wordMatch[0].toLowerCase() : "";

    const items = [];
    for (const [name, doc] of Object.entries(DOCS)) {
      if (!name.toLowerCase().startsWith(prefix) && prefix.length > 0) continue;

      const item = new vscode.CompletionItem(name, vscode.CompletionItemKind.Function);
      item.detail      = doc.sig;
      item.documentation = new vscode.MarkdownString(`${doc.desc}\n\n**Example:**\n\`\`\`gpp\n${doc.ex}\n\`\`\``);
      item.insertText  = new vscode.SnippetString(
        name.includes("(") ? name : `${name}($1)$0`
      );
      items.push(item);
    }

    // Keywords
    const keywords = ["make","set","fuc","rt","stop","skip","con loop","won loop",
                      "if","elif","else","TAR","FYU","NULL","PI","E","INF"];
    for (const kw of keywords) {
      if (!kw.toLowerCase().startsWith(prefix) && prefix.length > 0) continue;
      const item = new vscode.CompletionItem(kw, vscode.CompletionItemKind.Keyword);
      item.detail = "G++ keyword";
      items.push(item);
    }

    return items;
  }
};

// ─────────────────────────────────────────────────────────
//  Run command
// ─────────────────────────────────────────────────────────

function runGppFile(fileUri) {
  const editor = vscode.window.activeTextEditor;
  const targetUri = fileUri || (editor && editor.document.uri);

  if (!targetUri) {
    vscode.window.showErrorMessage("G++: No file to run.");
    return;
  }

  const filePath = targetUri.fsPath;
  if (!filePath.endsWith(".G++") && !filePath.endsWith(".g++")) {
    vscode.window.showWarningMessage("G++: Expected a .G++ file.");
    return;
  }

  // Save first
  const promise = editor && editor.document.isDirty
    ? editor.document.save()
    : Promise.resolve(true);

  promise.then(() => {
    let terminal = vscode.window.terminals.find(t => t.name === "G++ Runner");
    if (!terminal || terminal.exitStatus !== undefined) {
      terminal = vscode.window.createTerminal({
        name: "G++ Runner",
        env: process.env,
        cwd: path.dirname(filePath)
      });
    }
    terminal.show(true);

    // Try 'G++' first, fall back to 'gpp'
    const cmd = process.platform === "win32"
      ? `python "%USERPROFILE%\\.gpp\\gpp.py" "${filePath}"`
      : `G++ "${filePath}" 2>/dev/null || gpp "${filePath}"`;

    terminal.sendText(cmd);
  });
}

// ─────────────────────────────────────────────────────────
//  Activate
// ─────────────────────────────────────────────────────────

function activate(context) {
  // ── Diagnostics ─────────────────────────────────────────
  const diagCollection = vscode.languages.createDiagnosticCollection("gpp");
  context.subscriptions.push(diagCollection);

  function validate(doc) { validateDocument(doc, diagCollection); }

  vscode.workspace.textDocuments.forEach(validate);
  context.subscriptions.push(
    vscode.workspace.onDidOpenTextDocument(validate),
    vscode.workspace.onDidChangeTextDocument(e => validate(e.document)),
    vscode.workspace.onDidCloseTextDocument(doc => diagCollection.delete(doc.uri))
  );

  // ── Run Command ──────────────────────────────────────────
  context.subscriptions.push(
    vscode.commands.registerCommand("gpp.runFile", (uri) => runGppFile(uri))
  );

  // ── Hover ────────────────────────────────────────────────
  context.subscriptions.push(
    vscode.languages.registerHoverProvider("gpp", hoverProvider)
  );

  // ── Autocomplete ─────────────────────────────────────────
  context.subscriptions.push(
    vscode.languages.registerCompletionItemProvider("gpp", completionProvider, ..."abcdefghijklmnopqrstuvwxyz_")
  );

  console.log("G++ extension activated.");
}

function deactivate() {}

module.exports = { activate, deactivate };

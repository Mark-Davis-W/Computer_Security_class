## 2.0 - Remove “script”
filtered = re.sub(r"(?i)script", "", input)
Target: https://project2.ecen4133.org/search?xssdefense=1
Submission: xss_1.txt

* based off the XSS filter evasion cheat sheet we can approach this problem by exploiting
  malformed IMG tags
* try something like: `<IMG """><SCRIPT>alert("XSS")</SCRIPT>`
* took some tinkering to find something that work but should have a working solution

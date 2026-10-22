# Static Analysis Issues

| Issue | Type | Line(s) before fix | Description | Fix Approach |
|-------|------|--------------------|-------------|--------------|
| Dynamic expression evaluation | Security | 44 | `eval()` allowed arbitrary code execution through the discount expression. | Replaced the expression string with a validated numeric discount rate. |
| Shell command execution | Security | 60 | `os.system()` passed a filename into a shell command and could enable command injection. | Replaced it with a normal Python `print()` call. |
| Weak item hash | Security | 49 | MD5 is unsuitable for security-sensitive hashing. | Replaced MD5 with SHA-256. |
| Predictable checkout PIN | Security | 53 | The standard pseudo-random generator is not appropriate for security-related PINs. | Used `secrets.randbelow()` for cryptographically secure randomness. |
| Broad exception handling | Quality/Security | 28 | A bare `except` hid every exception and silently ignored failures. | Removed exception handling and used `dict.pop(item_id, None)`. |
| Mutable default argument | Quality | 15 | The same audit list was shared by every call. | Changed the default to `None` and initialized a new list per call. |
| Hard-coded credential | Security | 73 | A live-looking gateway secret was embedded in source code and printed. | Removed the credential and its output from the demonstration. |
| Formatting and maintainability | Style | Multiple | Unused imports, non-PEP 8 names, missing docstrings, unused variables, and missing final newline were reported. | Cleaned imports, renamed functions/constants, added docstrings, removed unused code, and formatted the file. |
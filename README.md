Argument Comparer
=================
Check whether commands are equivalent. Although commands may not be
identical (e.g. the arguments are not in the same order) they may have
the same effect.

Usage
-----
```
$ ./argcompare.py --help
Usage: ./argcompare.py [- | COMMAND_A [COMMAND_B]]

        If one argument is specified, it will be interpreted as a command,
        and its opaque description will be printed.

        If two arguments are specified, they will be interpreted as commands
        and compared against each other. If they are equivalent, the exit code is
        0 and nothing is printed. Otherwise, if they are not equivalent, the exit
        code is 1, and an error message is printed to STDERR.

        If - or no arguments are specified, then the commands on STDIN are
        compared to each other.
```

Examples
--------
Compare two inequivalent commands:
```bash
$ ./argcompare.py "git log -u" "git -u log"
Commands are not equivalent.
```

Compare two equivalent commands (doesn't print anything):
```bash
$ ./argcompare.py "cmd --arg1 val1 --arg2 val2" "cmd --arg2 val2 --arg1 val1"
```

Disclaimer
----------
This will not be correct for all commands. This assumse that every
optional argument (prefixed by one or more (-) dashes) is followed by
its value, or by the next optional argument. E.g., this will not work
for commands that have flags that take no value:
```bash
cmd --flag --arg1 val1 arg_at_the_end
```
will not be equivalent to 
```bash
cmd --arg1 val1 --flag arg_at_the_end
```

License
-------
See LICENSE file.

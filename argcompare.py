#!/usr/bin/env python
import sys
import shlex

def describe(listOrString):
  cmd = listOrString
  if type(listOrString) == type(''):
    cmd = shlex.split(listOrString)
  if type(cmd) != type([]):
    raise Exception("Expects a string or list.")

  arg_groups = {}
  loose_args = []
  n = 0
  while n < len(cmd):
    arg = cmd[n]
    if arg[0] == '-':
      group = {}
      group['after'] = len(loose_args) - 1
      if n+1 < len(cmd) and cmd[n+1][0] != '-':
        group['val'] = cmd[n+1]
        n += 1
      if not arg in arg_groups: arg_groups[arg] = []
      arg_groups[arg].append(group)
    else:
      loose_args.append(arg)
    n += 1

  return {'arg_groups': arg_groups, 'loose_args': loose_args}

def equivalent(cmdA, cmdB):
  a = describe(cmdA)
  b = describe(cmdB)
  return a == b

if __name__ == '__main__':
  if len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help']:
    print "Usage:", sys.argv[0], "[- | COMMAND_A [COMMAND_B]]"
    print "\n\tIf one argument is specified, it will be interpreted as a command,"
    print "\tand its opaque description will be printed."
    print "\n\tIf two arguments are specified, they will be interpreted as commands"
    print "\tand compared against each other. If they are equivalent, the exit code is"
    print "\t0 and nothing is printed. Otherwise, if they are not equivalent, the exit"
    print "\tcode is 1, and an error message is printed to STDERR."
    print "\n\tIf - or no arguments are specified, then the commands on STDIN are"
    print "\tcompared to each other.\n"
    sys.exit(0)
  if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] == '-'):
    commands = sys.stdin.readlines()
    if len(commands) == 1:
      print repr(describe(commands[0]))
    else:
      for n in range(0, len(commands)-1):
        if not equivalent(commands[n], commands[n+1]):
          sys.stderr.write("Commands are not equivalent.\n")
          sys.exit(1)
    sys.exit(0)

  if len(sys.argv) == 2:
    print repr(describe(sys.argv[1]))
    sys.exit(0)

  if len(sys.argv) > 2: # compare two commands
    if not equivalent(sys.argv[1], sys.argv[2]):
      sys.stderr.write("Commands are not equivalent.\n")
      sys.exit(1)
    sys.exit(0)

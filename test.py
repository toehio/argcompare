from argcompare import describe, equivalent


def areCommandsEquivalent(cmds):
  for n in range(0, len(cmds)-1):
    if not equivalent(cmds[n], cmds[n+1]):
      return False
  return True

def commandsShouldBeEquivalent(cmds):
  if not areCommandsEquivalent(cmds):
    raise Exception("Expected commands to be equivalent")

def commandsShouldNotBeEquivalent(cmds):
  if areCommandsEquivalent(cmds):
    raise Exception("Expected commands to *not* be equivalent")


commandsShouldBeEquivalent(['cmd', 'cmd'])
commandsShouldBeEquivalent(['cmd', 'cmd '])
commandsShouldBeEquivalent(['cmd arg1', 'cmd arg1'])
commandsShouldBeEquivalent(['cmd arg1', 'cmd   arg1  '])
commandsShouldBeEquivalent(['cmd -f', 'cmd -f'])
commandsShouldBeEquivalent(['cmd --f', 'cmd --f'])
commandsShouldBeEquivalent(['cmd --arg1', 'cmd --arg1'])
commandsShouldBeEquivalent(['cmd --arg1 val1', 'cmd --arg1 val1'])
commandsShouldBeEquivalent(['cmd -a --arg1 val1', 'cmd -a --arg1 val1'])
commandsShouldBeEquivalent(['cmd --arg1 val1 -a', 'cmd -a --arg1 val1'])
commandsShouldBeEquivalent(['cmd --arg1 val1 --arg2 val2', 'cmd --arg1 val1 --arg2 val2'])
commandsShouldBeEquivalent(['cmd --arg1 val1 --arg2 val2', 'cmd --arg2 val2 --arg1 val1'])
commandsShouldBeEquivalent(['cmd --arg1 val1 --arg2 val2 end', 'cmd --arg2 val2 --arg1 val1 end'])


commandsShouldNotBeEquivalent(['cmd', 'cmd2'])
commandsShouldNotBeEquivalent(['cmd', 'cmd -a'])
commandsShouldNotBeEquivalent(['cmd foo -a', 'cmd -a foo'])
commandsShouldNotBeEquivalent(['cmd --arg1 val1 --arg2 val2', 'cmd --arg2 val1 --arg1 val2'])
commandsShouldNotBeEquivalent(['cmd --arg1 val1 --arg2 val2', 'cmd --arg2 val2 bar --arg1 val2'])
commandsShouldNotBeEquivalent(['cmd --arg1 val1 --arg2 val2', 'cmd --arg2 val2 --arg1 val2 bar'])

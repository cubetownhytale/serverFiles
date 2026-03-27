import subprocess
import fast
import time

serverFolder=fast.files.File(__file__).getParentFolder()
c=fast.console.Console()
c.runCmd(f'cd "{serverFolder}"')
c.runCmd(f'start "website" /d"{serverFolder}" python "{serverFolder}/website/__init__.py"',False,True)
print("launched website")
# time.sleep(1)
c2=fast.console.Console()
c2.runCmd(f'cd "{serverFolder}"')
c2.runCmd(f'start "discordBot" /d"{serverFolder}" python "{serverFolder}/discordBot/__init__.py"',False,True)
print("launched discordBot")
# time.sleep(1)
c3=fast.console.Console()
c3.runCmd(f'cd "{serverFolder}"')
c3.runCmd(f'start "server" /d"{serverFolder}" python "{serverFolder}/launchServer.py"',False,True)
print("launched server")
# time.sleep(1)
c4=fast.console.Console()
c4.runCmd(f'cd "{serverFolder}"')
c4.runCmd(f'start "gitCommitSystem" /d"{serverFolder}" python "{serverFolder}/gitCommitSystem/__init__.py"',False,True)
print("launched gitCommitSystem")
c5=fast.console.Console()
c5.runCmd(f'cd "{serverFolder}"')
c5.runCmd(f'start "proxyServer" /d"{serverFolder}" python "{serverFolder}/proxyServer/__init__.py"',False,True)
print("launched proxyServer")
# from . import website
# from . import discordBot
# from . import launchServer
# fast.devTools.reloadModuleRecursive()

# time.sleep(100)
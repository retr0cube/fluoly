#_______Modules__________#

import subprocess

#_______Variables__________#

GIT_CLONE = ["git", "clone", "https://github.com/retr0cube/fluoly.git"]
CD_FLUOLY = ["cd", "fluoly"]
PIP_INSTALL = ["pip3", "install", "."]
PATH_TO_TEST = ["cd", "./tests"]

TOOL_WIN_86 = ["python", "-m", "fluoly", "install", "regolith", "--machine", "Windows", "--cpu_arch", "x86"]
TOOL_WIN_64 = ["python", "-m", "fluoly", "install", "regolith", "--machine", "Windows", "--cpu_arch", "AMD64"]
TOOL_LIN_64 = ["python", "-m", "fluoly", "install", "regolith", "--machine", "Linux", "--cpu_arch", "AMD64"]
PLUGIN = ["python", "-m", "fluoly", "install", "mcblend"]
ADDON = ["python", "-m", "fluoly", "install", "fallen_kingdom", "-v", "1.0.0.1"]

ORDER = [GIT_CLONE, CD_FLUOLY, PIP_INSTALL, PATH_TO_TEST, TOOL_WIN_86, TOOL_WIN_64, TOOL_LIN_64, PLUGIN, ADDON]

for proc in ORDER:
    try:
        subprocess.call(proc)
        print(f"PROCESS {proc} PASSED")
    except Exception as e:
        print(f"PROCESS {proc} FAILED")
        print(e)
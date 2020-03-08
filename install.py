import subprocess
import importlib, site

msgpy = ['python', '-m', 'pip', 'uninstall', 'msgpack-python']
msg = ['python', '-m', 'pip', 'install', '-U' ,'msgpack']
nump = ['python', '-m', 'pip', 'install', 'numpy']
pyn = ['python', '-m', 'pip', 'install', 'pynvim']

try:
    res = subprocess.check_call(msgpy)
    res = subprocess.check_call(msg)
    res = subprocess.check_call(nump)
    res = subprocess.check_call(pyn)
    importlib.reload(site)
except Exception:
    traceback.print_exc()

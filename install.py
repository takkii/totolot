import subprocess
import importlib, site

class InstallerClass:
    msgpy = ['python3', '-m', 'pip', 'uninstall', 'msgpack-python']
    msg = ['python3', '-m', 'pip', 'install', '-U' ,'msgpack']
    nump = ['python3', '-m', 'pip', 'install', 'numpy']
    pyn = ['python3', '-m', 'pip', 'install', 'pynvim']

    def msgpy_method(self):
        res = subprocess.check_call(self.msgpy)
    def msg_method(self):
        res = subprocess.check_call(self.msg)
    def nump_method(self):
        res = subprocess.check_call(self.nump)
    def pyn_method(self):
        res = subprocess.check_call(self.pyn)


InstClass = InstallerClass()
InstClass.msgpy_method()
InstClass.msg_method()
InstClass.nump_method()
InstClass.pyn_method()

importlib.reload(site)
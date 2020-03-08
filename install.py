import subprocess
import importlib, site

class InstallerClass:
    msgpy = ['python', '-m', 'pip', 'uninstall', 'msgpack-python']
    msg = ['python', '-m', 'pip', 'install', '-U' ,'msgpack']
    nump = ['python', '-m', 'pip', 'install', 'numpy']
    pyn = ['python', '-m', 'pip', 'install', 'pynvim']

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
import subprocess
import importlib, site

class InstallerClass:
    msgpy = ['python3', '-m', 'pip', 'uninstall', 'msgpack-python']
    msg = ['python3', '-m', 'pip', 'install', '-U' ,'msgpack']
    nump = ['python3', '-m', 'pip', 'install', 'numpy']
    pyn = ['python3', '-m', 'pip', 'install', 'pynvim']

    def msgpy_method(self):
        try:
            res = subprocess.check_call(self.msgpy)
        except Exception:
            traceback.print_exc()
    def msg_method(self):
        try:
            res = subprocess.check_call(self.msg)
        except Exception:
            traceback.print_exc()
    def nump_method(self):
        try:
            res = subprocess.check_call(self.nump)
        except Exception:
            traceback.print_exc()
    def pyn_method(self):
        try:
            res = subprocess.check_call(self.pyn)
        except Exception:
            traceback.print_exc()

InstClass = InstallerClass()
InstClass.msgpy_method()
InstClass.msg_method()
InstClass.nump_method()
InstClass.pyn_method()

importlib.reload(site)
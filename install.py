import sys, traceback
import subprocess
import importlib, site

class InstallerClass:
    msgpy = ['python', '-m', 'pip', 'uninstall', 'msgpack-python']
    msg = ['python', '-m', 'pip', 'install', '-U' ,'msgpack']
    nump = ['python', '-m', 'pip', 'install', 'numpy']
    pyn = ['python', '-m', 'pip', 'install', 'pynvim']

    def msgpy_method(self):
        try:
            ret_msgpy = subprocess.run(self.msgpy)
            ret_msgpy
        except Exception:
            traceback.print_exc()
    def msg_method(self):
        try:
            ret_msg = subprocess.run(self.msg)
            ret_msg
        except Exception:
            traceback.print_exc()
    def nump_method(self):
        try:
            nump = subprocess.run(self.nump)
            nump
        except Exception:
            traceback.print_exc()
    def pyn_method(self):
        try:
            pyn = subprocess.run(self.pyn)
            pyn
        except Exception:
            traceback.print_exc()

InstClass = InstallerClass()
InstClass.msgpy_method()
InstClass.msg_method()
InstClass.nump_method()
InstClass.pyn_method()

importlib.reload(site)

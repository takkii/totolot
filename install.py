import sys, traceback
import subprocess, platform
import importlib, site


class InstallerClass:
    msgpy = ['python3', '-m', 'pip', 'uninstall', 'msgpack-python']
    msg = ['python3', '-m', 'pip', 'install', 'msgpack==1.0.0']
    nump = ['python3', '-m', 'pip', 'install', 'numpy']
    pyn = ['python3', '-m', 'pip', 'install', 'pynvim']
    pan = ['python3', '-m', 'pip', 'install', 'pandas']

    msgpy_win = ['python', '-m', 'pip', 'uninstall', 'msgpack-python']
    msg_win = ['python', '-m', 'pip', 'install', 'msgpack==1.0.0']
    nump_win = ['python', '-m', 'pip', 'install', 'numpy']
    pyn_win = ['python', '-m', 'pip', 'install', 'pynvim']
    pan_win = ['python', '-m', 'pip', 'install', 'pandas']

    def msgpy_win_method(self):
        try:
            ret_msgpy_win = subprocess.run(self.msgpy_win, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_msgpy_win)
        except Exception:
            traceback.print_exc()

    def msg_win_method(self):
        try:
            ret_msg_win = subprocess.run(self.msg_win, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_msg_win)
        except Exception:
            traceback.print_exc()

    def nump_win_method(self):
        try:
            ret_nump_win = subprocess.run(self.nump_win, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_nump_win)
        except Exception:
            traceback.print_exc()

    def pyn_win_method(self):
        try:
            ret_pyn_win = subprocess.run(self.pyn_win, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_pyn_win)
        except Exception:
            traceback.print_exc()

    def pan_win_method(self):
        try:
            ret_pan_win = subprocess.run(self.pan_win, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_pan_win)
        except Exception:
            traceback.print_exc()

    def msgpy_method(self):
        try:
            ret_msgpy = subprocess.run(self.msgpy, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_msgpy)
        except Exception:
            traceback.print_exc()

    def msg_method(self):
        try:
            ret_msg = subprocess.run(self.msg, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_msg)
        except Exception:
            traceback.print_exc()

    def nump_method(self):
        try:
            ret_nump = subprocess.run(self.nump, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_nump)
        except Exception:
            traceback.print_exc()

    def pyn_method(self):
        try:
            ret_pyn = subprocess.run(self.pyn, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_pyn)
        except Exception:
            traceback.print_exc()

    def pan_method(self):
        try:
            ret_pan = subprocess.run(self.pan, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_pan)
        except Exception:
            traceback.print_exc()


if sys.version_info[0] == 2:
    print("This installer is Python2 not supported.")

elif sys.version_info[0] == 3:
    pf = platform.system()
    if pf == 'Windows':
        InstClass = InstallerClass()
        InstClass.msgpy_win_method()
        InstClass.msg_win_method()
        InstClass.nump_win_method()
        InstClass.pyn_win_method()
        InstClass.pan_win_method()

    elif pf == 'Darwin':
        InstClass = InstallerClass()
        InstClass.msgpy_method()
        InstClass.msg_method()
        InstClass.nump_method()
        InstClass.pyn_method()
        InstClass.pan_method()

    elif pf == 'Linux':
        InstClass = InstallerClass()
        InstClass.msgpy_method()
        InstClass.msg_method()
        InstClass.nump_method()
        InstClass.pyn_method()
        InstClass.pan_method()

    else:
        print("Installer does not support OS other than Windows, MacOS and Linux kernel.")


else:
    print("A version other than Python2 and Python3. Does not match.")

importlib.reload(site)

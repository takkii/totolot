import traceback, subprocess ,sys
import importlib, site, platform

class InstallerClass:
    sci_win = ['python', '-m', 'pip', 'install', 'scikit-learn']
    nump_win = ['python', '-m', 'pip', 'install', 'numpy']
    pan_win = ['python', '-m', 'pip', 'install', 'pandas']
    req_win = ['python', '-m', 'pip', 'install', 'requests-html']
    bs4_win = ['python', '-m', 'pip', 'install', 'beautifulsoup4']

    sci = ['python3', '-m', 'pip', 'install', 'scikit-learn']
    nump = ['python3', '-m', 'pip', 'install', 'numpy']
    pan = ['python3', '-m', 'pip', 'install', 'pandas']
    req = ['python3', '-m', 'pip', 'install', 'requests-html']
    bs4 = ['python3', '-m', 'pip', 'install', 'beautifulsoup4']

    def sci_win_method(self):
        try:
            ret_sci_win = subprocess.run(self.sci_win, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_sci_win)
        except Exception:
            traceback.print_exc()
    def nump_win_method(self):
        try:
            ret_nump_win = subprocess.run(self.nump_win, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_nump_win)
        except Exception:
            traceback.print_exc()
    def pan_win_method(self):
        try:
            ret_pan_win = subprocess.run(self.pan_win, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_pan_win)
        except Exception:
            traceback.print_exc()
    def req_win_method(self):
        try:
            ret_req_win = subprocess.run(self.req_win, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_req_win)
        except Exception:
            traceback.print_exc()
    def bs4_win_method(self):
        try:
            ret_bs4_win = subprocess.run(self.bs4_win, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_bs4_win)
        except Exception:
            traceback.print_exc()

    def sci_method(self):
        try:
            ret_sci = subprocess.run(self.sci, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_sci)
        except Exception:
            traceback.print_exc()
    def nump_method(self):
        try:
            ret_nump = subprocess.run(self.nump, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_nump)
        except Exception:
            traceback.print_exc()
    def pan_method(self):
        try:
            ret_pan = subprocess.run(self.pan, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_pan)
        except Exception:
            traceback.print_exc()
    def req_method(self):
        try:
            ret_req = subprocess.run(self.req, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_req)
        except Exception:
            traceback.print_exc()
    def bs4_method(self):
        try:
            ret_bs4 = subprocess.run(self.bs4, encoding='utf-8', stderr=subprocess.PIPE)
            print(ret_bs4)
        except Exception:
            traceback.print_exc()

if sys.version_info[0] == 2:
  print("This installer is Python2 not supported.")

elif sys.version_info[0] == 3:
    pf = platform.system()
    if pf == 'Windows':
       InstClass = InstallerClass()
       InstClass.sci_win_method()
       InstClass.nump_win_method()
       InstClass.pan_win_method()
       InstClass.req_win_method()
       InstClass.bs4_win_method()

    elif pf == 'Darwin':
       InstClass = InstallerClass()
       InstClass.sci_method()
       InstClass.nump_method()
       InstClass.pan_method()
       InstClass.req_method()
       InstClass.bs4_method()

    elif pf == 'Linux':
       InstClass = InstallerClass()
       InstClass.sci_method()
       InstClass.nump_method()
       InstClass.pan_method()
       InstClass.req_method()
       InstClass.bs4_method()

    else:
       print("Windows and MacOS and Linux other OS not supported.")


else:
  print("Python2 and Python3 Version is No match.")

importlib.reload(site)

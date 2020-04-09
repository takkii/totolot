import traceback
import subprocess
import importlib, site

class InstallerClass:
    sci = ['python', '-m', 'pip', 'install', 'scikit-learn']
    nump = ['python', '-m', 'pip', 'install', 'numpy']
    pan = ['python', '-m', 'pip', 'install', 'pandas']
    req = ['python', '-m', 'pip', 'install', 'requests-html']
    bs4 = ['python', '-m', 'pip', 'install', 'beautifulsoup4']

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

InstClass = InstallerClass()
InstClass.sci_method()
InstClass.nump_method()
InstClass.pan_method()
InstClass.req_method()
InstClass.bs4_method()

importlib.reload(site)

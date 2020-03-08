import pip, site, importlib

pip.main(['uninstall', 'msgpack-python'])
#pip.main(['install','msgpack'])
pip.main(['install','-U','msgpack'])
pip.main(['install','numpy'])

importlib.reload(site)

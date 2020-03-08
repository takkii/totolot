from pip._internal import main as _main
import importlib

def _import(name, module, ver=None):
    try:
        globals()[name] = importlib.import_module(module)
    except ImportError:
        try:
            if ver is None:
                _main(['install', module])
            else:
                _main(['install', '{}=={}'.format(module, ver)])
            globals()[name] = importlib.import_module(module)
        except:
            print("can't import: {}".format(module))

_import('msg','msgpack', '1.0.0')
_import('nump','numpy', '1.18.1')

print(msg)
print(nump)
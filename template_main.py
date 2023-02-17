import sys
import importlib

if __name__ == '__main__':
    # TODO specify the right path
    install_dir = 'PATH/TO/abc_export'
    if not sys.path.__contains__(install_dir):
        sys.path.append(install_dir)

    modules = [
        "ABCExport",
        "ABCExportAsset",
    ]

    from utils import *
    unload_packages(silent=True, packages=modules)

    for module in modules:
        importlib.import_module(module)

    from ABCExport import *

    try:
        abc_export.close()
    except:
        pass
    abc_export = ABCExport()
    abc_export.show()

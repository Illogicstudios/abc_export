import sys
import importlib
import subprocess
from threading import Thread
from pymel.all import *
from PySide2 import QtWidgets
install_dir = 'C:/Users/m.jenin/Documents/marius/abc_export'
if not sys.path.__contains__(install_dir): sys.path.append(install_dir)
modules = ["ABCExport", "ABCExportAsset", "export_abc_scenes"]
from utils import *
unload_packages(silent=True, packages=modules)
for module in modules: importlib.import_module(module)
import export_abc_scenes

# ######################################################################################################################
__FOLDER_TYPE = r"^anim$"                   # ANIM
# __FOLDER_TYPE = r"^layout$"                 # LAYOUT
# __FOLDER_TYPE = r"^(anim|layout)$"          # ANIM and LAYOUT
# ######################################################################################################################


def export_all(current_project_dir, scenes):
    subprocess.check_call([r"C:\Program Files\Autodesk\Maya2022\bin\mayapy.exe","C:/Users/m.jenin/Documents/marius/abc_export/export_abc_scenes.py", current_project_dir] + scenes)


current_project_dir = os.getenv("CURRENT_PROJECT_DIR")
if current_project_dir is None:
    print_warning("CURRENT_PROJECT_DIR has not been found")
    exit(1)
scenes = export_abc_scenes.list_scenes(current_project_dir, __FOLDER_TYPE)
if len(scenes) == 0:
    print_warning("No scene found")
    exit(1)
scenes_cpd_stripped = [s.replace(current_project_dir,"") for s in scenes]
scenes_str = "\n".join(scenes_cpd_stripped)
ret = QtWidgets.QMessageBox().question(None, '', "Are you sure to export abcs from these scenes ?\n\n"+scenes_str, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
if ret == QtWidgets.QMessageBox.Yes:
    thread = Thread(target = export_all, args = (current_project_dir, scenes))
    thread.start()

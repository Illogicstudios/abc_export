import os
import re

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# ######################################################################################################################

__FOLDER_TYPE = r"^anim$"                   # ANIM
# __FOLDER_TYPE = r"^layout$"               # LAYOUT
# __FOLDER_TYPE = r"^(anim|layout)$"        # ANIM and LAYOUT

# ######################################################################################################################

def print_scene_paths(scenes):
    print("\n############################################################\n")
    print("                      Copy-paste this :\n")
    for scene in scenes:
        print(scene + " ^")
    print("\n############################################################\n")


file_dialog = QFileDialog()
file_dialog.setFileMode(QFileDialog.DirectoryOnly)
file_dialog.setOption(QFileDialog.DontUseNativeDialog, True)
file_view = file_dialog.findChild(QListView, 'listView')
file_view.setSelectionMode(QAbstractItemView.MultiSelection)
f_tree_view = file_dialog.findChild(QTreeView)
f_tree_view.setSelectionMode(QAbstractItemView.MultiSelection)

paths = []
if file_dialog.exec():
    paths = file_dialog.selectedFiles()

version_folders = []

for path in paths:
    for folder in os.listdir(path):
        if re.match(__FOLDER_TYPE, folder):
            folder_path = os.path.join(path, folder)
            for version_folder in sorted(os.listdir(folder_path), reverse=True):
                if re.match(r"^([0-9]+)$", version_folder):
                    version_folders.append(os.path.join(folder_path, version_folder))
                    break

scene_paths = []
for version_folder in version_folders:
    for file in sorted(os.listdir(version_folder), reverse=True):
        file_path = os.path.join(version_folder, file).replace("\\","/")
        if re.match(r".*\.m[ab]$", file_path):
            scene_paths.append(file_path)
            break

scene_paths = sorted(scene_paths)
print_scene_paths(scene_paths)

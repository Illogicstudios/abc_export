from pymel.core import *
import os
import sys
import re

from ABCExport import *

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


def list_scenes(current_project_dir, folder_type):
    file_dialog = QFileDialog()
    file_dialog.setDirectory(current_project_dir)
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
            if re.match(folder_type, folder):
                folder_path = os.path.join(path, folder)
                for version_folder in sorted(os.listdir(folder_path), reverse=True):
                    if re.match(r"^([0-9]+)$", version_folder):
                        version_folders.append(os.path.join(folder_path, version_folder))
                        break

    scene_paths = []
    for version_folder in version_folders:
        for file in sorted(os.listdir(version_folder), reverse=True):
            file_path = os.path.join(version_folder, file).replace("\\", "/")
            if re.match(r".*\.m[ab]$", file_path):
                scene_paths.append(file_path)
                break

    scene_paths = sorted(scene_paths)
    return scene_paths


def export_char_in_scene(scene_path, database_path, abc_path, nb , nb_tot):
    os.system("cls")
    print("\n########################################################################################################\n")
    print("Opening the scene : "+scene_path)
    print("Scene "+nb+" on "+nb_tot)
    print("\n########################################################################################################\n\n\n")
    openFile(scene_path, force=True)

    abcs = ABCExport.retrieve_abcs(database_path)
    start_frame = int(playbackOptions(min=True, query=True))
    end_frame = int(playbackOptions(max=True, query=True))

    abc_exported = []
    for abc in abcs:
        name_num = abc.get_name_with_num()
        asset_dir_path = os.path.join(abc_path, name_num)
        next_version = str(ABCExportAsset.next_version(asset_dir_path))
        os.system("cls")
        print("\n########################################################################################################\n")
        print("Exporting : " + name_num)
        print("Version : " + next_version)
        print("from the scene : " + scene_path)
        print("Scene "+nb+" on "+nb_tot)
        print("\n########################################################################################################\n\n\n")
        abc_exported.append((name_num, next_version))
        abc.export(abc_path, start_frame, end_frame)
    return abc_exported


def export_abcs_from_scenes(list_scenes, current_project_dir):
    database_path = os.path.join(current_project_dir, "assets/_database")
    scene_abc_exported = {}
    nb_scenes = len(list_scenes)
    i = 1
    for file_path in list_scenes:
        if os.path.isfile(file_path) and re.match(r".*\.m[ab]$", file_path):
            match = re.match(r"^(" + current_project_dir + r"\/shots\/[a-zA-Z0-9_\- \.]+)\/.*$", file_path)
            if match:
                shot_folder = match.group(1)
                abc_export_path = os.path.join(shot_folder, "abc")
                os.makedirs(abc_export_path, exist_ok=True)
                scene_abc_exported[file_path] = export_char_in_scene(file_path, database_path, abc_export_path, str(i) , str(nb_scenes))
        i += 1

    os.system("cls")
    print("\n########################################################################################################")
    print("ABC Exported by scene :")
    for scene_path, abcs in scene_abc_exported.items():
        print("\n" + scene_path + " :")
        for abc, version in abcs:
            print("\t" + abc + " ["+version+"]")
    print(
        "\n########################################################################################################\n")


if __name__ == '__main__':
    export_abcs_from_scenes(sys.argv[2:],sys.argv[1])
    os.system("pause")

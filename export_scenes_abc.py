from pymel.core import *
import os
import sys

from ABCExport import *

current_project_dir = os.getenv("CURRENT_PROJECT_DIR")
if current_project_dir is None:
    print("CURRENT_PROJECT_DIR has not been found")
    exit(1)

__DATABASE_PATH = os.path.join(current_project_dir, "assets/_database")


def export_char_in_scene(scene_path, database_path, abc_path):
    openFile(scene_path, force=True)

    abcs = ABCExport.retrieve_abcs(database_path)
    start_frame = int(playbackOptions(min=True, query=True))
    end_frame = int(playbackOptions(max=True, query=True))

    for abc in abcs:
        abc.export(abc_path, start_frame, end_frame)


if __name__ == '__main__':
    for file_path in sys.argv[1:]:
        if os.path.isfile(file_path) and re.match(r".*\.m[ab]$", file_path):
            match = re.match(r"^(" + current_project_dir + r"\/shots\/[a-zA-Z0-9_\- \.]+)\/.*$", file_path)
            if match:
                shot_folder = match.group(1)
                abc_export_path = os.path.join(shot_folder, "abc")
                os.makedirs(abc_export_path, exist_ok=True)
                print(abc_export_path)
                # export_char_in_scene(file_path, __DATABASE_PATH, abc_export_path)

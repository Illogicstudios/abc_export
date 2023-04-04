import importlib
import sys
# TODO specify the right path
install_dir = 'PATH/TO/abc_export'
if not sys.path.__contains__(install_dir): sys.path.append(install_dir)
import export_abc_scenes
importlib.reload(export_abc_scenes)

# ######################################################################################################################
__FOLDER_TYPE = r"^anim$"  # ANIM
#__FOLDER_TYPE = r"^layout$"                 # LAYOUT
#__FOLDER_TYPE = r"^(anim|layout)$"          # ANIM and LAYOUT

__FILTER_CHAR = ""
#__FILTER_CHAR = "ch_namechar"

# __SUBSAMPLE = ""
__SUBSAMPLE = "-0.125 0 0.125"

__LOG_FILE_FOLDER = r"I:\tmp\log\abc_export"
# ######################################################################################################################

export_abc_scenes.run_export_abc_scenes(__FOLDER_TYPE, __FILTER_CHAR, __SUBSAMPLE, __LOG_FILE_FOLDER)

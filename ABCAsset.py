import os
import logging
from pymel.core import *


class ABCAsset:

    # Get the next version (version when the ABC will be exported)
    @staticmethod
    def next_version(folder):
        version = 1
        if os.path.isdir(folder):
            for f in os.listdir(folder):
                if os.path.isdir(os.path.join(folder, f)):
                    try:
                        v = int(f)
                        if v > version:
                            version = v
                    except Typeerror:
                        pass
        path = os.path.join(folder, str(version).zfill(4))
        while os.path.exists(path):
            version += 1
            path = os.path.join(folder, str(version).zfill(4))
        return version

    def __init__(self, name, namespace, geos):
        self.__name = name
        self.__namespace = namespace
        self.__num = 0
        self.__geos = geos

    # Geter of the name merged with the num
    def get_name_with_num(self):
        return self.__name + "_" + str(self.__num).zfill(2)

    # Setter of the num
    def set_num(self, num):
        self.__num = num

    # Getter of the geos
    def get_geos(self):
        return self.__geos

    # Export this reference in ABC in a new version
    def export(self, folder, start, end):
        abc_name = self.get_name_with_num()
        asset_dir_path = os.path.join(folder, abc_name)
        next_version = ABCAsset.next_version(asset_dir_path)
        version_dir_path = os.path.join(asset_dir_path, str(next_version).zfill(4))
        path = os.path.join(version_dir_path, abc_name + ".abc")
        path = path.replace("\\", "/")

        os.makedirs(version_dir_path, exist_ok=True)

        command = "-frameRange %s %s" % (start, end)
        command += " -writeVisibility  -stripNamespaces  -worldSpace -dataFormat ogawa -eulerFilter "
        if not self.__geos:
            return
        for geo in self.__geos:
            command += " -root %s" % geo
        command += " -file \"%s\"" % (path)

        refresh(suspend=True)
        AbcExport(j=command)
        refresh(suspend=False)

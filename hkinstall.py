from hkpilot.utils.cmake import CMake

import inspect
import os


class ROOT(CMake):

    def __init__(self, path):
        super().__init__(path)

        self._package_name = "ROOT"
        self._package_version = "v6.26.04"
        self._download_url = "https://root.cern/download/root_v6.26.04.source.tar.gz"
        # self._git_url = "git@github.com:zeromq/libzmq.git"
        # self._git_branch = "master"
        # self._git_tag = "v4.3.482"
        # self._git_clone_dir = "src"
        self._cmakelist_path = "src/root-6.26.04"

        self._cmake_options = {
            "CMAKE_CXX_STANDARD": "14",
            # "Geant4_DIR": "/Users/mguigue/Work/T2K/HK/Software/newSystem/hkpilot/../Geant4/install-Darwin_arm64-gcc_13.1.6-python_3.9.13"
        }

        # self._path = os.path.relpath(inspect.getfile(self.__class__))

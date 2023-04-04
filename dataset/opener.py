import pathlib
import substratools as tools

import os

class StubOpener(tools.Opener):
    def fake_data(self, n_samples=None):
        return ""

    def get_data(self, folders):
        return list(pathlib.Path(folders[0]).glob("*.txt"))[0]

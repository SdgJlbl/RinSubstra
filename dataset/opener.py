import pathlib
import substratools as tools

import os

class StubOpener(tools.Opener):
    def fake_data(self, n_samples=None):
        return 0

    def get_data(self, folders):
        path = list(pathlib.Path(folders[0]).glob("*.txt"))[0]
        return path.read_text()

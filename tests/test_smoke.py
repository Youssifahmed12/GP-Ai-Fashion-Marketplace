import importlib
import unittest


class SmokeTest(unittest.TestCase):
    def test_packages_import(self):
        for name in ("outfits", "catalog", "embeddings", "vision", "master"):
            importlib.import_module(name)


if __name__ == "__main__":
    unittest.main()

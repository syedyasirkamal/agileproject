import unittest
import pathlib as pl


class TestCaseBase(unittest.TestCase):
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

class TemplateTest(TestCaseBase):
    def test(self):
        path = pl.Path("/workspace/templates/index.html")
        self.assertIsFile(path)

class StaticTest(TestCaseBase):
    def test(self):
        path = pl.Path("/workspace/static/css/globals.css")
        self.assertIsFile(path)

if __name__ == '__main__':
    unittest.main()


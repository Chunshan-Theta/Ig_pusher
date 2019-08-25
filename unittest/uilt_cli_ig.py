import unittest
from util.cli import *


class TestUtilIG(unittest.TestCase):
    """Test Util Tool"""

    @classmethod
    def setUp(self) -> None:
        self.obj= ig_cli('just.test.pusher','00000000')

    @classmethod
    def tearDown(self) -> None:
        del self.obj

    def test_connection(self):
        self.assertTrue(self.obj.status())

    def test_upload(self):
        token = self.obj.push_post("../test_pic.png", "some_word")
        self.assertTrue(token)


import unittest

import bslint.constants as const
from tests.resources.common.test_methods import CommonMethods as Common


class TestMultiLineReductionParse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_while_block(self):
        self.common.match_program("while x = 3\ni = 4\nendwhile", const.BLOCK_STATEMENT)

    def test_while_closed_with_endfor(self):
        self.common.exception_runner("while x = 3\ni = 4\n end for")

    def test_while_closed_with_endif(self):
        self.common.exception_runner("while x = 3\ni = 4\n end if")
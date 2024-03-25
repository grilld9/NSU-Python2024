import unittest
import problem2 as tr


class TranslateSymbolsTest(unittest.TestCase):

    def testErrors(self):
        with self.assertRaises(ValueError):
            tr.translate("abc", "ab", "b", "g")

    def testValidArgs(self):
        self.assertEqual(tr.translate("abb", "ab", "cx", ""), "cxx")
        self.assertEqual(tr.translate("bbb", "b", "a", ""), "aaa")

    def testDeleteArg(self):
        self.assertEqual(tr.translate("abb", "xy", "zy", "ab"), "")
        self.assertEqual(tr.translate("aaaaa", "a", "b", "a"), "")

    def testEmptyInput(self):
        self.assertEqual(tr.translate("", "ab", "ab", "a"), "")




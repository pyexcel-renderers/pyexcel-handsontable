import os
import sys
from mock import patch
from unittest import TestCase

PY2 = sys.version_info[0] == 2
PY26 = PY2 and sys.version_info[1] < 7


DEFAULT_CONFIG = ('{"rowHeaders": true, ' +
                  '"readOnly": true, ' +
                  '"colHeaders": true, ' +
                  '"preventOverflow": "hornizontal"}')


class MyTestCase(TestCase):
    def setUp(self):
        self.maxDiff = None
        self._test_file = "test.handsontable.html"
        self.patcher1 = patch(
            'pyexcel_handsontable.handsontable._generate_uuid')
        self.fake_uuid = self.patcher1.start()

        self.patcher2 = patch(
            'pyexcel_handsontable.handsontable._dump_dict')
        self.dump_dict = self.patcher2.start()

    def customAssertMultiLineEqual(self, a, b):
        if PY26:
            self.assertEqual(a, b)
        else:
            self.assertMultiLineEqual(a, b)

    def tearDown(self):
        self.patcher2.stop()
        self.patcher1.stop()
        if os.path.exists(self._test_file):
            os.unlink(self._test_file)

    def compareTwoFiles(self, filea, fileb):
        with open(filea, 'r') as f:
            actual = f.read()
        with open(fileb, 'r') as f:
            expected = f.read()
        self.customAssertMultiLineEqual(expected, actual)

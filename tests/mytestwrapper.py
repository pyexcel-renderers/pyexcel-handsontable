import sys
from unittest import TestCase

PY2 = sys.version_info[0] == 2
PY26 = PY2 and sys.version_info[1] < 7


DEFAULT_CONFIG = ('{"rowHeaders": true, ' +
                  '"readOnly": true, ' +
                  '"colHeaders": true, ' +
                  '"preventOverflow": "hornizontal"}')


class MyTestCase(TestCase):

    def customAssertMultiLineEqual(self, a, b):
        if PY26:
            self.assertEqual(a, b)
        else:
            self.assertMultiLineEqual(a, b)

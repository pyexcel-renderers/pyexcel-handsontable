"""
    pyexcel_handsontable
    ~~~~~~~~~~~~~~~~~~~~~~~

    chart drawing plugin for pyexcel

    :copyright: (c) 2016-2017 by Onni Software Ltd.
    :license: New BSD License, see LICENSE for further details
"""
from lml.registry import PluginList, PluginInfo


class MyPluginInfo(PluginInfo):

    def keywords(self):
        file_types = self.file_types
        for file_type in file_types:
            yield file_type


PluginList(__name__)._add_a_plugin(
    MyPluginInfo(
        'renderer',
        '%s.handsontable.HandsonTable' % __name__,
        file_types=['handsontable.html'],
        stream_type='string'
    )
)

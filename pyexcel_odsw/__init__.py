"""
    pyexcel_odsw
    ~~~~~~~~~~~~~~~~~~~
    The lower level ods file format handler
    :copyright: (c) 2018 by Onni Software & its contributors
    :license: New BSD License
"""
from ._version import __version__, __author__  # flake8: noqa
from pyexcel_io.plugins import IOPluginInfoChain
from pyexcel_io.io import isstream, store_data as write_data


__FILE_TYPE__ = 'ods'

IOPluginInfoChain(__name__).add_a_writer(
    relative_plugin_class_path='odsw.ODSWriter',
    file_types=[__FILE_TYPE__],
    stream_type='binary'
)


def save_data(afile, data, file_type=None, **keywords):
    """standalone module function for writing module supported file type"""
    if isstream(afile) and file_type is None:
        file_type = __FILE_TYPE__
    write_data(afile, data, file_type=file_type, **keywords)

from pycore.core import fsutil

import os
import pdb

from .data import *

class Exhume( object ):
    def __init__( self, path ):
        self.path = path

    def run(self, path = None, fltr = '*'):
        dataset = FileSystemDataSet()
        for fname in fsutil.yieldall( self.path, fltr ):
            data = StatData( fname )
            dataset[ fname ] = data

        return dataset#paths



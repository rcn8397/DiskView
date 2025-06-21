from collections.abc import MutableMapping
from pycore.core import fsutil


import os

import pdb

CACHE_DIR = os.path.expanduser('~/.dataview/')

# Data item
# label -> value pair

def init_cache():
    ftutil.mkdir_p( CACHE_DIR )

def clean_cache():
    os.rmdir( CACHE_DIR )

class Data( object ):
    def __init__(self, label, value ):
        self.label = label
        self.value = value

class StatData( Data ):
    def __init__( self, path ):
        super( StatData, self ).__init__( label = path, value = os.stat( path ) )

    @property
    def size( self ):
        return self.value.st_size

class DataSet( MutableMapping ):

    def __init__( self, *args, **kwargs ):
        self.store = dict()
        self.update( dict( *args, **kwargs ))

    def __getitem__( self, key ):
        return self.store[ key ]

    def __setitem__( self, key, value ):
        self.store[ key ] = value

    def __iter__( self ):
        return iter( self.store )

    def __delitem__( self, key ):
        del self.store[ key ]

    def __len__( self ):
        return len( self.store )

    def load( self, d ): pass
        # Load data set from dict

    def dump( self ):
        # Dump the data from the data set
        for key, value in self.items():
            print( key, value )

    def write( self, fname ): pass

    def read( self, fname ): pass


class Size( object ):
    mib={
        'kilobyte':1024,
        'megabyte':1024*1024,
        'gigabyte':1024*1024*1024,
        'terabyte':1024*1024*1024*1024,
    }
    units={
        'kilobyte':'kB',
        'megabyte':'MB',
        'gigabyte':'GB',
        'terabyte':'TB',
    }
    
    def __init__(self, v, mode='megabyte' ):
        self.v = v
        self.mode = mode

    @property
    def value( self ):
        mib = self.mib[self.mode]
        uom = self.units[self.mode]
        val = self.v/mib
        return '{:0.4} {}'.format( val, uom )



class FileSystemDataSet( DataSet ):
    def __init__( self, *args, **kwargs ):
        super( FileSystemDataSet, self ).__init__( *args, **kwargs )

    def dump( self ):
        # Dump the data from the data set
        for key, value in self.items():
            print( key, value.size )

    def dump_sorted( self ):
        ds = self.sort()
        for key, value in ds.items():
            s = Size( value )
            v = s.value
            print( key, v )

    def write( self, fname ):
        pass

    def sort( self ):
        def size_value(item):
            print( '{}:  {}'.format( item[0], item[1].size ) )
            return item[1].size
        
        vals = dict()
        for i, (key, value) in enumerate( sorted( self.store.items(), key = size_value )):
            #print( i, key, value.size, type( value.size) )
            vals[key]=value.size
      
        return vals
        

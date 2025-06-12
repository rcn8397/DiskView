from pycore.core import fsutil

def dir_this():
    for fname in fsutil.yieldall( '.', '*' ):
        print( fname )


class Exhume( object ):
    def __init__( self, path ):
        self.path = path

        

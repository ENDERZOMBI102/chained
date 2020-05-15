from typing import Union
from pathlib import Path

class chainOpen:
    """
        a wrapper around the python's open() to provide a chainable fuction

        example:
        >>> from chained import chainOpen
        >>> chainOpen('C:/hi.txt', 'x').write('hello ').write('world!').close()
        >>> chainOpen('C:/hi.txt', 'r').read().close()
        "hello world!"
    """
    # if the last write operation succeeded
    lastSucceeded: bool = True



    def __init__( self, path: Union[Path, str], mode = 'r' ):
        if not ( mode in ['r', 'x', 'w', 'a', 'b'] ):
            raise ValueError('only r, x, w, a, b are supported operations!')
        if isinstance(path, str): self.filePath = path
        else: self.filePath = path.resolve()
        self.file = open(self.filePath, mode)

    def write( self, txt: Union[str, bytes] ):
        self.lastSucceeded = self.file.write(txt)
        return self
    
    def read( self, size: int = None ):
        return self, self.file.read(size)
            
    def close(self, x='o'):
        self.file.close()
        if x == 'o':
            return _kill(self)
        else: return self

    def reopen(self, mode='r'):
        if not (mode in ['r', 'x', 'w', 'a', 'b']):
            raise ValueError('only r, x, w, a, b are supported operations!')
        self.file = open(self.filePath, mode)
        return self

def _kill(obj):
    del obj
    return None
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
    
    def read( self ):
        return self, self.file.read()
            
    def close(self, data: Union[str, bytes] = None):
        self.file.close()
        if data is not None:
            return data
        

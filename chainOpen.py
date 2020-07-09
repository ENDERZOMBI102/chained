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



    def __init__( self, path: Union[Path, str, bytes], mode = 'r' ):
        if isinstance(path, str): self.filePath = path
        elif isinstance(path, bytes): self.filePath = str(path)
        else: self.filePath = path.resolve()
        self.file = open(self.filePath, mode)

    def write( self, txt: Union[str, bytes] ):
        self.lastSucceeded = self.file.write(txt)
        return self
    
    def readAndClose( self ):
        data = self.file.read()
        self.file.close()
        return data
            
    def close( self ):
        self.file.close()
        
if __name__=='__main__':
	print( chainOpen('code.x', 'r').readAndClose() )

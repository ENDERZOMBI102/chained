class chainOpen:
    """
        a wrapper around the python's open() to provide a chainable fuction
        example:
        >>> from chained import chainOpen
        >>> chainOpen('C:/hi.txt', 'x').write('hello ').write('world!').close()
        >>> chainOpen('C:/hi.txt', 'r').read().close()
        "hello world!"
    """
    def __init__( self, path: Union([Path, str]), mode = 'r' ):
        if not ( mode in ['r', 'x', 'w', 'a', 'b'] ):
            raise ValueError('only r, x, w, a, b are supported operations!')
        self.filePath = path
        self.file = open(path, mode)

    def write( self, txt: Union( [str, bytes] ) ) -> chainOpen:
        self.lastSuceeded = self.file.write(txt)
        return self
    
    def read( self, size ):
        return self, self.file.read(size)

    def writeLine(self, txt: str):
        self.writeline(txt)
        return self
            
    def close(self):
        self.file.close()

    def reopen(self, path: Union([Path, str]), mode='r'):
        if not (mode in ['r', 'x', 'w', 'a', 'b']):
            raise ValueError('only r, x, w, a, b are supported operations!')
        self.file = open(path, mode)
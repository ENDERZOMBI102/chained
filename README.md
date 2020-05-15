# chained
A python 3 library that provide chainable functions

| Modules |
|---------|
|[chainOpen](|



chainOpen
-
```python
>>> from chained import chainOpen
>>> chainOpen('C:/text.txt', 'x').write('hello ').write('world!').close().reopen('r').read().close('')
'hello world!'
```

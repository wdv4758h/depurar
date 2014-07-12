## @printc

print the function calls / return values / exceptions

example 1:

```python
from depurar import printc

@printc
def fib(num):
    if num <= 2:
        return 1
    return fib(num-1) + fib(num-2)

fib(5)
```

result 1:

```python
fib(5)
| fib(4)
| | fib(3)
| | | fib(2)
| | | fib(2) => 1
| | | fib(1)
| | | fib(1) => 1
| | fib(3) => 2
| | fib(2)
| | fib(2) => 1
| fib(4) => 3
| fib(3)
| | fib(2)
| | fib(2) => 1
| | fib(1)
| | fib(1) => 1
| fib(3) => 2
fib(5) => 5
```

example 2:

```python
# lru_cache can be used in Python 3.2+
from functools import lru_cache
from depurar import printc

@printc
@lru_cache(maxsize=32)
def fib(num):
    if num <= 2:
        return 1
    return fib(num-1) + fib(num-2)
```

result 2:

```
fib(5)
| fib(4)
| | fib(3)
| | | fib(2)
| | | fib(2) => 1
| | | fib(1)
| | | fib(1) => 1
| | fib(3) => 2
| | fib(2)
| | fib(2) => 1
| fib(4) => 3
| fib(3)
| fib(3) => 2
fib(5) => 5
```

example 3:

```python
from depurar import printc

@printc
def func(x, y):
    if y > 0:
        return x/y + func(x, y-1)
    else:
        return 0

@printc
def func2(x, y):
    try:
        value = func(x, y-1)
    except:
        value = func2(x-1, y)
    return value

func2(2, 3)
```

result 3:

```python
func2(2, 3)
| func(2, 2)
| | func(2, 1)
| | | func(2, 0)
| | | func(2, 0) => 0
| | func(2, 1) => 2.0
| func(2, 2) => 3.0
func2(2, 3) => 3.0
```

example 4:

```python
from depurar import printc

@printc
def func(x, y):
    if x > 0:
        return x/y + func(x, y-1)
    else:
        return 0

@printc
def func2(x, y):
    try:
        value = func(x, y-1)
    except:
        value = func2(x-1, y)
    return value

func2(2, 3)
```

result 4:

```python
func2(2, 3)
| func(2, 2)
| | func(2, 1)
| | | func(2, 0)
| | | >> division by zero
| | >> division by zero
| >> division by zero
| func2(1, 3)
| | func(1, 2)
| | | func(1, 1)
| | | | func(1, 0)
| | | | >> division by zero
| | | >> division by zero
| | >> division by zero
| | func2(0, 3)
| | | func(0, 2)
| | | func(0, 2) => 0
| | func2(0, 3) => 0
| func2(1, 3) => 0
func2(2, 3) => 0
```

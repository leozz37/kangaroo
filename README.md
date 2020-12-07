# Kangaroo Sockets 🦘

![Unit Tests](https://github.com/leozz37/kangaroo/workflows/Unit%20Tests/badge.svg)
[![codecov](https://codecov.io/gh/leozz37/kangaroo/branch/main/graph/badge.svg?token=9MbL9uMi8u)](https://codecov.io/gh/leozz37/kangaroo)
[![Maintainability](https://api.codeclimate.com/v1/badges/5b4ee1430037ca66735e/maintainability)](https://codeclimate.com/github/leozz37/kangaroo/maintainability)
[![Release](https://img.shields.io/github/v/release/leozz37/kangaroo)](https://github.com/leozz37/kangaroo/releases)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square)](https://github.com/pre-commit/pre-commit)
[![code style: black](https://img.shields.io/static/v1?label=code%20style&message=black&color=black&style=flat-square)](https://github.com/psf/black)
[![License](https://img.shields.io/github/license/pytransitions/transitions.svg)](LICENSE)

Kangaroo is a user-friendly lib for sockets in Python. You can send and listen to TCP sockets with a few lines of code.

## Contents

- [Installation](#installation)
- [Quick start](#quick-start)
- [Documentation](#documentation)
- [Examples](#examples)
- [Development](#development)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

First you need [Python](https://www.python.org/) installed (version 3.6+ is required), then you can install Kangaroo:

```shell
$ pip install kangaroo-sockets
```

Import it ib your code:

```Python
import Kangaroo
```

(Optional) install [Jaguar](https://github.com/leozz37/jaguar) for testing the sockets:

```shell
$ brew tap leozz37/jaguar

$ brew install jaguar
```

## Quick start

Sample code for sending and listening to a port:

```python
from src.kangaroo import Kangaroo
import threading
import time


def listen_port(port: int):
    r = Kangaroo().listen(port)

    while True:
        if r.has_new_message():
            print(r.get_message())


if __name__ == '__main__':
    x = threading.Thread(target=listen_port, args=(3000,))
    y = threading.Thread(target=listen_port, args=(3001,))

    x.start()
    y.start()

    while True:
        Kangaroo().send(3000, "Hello")
        Kangaroo().send(3001, "World")
        time.sleep(1)
```

## Documentation

The library consists on two features: listen and send to a given port. You can check the full documentation on pypi.

---

### Listen

Receives a **port** as `int` and returns a Kangaroo instance.

```python
def listen(self, port: int):
```

Usage example:

```python
kangaroo = Kangaroo()

r = kangaroo.listen(3000)
l = kangaroo.listen(3001)
```

---

### Send

Receives a **port** and a **message**, both as `string`.

```python
def send(self, port: int, message: str) -> None:
```

Usage example:

```python
kangaroo = Kangaroo()

r = kangaroo.listen(3000)
kangaroo.send(3000, "Hello, World!")
```

### Messages

`has_new_messages()` returns a `bool` if there's a new message:

```python
def has_new_message(self) -> bool:
```

`get_message()` returns the last message as `str`:

````python
def get_message(self) -> str:
````

Usage example:

````python
import Kangaroo


if __name__ == '__main__':
    kangaroo = Kangaroo()

    r = kangaroo.listen(3000)
    kangaroo.send(3000, "Hello world")

    if r.has_new_message():
        print(r.get_message())
````

## Development

This project uses **pipenv** and **pre-commit** in order to run some static
checks and formatting on the code. After clone the repository you need to create
a new **virtual environment** and install the dependencies:

```shell
$ pipenv shell

$ pipenv install --dev --skip-lock

$ pre-commit install
```

Every time you run the ```git commit``` command the code will be checked. To
run the checking manually, run:

```shell
$ pre-commit run --all-files
```

## Testing

The tests uses the pytest framework. To run the test suit with coverage you can do the following:

```shell
$ pytest --cov=. -v

============================================================================================================================ test session starts ============================================================================================================================
platform darwin -- Python 3.8.2, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- /Library/Developer/CommandLineTools/usr/bin/python3
cachedir: .pytest_cache
rootdir: /Users/leo/Documents/codes/kangaroo
plugins: cov-2.10.1
collected 4 items

tests/kangaroo_test.py::test_send_with_success PASSED                                                                                                                                                                                                                 [ 25%]
tests/kangaroo_test.py::test_listen_with_success PASSED                                                                                                                                                                                                               [ 50%]
tests/kangaroo_test.py::test_get_message_fails PASSED                                                                                                                                                                                                                 [ 75%]
tests/kangaroo_test.py::test_has_new_message_fails PASSED                                                                                                                                                                                                             [100%]

---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name                     Stmts   Miss  Cover
--------------------------------------------
__init__.py                  3      0   100%
setup.py                     4      4     0%
src/__init__.py              0      0   100%
src/kangaroo.py             31      0   100%
tests/__init__.py            0      0   100%
tests/kangaroo_test.py      23      0   100%
--------------------------------------------
TOTAL                       61      4    93%
```

## Contributing

A full guideline about contributing to Kangaroo can be found in the [CONTRIBUTING.md](./CONTRIBUTING.md) file.

## License

Hare is released under the [MIT License](./LICENSE).

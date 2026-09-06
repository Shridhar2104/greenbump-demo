# greenbump-demo

A small pydantic **v1** app whose test suite breaks when pydantic is bumped to
**v2** — and gets fixed by [greenbump](https://github.com/Shridhar2104/greenbump).

Look at the pull requests: a dependency bump turns the suite red, then a
greenbump commit migrates the source code (never the tests) and the suite goes
green again.

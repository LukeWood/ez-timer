# ez-timer
The easiest way to time a function call in Python.

## Installation
ez-timer can be installed from pypi:

```bash
pip install ez-timer
```

## Usage
Using ez-timer is simple:

```python
from ez_timer import ez_timer

with ez_timer() as timer:
  # run expensive computation
  time.sleep(1)

print(timer.result)
# > 1.0001
```

That's all.  That is the API.

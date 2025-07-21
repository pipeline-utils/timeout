# pipeline-utils-timeout

## install

```bash
pip install pipeline-utils-timeout
```

## usage

```python3
# case 1: should raise TimeoutException
@timeout_decorator(1)
def long_running_function():
    time.sleep(2)
```

```python3
# case 2: should raise TimeoutException
with timeout_manager(1):
    time.sleep(2)
```

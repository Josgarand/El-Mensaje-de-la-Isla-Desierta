# The Desert Island Message

This project provides a function to check whether a message can be formed using only the characters available in a chest. Spaces are ignored, and all characters are treated case-insensitively. No restrictions are applied regarding character types (e.g., accented characters or symbols are allowed).

## Requirements

This project was developed in **Python 3.13.1**, but it should work on earlier versions as it only uses the standard library.

No external dependencies are required.

## Usage examples

If you want to call the function from the same file, you can use a **print()** to see the result in the console:

```python
print(validateMessage("SOS", "DANGEROUSSOS"))
```

To add or edit tests, go to the tests folder and open the test.py file. There you will find a class that inherits from unittest.TestCase. Inside that class, you'll see functions that start with test_. and you can add them as in the example below.

```python
def test_example(self):
    self.assertTrue(validateMessage("SOS", "DANGEROUSSOS"))
    self.assertFalse(validateMessage("RESCUE", "RSCU"))
```

## How to run the tests

From the project root, you can run all the tests using the following command:

```bash
python -m unittest tests.test
```

You can also run a specific test by specifying the test class and method name:

```bash
python -m unittest tests.test.TestvalidateMessage.test_uppercase_handling
```
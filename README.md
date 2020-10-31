# spdx

A Github Action that verifies whether project files include a specified SPDX
license header.

If any files do not pass the ruleset for their file type, the test will fail
with some guidance about how to fix it.

## Usage

Include the action as part of a workflow that performs a checkout. You'll also
need to provide input:

- `licenses`: Extensions and valid SPDX headers for them. Provide a dictionary,
  with file types as the keys and accepted SPDX IDs in a list as the values.

Here's an example:

```yml
name: spdx

on:
  pull_request

jobs:
  check-spdx-headers:
    runs-on: ubuntu-latest
    steps:
    - name: checkout
      uses: actions/checkout@v2
    - uses: enarx/spdx@master
      with:
        extensions: >
          {
            'rs': ['Apache-2.0', 'MIT']
            'py': ['GPLv3']
          }
```

## Adding support for new file extensions

Rules for individual file types are defined with a dictionary in
[`extensions.py`](extensions.py). If the file type you'd like to check isn't
yet supported, feel free to add rules for it and submit a PR.

The file extension (for example, `py` for Python) should be a new key in the
dictionary. The value should be another dictionary, with the following key-value
pairs:

- `shebang`: A boolean indicating whether the first line of the file extension
  may be a shebang.
- `comment`: A list of acceptable comment starters for the file extension.

See [`extensions.py`](extensions.py) for examples.

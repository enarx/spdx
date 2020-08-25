# spdx

A Github Action that verifies whether project files include a specified SPDX
license header.

If any files do not pass the ruleset for their file type, the test will fail
with some guidance about how to fix it.

## Usage

Include the action as part of a workflow that performs a checkout. You'll also
need to provide the required inputs:

- `extensions`: Extensions to verify SPDX headers for. Provide a
  comma-separated list. For example: `rs, py`
- `license`: The SPDX license ID to check for. Example: `Apache-2.0`

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
        extensions: 'rs, py'
        license: 'Apache-2.0'
```

## Adding support for new file extensions

Rules for individual file types are defined with a function in `extensions.py`.
If the file type you'd like to check isn't yet supported, feel free to implement
a function for it and submit a PR.

Your new function should be named the same as the file extension, and should
accept two input fields:

- `file`: Path to the file to test.
- `license`: A string containing the SPDX license identifier to test for.

Your function should open the file and perform whatever logic is needed to
determine if the file has a valid SPDX header. If it does, return `True`. If it
doesn't, print an error message explaining where the SPDX header should be
placed, and return `False`.

See [extensions.py](extensions.py) for examples.

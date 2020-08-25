# SPDX-License-Identifier: Apache-2.0

import os

def rs(file, license):
    len_workspace = len(os.environ.get("GITHUB_WORKSPACE", None))
    try:
        f = open(file, 'r')
    except:
        print(f'File {file} cannot be opened.')
        return False
    with f:
        lines = f.readlines()

    # Check the first line of the file. If it matches, we're done. If not, print
    # an error message.
    match_string = f'// SPDX-License-Identifier: {license}'
    if lines[0].strip() != match_string.strip():
        print(f'''
    {file[len_workspace:]} does not include an SPDX license header of type {license}.

    Ensure that it has

    "// SPDX-License-Identifier: {license}"

    included on the first line of the file.
        ''')
        return False
    return True

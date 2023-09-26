# INI

This repository contains a [Vale-compatible][1] implementation of the 
guidelines created by the [Inclusive Naming Initiative][2].

## Repository Structure

### `INI`

The `INI` directory contains the actual Vale-compatible implementation of the
INI guidelines.

### `script`

The `script` directory contains a script that can be used to generate an 
approximate implementation of the INI guidelines from their actual JSON source.

Some details have been changed in the `INI` release directory to better 
accommodate the Vale CLI.

### `testdata`

The `testdata` directory contains a set of test cases that can be used to 
validate the INI implementation. Each subdirectory contains a set of test cases 
for a specific rule.

These tests are run automatically by the GitHub CI system (see 
`.github/workflows/test.yml`).

[1]: https://github.com/errata-ai/vale
[2]: https://inclusivenaming.org/
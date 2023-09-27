# INI

This repository contains a [Vale-compatible][1] implementation of the 
guidelines created by the [Inclusive Naming Initiative][2].

## Creating a Release

To create a new release, follow the steps outlined at 
[Managing releases in a repository][3].

The Vale package, `INI.zip`, will be uploaded automatically by the GitHub CI
workflow (`.github/workflows/release.yml`).

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
[3]: https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release
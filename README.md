# Lineosaurus

[![Run tests](https://github.com/Lineosaurus/Lineosaurus/actions/workflows/run-tests.yml/badge.svg)](https://github.com/Lineosaurus/Lineosaurus/actions/workflows/run-tests.yml)
[![License](https://img.shields.io/github/license/Lineosaurus/Lineosaurus)](https://github.com/Lineosaurus/Lineosaurus/blob/main/LICENSE)

🦕Make your card, show it on your GitHub profile readme, count lines of code, repository sizes, stargazers, character counts, and more across all your repositories, and share it with others!🦕

![lineosaurus](https://github.com/Lineosaurus/Lineosaurus/blob/main/assets/lineosaurus_h200.jpg?raw=true)


## Usage

> **Note**
Make sure you have README.md at the root of your repository.

Copy this file `.github/workflows/lineosaurus.yml` to your `github.com/<YOUR_USERNAME>/<YOUR_USERNAME>` repository.

```yaml
name: Lineosaurus

on:
  schedule:
    - cron: '0 0 * * *'  # Runs daily
  workflow_dispatch:     # Update manually via 'Actions' tab

jobs:
  run:
    runs-on: ubuntu-latest
    permissions:
      contents: write  # For committing
    steps:
      - uses: Lineosaurus/Lineosaurus@v1
        env:
          GH_TOKEN: ${{ github.token }}  # For GitHub CLI
        with:

          ## required ##

          git-name: your name
          git-email: your@email

          ## options ##

          only-type: null
          ignore-type: null
          header: null
          footer: null
          custom-title: |-
            ### Over _LINESROUND_ lines of code stretch through _OWNER_'s repositories.

            ### *updated on _DATE_*
          num-shown: 3
          show-approx: true
          card-titles: |
            - line: #### Lines of code
            - type: #### Languages
            - star: #### Stargazers
            - stat: #### _OWNER_'s statistics
          card-order: |
            - line
            - type
            - star
            - stat
          prefer-extension: true
          auto-line-break: true
          show-credit: true
```

### Options

option             | description | default | example
---                | ---         | ---     | ---
`only-type`        | count only specific file type | `null` | `'[".py", ".js"]'`
`ignore-type`      | ignore specific file type (this option is ignored if `only-type` is used) | `null` | `'[".py", ".js"]'`
`header`           | set extra stuff above the cards (text/path) | `null` | `relative/path/to/header.md`
`footer`           | set extra stuff below the cards (text/path) | `null` | `## This is a footer`
`custom-title`     | special text above the top card | `null` | `## _OWNER_'s stats`
`num-shown`        | number of items for each card | `3` | 
`show-approx`      | will be using `13K` instead of `13,241` | `true` |
`card-titles`      | set special titles for specific cards | `null` | `'{"line": "foo", "stat": "bar"}'`
`card-order`       | choose and arrange the cards | `null` | `'["line", "stat"]'`
`prefer-extension` | will be using `.py` over `Python` | `true` | 
`auto-line-break`  | auto next line after header/footer/etc ends | `true` | 
`show-credit`      | show credit at the end of the file | `true` | 

[more options...](https://github.com/Lineosaurus/Lineosaurus)

### Variables

These variables can be used inside `header`, `custom-title`, `card-titles`, and `footer`.

variable        | description | example
---             | ---         | ---
`_OWNER_`       | your GitHub username | `Lineosaurus`
`_DATE_`        | today's date | `Aug 1, 2023`
`_LINES_`       | total lines of code across all repositories (regardless only-type/ignore-type) | `123456`
`_LINESFMT_`    | formatted `_LINES_` | `123,456`
`_LINESAPPROX_` | formatted `_LINES_` | `123.5K`
`_LINESROUND_`  | formatted `_LINES_` | `120,000`
`_LINE_`        | total lines of code across all repositories (following only-type/ignore-type) | `3141`
`_LINEFMT_`  | formatted `_LINE_` | `3,141`
`_LINEAPPROX_`  | formatted `_LINE_` | `3.1K`
`_LINEROUND_`   | formatted `_LINE_` | `3,100`
`_VER_`         | Lineosaurus version | `1.23`

[more variables...](https://github.com/Lineosaurus/Lineosaurus)

## Pick your flavors

Or, for a bit of variety, you can explore these ready-made cards. Take a look and choose your favorite!

```yaml
name: Lineosaurus

on:
  schedule:
    - cron: '0 0 * * *'  # Runs daily
  workflow_dispatch:     # Update manually via 'Actions' tab

jobs:
  run:
    runs-on: ubuntu-latest
    permissions:
      contents: write  # For committing
    steps:
      - uses: Lineosaurus/Lineosaurus@v1
        env:
          GH_TOKEN: ${{ github.token }}  # For GitHub CLI
        with:

          ## required ##

          git-name: your name
          git-email: your@email

          ## options ##

          flavor: <FLAVOR> by <CREATOR>
```

### flavors

- [Wondering](https://github.com/Lineosaurus/Lineosaurus/tree/main/flavors/Lineosaurus/Wondering) by [Lineosaurus](https://github.com/Lineosaurus/Lineosaurus):

  ```yml
  flavor: Wondering by Lineosaurus
  ```

- [friends](https://github.com/Lineosaurus/Lineosaurus/tree/main/flavors/Lineosaurus/friends) by [Lineosaurus](https://github.com/Lineosaurus/Lineosaurus):

  ```yml
  flavor: friends by Lineosaurus
  ```

- [miniature](https://github.com/Lineosaurus/Lineosaurus/tree/main/flavors/nvfp/miniature) by [nvfp](https://github.com/nvfp):

  ```yml
  flavor: miniature by nvfp
  ingredients: |
    - banner-path: ./assets/banner.png  # relative to your repo root dir  (optional)
    - banner-alt : example-repo-banner  # image alt text                  (optional)
  ```

[more flavors...](https://github.com/Lineosaurus/Lineosaurus)


## Contributing

Lineosaurus welcomes and appreciates contributions. All contributions will be reviewed, please explain what changes you've made and the effects.


## License

The scripts and documentation in this project are released under the [MIT License](https://github.com/Lineosaurus/Lineosaurus/blob/main/LICENSE).
# 🦕🦕 Line*osaurus* 🦕🦕

[![Run tests](https://github.com/Lineosaurus/Lineosaurus/actions/workflows/run-tests.yml/badge.svg)](https://github.com/Lineosaurus/Lineosaurus/actions/workflows/run-tests.yml)

Count GitHub repo stats, like the number of lines of code across all your GitHub repos.

## Usage

First copy this file `.github/workflows/lineosaurus.yml`:

```yml
name: Lineosaurus
on: { schedule: [{ cron: '0 0 * * *' }], workflow_dispatch: null }
jobs:
  run:
    runs-on: ubuntu-latest
    permissions: { contents: write }  # for committing
    steps:
      - uses: Lineosaurus/Lineosaurus@v5
        env:
          GH_TOKEN: ${{ github.token }}  # for GitHub CLI
        with:
          nickname: Foo bar
          gitname: your Git name
          gitemail: your Git email
```

Next, change the option values.

Learn more about the [options here](https://github.com/Lineosaurus/Lineosaurus/blob/main/action.yml).

> Note: The latest version is recommended

That's it! it will update once a day! 🎉

## Notes

- Make sure you already have `README.md` at the root of your `github.com/NAME/NAME` repository.

## License

MIT License.

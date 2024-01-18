# 🦕🦕 Line*osaurus* 🦕🦕

[![Run tests](https://github.com/Lineosaurus/Lineosaurus/actions/workflows/run-tests.yml/badge.svg)](https://github.com/Lineosaurus/Lineosaurus/actions/workflows/run-tests.yml)

Count your GitHub repo stats, like the total number of lines of code and characters across all your GitHub repositories. Also, show the latest repo that you've worked on for the last time!

## Usage

Great, want to show your GitHub stats? let's first copy this file:

`.github/workflows/lineosaurus.yml`:

```yml
name: Lineosaurus
on: { schedule: [{ cron: '0 0 * * *' }], workflow_dispatch: null }
jobs:
  run:
    runs-on: ubuntu-latest
    permissions: { contents: write }  # for committing
    steps:
      - uses: Lineosaurus/Lineosaurus@...  # EDITME: choose the version you prefer, the latest version is recommended.
        env:
          GH_TOKEN: ${{ github.token }}  # for GitHub CLI
        with:  # v EDIT THESE v
          nickname: Foo bar
          banner: ./relpath/to/the/image.jpg  # can also be .png/.jpeg/etc. that supported by GitHub
          include_last_activity: true
          gitname: your Git name    # for committing the changes (required)
          gitemail: your Git email  # for committing the changes (required)
          credit: false
```

Second, change the value marked with "EDITME" to yours. Also, it's okay to change the file name too, it has no effect.

Learn more about [params' desc here](https://github.com/Lineosaurus/Lineosaurus/blob/main/action.yml).

And that's it! it will update your README.md once a day with your GitHub stats.

## Notes

- Make sure you already have `README.md` at the root of your `github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY>` repository.

## License

[MIT License](https://en.wikipedia.org/wiki/MIT_License). Everyone is welcome to change, reuse, contribute, sell, share, etc. the code.

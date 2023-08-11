## miniature

Usage:

```yml
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

          flavor: miniature by nvfp
          ingredients: |
              - banner-path: ./assets/banner.png  # relative to your repo root dir  (optional)
              - banner-alt : example-repo-banner  # image alt text                  (optional)
```
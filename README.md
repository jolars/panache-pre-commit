# panache-pre-commit

[![CI](https://github.com/jolars/panache-pre-commit/actions/workflows/ci.yml/badge.svg)](https://github.com/jolars/panache-pre-commit/actions/workflows/ci.yml)

[pre-commit](https://pre-commit.com) hooks for
[panache](https://github.com/jolars/panache), a formatter and linter for Quarto,
Pandoc, and Markdown.

This repository is a thin shim. The hooks themselves are implemented in the main
[`jolars/panache`](https://github.com/jolars/panache) repository; this repo
exists so that `pre-commit autoupdate` resolves to panache's actual release
versions (`vX.Y.Z`) rather than to unrelated tags from sub-packages that share
the main repo (`panache-code-vX.Y.Z`, `panache-formatter-vX.Y.Z`,
`panache-parser-vX.Y.Z`).

## Usage

Add to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/jolars/panache-pre-commit
    rev: v3.3.0  # use `pre-commit autoupdate` to bump
    hooks:
      - id: panache-format
      - id: panache-lint
```

## Hooks

- `panache-format` --- format Quarto, Pandoc, and Markdown files
- `panache-lint` --- lint Quarto, Pandoc, and Markdown files

Both hooks install panache from PyPI (the `panache-cli` wheel, which ships the
`panache` binary) into pre-commit's managed virtualenv.

## Versioning

Tags here mirror panache releases: installing at tag `vX.Y.Z` gives you panache
X.Y.Z. New tags are created automatically when a new panache version is
published to PyPI.

## Migrating from `jolars/panache`

If your `.pre-commit-config.yaml` currently points at
`https://github.com/jolars/panache`, update the `repo:` URL to
`https://github.com/jolars/panache-pre-commit` and run `pre-commit autoupdate`.

## License

MIT

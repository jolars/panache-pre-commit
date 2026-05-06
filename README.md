# panache-pre-commit

[pre-commit](https://pre-commit.com) hooks for
[panache](https://github.com/jolars/panache), a formatter and linter for
Quarto, Pandoc, and Markdown.

This repository is a thin shim. The hooks themselves are implemented in the
main [`jolars/panache`](https://github.com/jolars/panache) repository; this
repo exists so that `pre-commit autoupdate` resolves to panache's actual
release versions (`vX.Y.Z`) rather than to unrelated tags from sub-packages
that share the main repo (`panache-code-vX.Y.Z`,
`panache-formatter-vX.Y.Z`, `panache-parser-vX.Y.Z`).

## Usage

Add to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/jolars/panache-pre-commit
    rev: v2.43.1  # use `pre-commit autoupdate` to bump
    hooks:
      - id: panache-format
      - id: panache-lint
```

## Hooks

- `panache-format` — format Quarto, Pandoc, and Markdown files
- `panache-lint` — lint Quarto, Pandoc, and Markdown files

Both hooks install panache from npm and run it via Node.

## Versioning

Tags here mirror panache's main release tags (`vX.Y.Z`). They are not
guaranteed to land at the exact moment a panache release ships, but they
should follow within a short window.

## Migrating from `jolars/panache`

If your `.pre-commit-config.yaml` currently points at
`https://github.com/jolars/panache`, update the `repo:` URL to
`https://github.com/jolars/panache-pre-commit` and run
`pre-commit autoupdate`.

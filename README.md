# 🌹 The Hatchlor 🌹 Cookiecutter Template

<div align="center">
<img src="https://raw.githubusercontent.com/FlorianWilhelm/the-hatchlor/master/images/logo.svg" alt="The Hatchlor logo" width="300" role="img">
</div>

|         |                                    |
|---------|------------------------------------|
| Details | [![Tests][Tests-image]][Tests-link] [![License - MIT][MIT-image]][MIT-link] [![GitHub Sponsors][sponsor-image]][sponsor-link] |
| Features | [![Hatch project][hatch-image]][hatch-link] [![linting - Ruff][ruff-image]][ruff-link] [![types - mypy][mypy-image]][mypy-link] [![test - pytest][pytest-image]][pytest-link]  [![Pre-Commit][precommit-image]][precommit-link] [![docs - mkdocs][mkdocs-image]][mkdocs-link] |

The Hatchlor is a [cookiecutter] template featuring the modern and extensible Python project manager [hatch] 🐣.

With hatch, you no longer need to deal with files like `requirements.txt`, `Pipfile` or `environment.yml`,
just configure everything in `pyproject.toml`. Thus, hatch is a sophisticated alternative to [pipenv], [poetry], [conda], or
direct [virtualenv] usage. Just think of hatch as a tool that allows you to easily define many isolated development environments,
e.g. virtual but also docker environments, and helps you to manage them. A bit like what [tox] does for testing environments but
for all kinds of environments, e.g. testing, linting your code, buildings your docs, and whatever you want.

Check out a [vanilla Python project] created by the Hatchlor.

## ✨ Features

The Hatchlor integrates the following features:

* [hatch]: Python packaging, environment management and test runner,
* [hatch-vcs]: determine the package version automatically from git tags, e.g. `v0.9`,
* [hatch-pip-compile]: support for lock-files,
* [pyproject.toml]: all package, build and tool configuration in one file,
* [pytest]: full-featured Python testing tool that helps you write better programs,
* [coverage]: tool for measuring code coverage of Python programs with pytest integration,
* [GitHub Actions]: workflows with [dependabot], [release-drafter], [labeler], build docs, test & publish to PyPI,
* [ruff]: extremely fast Python linter/formatter, which replaces [isort], [flake8], [black], etc.,
* [mypy]: optional static type checker for Python,
* [mkdocs]: a fast, simple and downright gorgeous static site generator,
* [pre-commit]: pre-commit git hooks that make your life easier,
* [Markdown]: instead of reStructuredText, Markdown is used consistently for all text files,
* [EditorConfig]: maintain consistent coding styles for multiple developers,
* [src-layout]: the actual Python package is kept under a `src` folder avoiding many common errors.

Please note additional integrations and following amendments:

* [semantic-release]: local prepare of a commit: create changelog and commit with a version tag
* [bump-my-version] and [generate-changelog]: alternative to [semantic-release]
* [gitlint]: include linting of commit messages
* [GitHub Actions]: reworked workflows - dump context, add test publishing on TestPy, switch to new PyPi mechanism

The amendments support a local development and commit process while "outsourcing" testing for different OS
and with  different Python versions to GitHub.
The local committing includes preparation of a changelog. It is based on semantic-versioning.
Commit-messages are linted to enforce commit messages according to conventional commits format as
basis for a proper and automatically generated changelog.

The template includes a `skeleton.py` with a simple function `fib` that calculates the Fibonacci numbers
as demonstration. This is tested with `tests/test_skeleton.py` to demonstrate the corresponding features
from above. As an additional tidbit, `skeleton.py` also features [Typer] to show how `fib` can be
exposed as a CLI command. These files are only for demonstration and can be safely deleted.

## 💫 Quickstart

Install the latest [cookiecutter], i.e. >= 1.4, if not installed:

```console
pip install -U cookiecutter
```

Then generate your Python project with:

```console
cookiecutter https://github.com/florianwilhelm/the-hatchlor.git
```

🎉 That's  it! Now change into the created directory and check out [`README.md`] for more information.

## 🪪 License

The Hatchlor is distributed under the terms of the [MIT license](LICENSE.txt).

## 🙏 Credits

To start this project off a lot of inspiration was taken from [hatch], [cookiecutter-pypackage] and [Pyscaffold].

[cookiecutter]: https://cookiecutter.readthedocs.io/
[tox]: https://tox.wiki/
[hatch]: https://hatch.pypa.io/
[hatch-vcs]: https://github.com/ofek/hatch-vcs
[hatch-pip-compile]: https://github.com/juftin/hatch-pip-compile
[cookiecutter-pypackage]: https://github.com/audreyfeldroy/cookiecutter-pypackage
[Pyscaffold]: https://pyscaffold.org/
[pre-commit]: https://pre-commit.com/
[mkdocs]: https://www.mkdocs.org/
[Markdown]: https://www.markdownguide.org/
[src-layout]: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
[flake8]: https://pypi.org/project/flake8/
[isort]: https://pycqa.github.io/isort/
[pytest]: https://docs.pytest.org/
[coverage]: https://coverage.readthedocs.io/
[mypy]: https://mypy-lang.org/
[black]: https://black.readthedocs.io/
[ruff]: https://beta.ruff.rs/
[EditorConfig]: http://editorconfig.org/
[Typer]: https://typer.tiangolo.com/
[pyproject.toml]: https://hatch.pypa.io/latest/config/metadata/
[pipenv]: https://pipenv.pypa.io/
[poetry]: https://python-poetry.org/
[conda]: https://docs.conda.io/
[virtualenv]: https://virtualenv.pypa.io/
[vanilla Python project]: https://github.com/FlorianWilhelm/the-hatchlor-demo
[`README.md`]: https://github.com/FlorianWilhelm/the-hatchlor-demo
[GitHub Actions]: https://docs.github.com/en/actions
[labeler]: https://github.com/marketplace/actions/github-labeler
[dependabot]: https://docs.github.com/en/code-security/dependabot
[release-drafter]: https://github.com/marketplace/actions/release-drafter

[Tests-image]: https://github.com/FlorianWilhelm/the-hatchlor/actions/workflows/run-tests.yml/badge.svg?branch=main
[Tests-link]: https://github.com/FlorianWilhelm/the-hatchlor/actions/workflows/run-tests.yml
[hatch-image]: https://img.shields.io/badge/%F0%9F%A5%9A-hatch-4051b5.svg
[hatch-link]: https://github.com/pypa/hatch
[ruff-image]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[ruff-link]: https://github.com/charliermarsh/ruff
[mypy-image]: https://img.shields.io/badge/Types-mypy-blue.svg
[mypy-link]: https://mypy-lang.org/
[pytest-image]: https://img.shields.io/static/v1?label=‎&message=Pytest&logo=Pytest&color=0A9EDC&logoColor=white
[pytest-link]:  https://docs.pytest.org/
[mkdocs-image]: https://img.shields.io/static/v1?label=‎&message=mkdocs&logo=Material+for+MkDocs&color=526CFE&logoColor=white
[mkdocs-link]: https://www.mkdocs.org/
[precommit-image]: https://img.shields.io/static/v1?label=‎&message=pre-commit&logo=pre-commit&color=76877c
[precommit-link]: https://pre-commit.com/
[MIT-image]: https://img.shields.io/badge/License-MIT-9400d3.svg
[MIT-link]: LICENSE.txt
[sponsor-image]: https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=ff69b4
[sponsor-link]: https://github.com/sponsors/FlorianWilhelm

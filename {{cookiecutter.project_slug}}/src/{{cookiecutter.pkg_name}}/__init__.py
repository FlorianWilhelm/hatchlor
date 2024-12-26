# version determination


# original Hatchlor version
# from importlib.metadata import PackageNotFoundError, version
# try:
#     __version__ = version('{{ cookiecutter.project_slug }}')
# except PackageNotFoundError:  # pragma: no cover
#     __version__ = 'unknown'
# finally:
#     del version, PackageNotFoundError

# modified version for editable mode installs (if desired
# up-to-date version tag for modules installed in editable mode inspired by
# https://github.com/maresb/hatch-vcs-footgun-example/blob/main/hatch_vcs_footgun_example/__init__.py
# Define the variable '__version__':
# try:
#
#     # own developed alternative variant to hatch-vcs-footgun overcoming problem of ignored setuptools_scm settings
#     # from hatch-based pyproject.toml libraries
#     from hatch.cli import hatch
#     from click.testing import CliRunner
#     # determine version via hatch
#     __version__ = CliRunner().invoke(hatch, ["version"]).output.strip()
#
# except (ImportError, LookupError):
#     # As a fallback, use the version that is hard-coded in the file.
#     try:
#         from ._version import __version__  # noqa: F401
#     except ModuleNotFoundError:
#         # The user is probably trying to run this without having installed the
#         # package, so complain.
#         raise RuntimeError(
#             f"Package {__package__} is not correctly installed. Please install it with pip."
#         )

# simplified version to avoid evaluation of metadata and additional dependencies
# version file is generated during Hatch build process
try:
    from ._version import __version__  # noqa: F401
except ModuleNotFoundError:
    # The user is probably trying to run this without having installed the
    # package, so complain.
    raise RuntimeError(
        f"Package {__package__} is not correctly installed. Please install it with pip."
    )

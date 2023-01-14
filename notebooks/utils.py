"""Utility functions for the workshop."""

from packaging.version import Version
import datetime as dt
import importlib
import json
import os
import sys
import yaml


_OK = '\x1b[42m[ OK ]\x1b[0m'
_FAIL = '\x1b[41m[FAIL]\x1b[0m'

def _print_version_ok(item):
    """Print an OK message for version check."""
    print(_OK, '%s' % item)

def _print_version_failure(item, req_version, version):
    """Print a failure message for version check."""
    if version:
        msg = '%s version %s is required, but %s installed.'
        values = (item, req_version, version)
    else:
        msg = '%s is not installed.'
        values = item
    print(_FAIL, msg % values)

def run_env_check():
    """Check that the packages we need are installed and the Python version is correct."""
    # read in the environment file and process versions
    with open('../environment.yml', 'r') as file:
        env = yaml.safe_load(file)

    requirements = {}
    for req in env['dependencies']:
        pkg, version = req.split('=')
        if '-' in pkg:
            continue
        requirements[pkg.split('::')[-1]] = version

    # check the python version
    python_version = sys.version_info
    required_version = requirements.pop('python')
    for component, value in zip(['major', 'minor', 'micro'], required_version.split('.')):
        if getattr(python_version, component) != int(value):
            print(f'Using Python at {sys.prefix}:\n-> {sys.version}')
            _print_version_failure(
                'Python',
                required_version,
                f'{python_version.major}.{python_version.minor}'
            )
            break
    else:
        _print_version_ok('Python')

    for pkg, req_version in requirements.items():
        try:
            mod = importlib.import_module(pkg)
            if req_version:
                version = mod.__version__
                if Version(version).base_version != Version(req_version).base_version:
                    _print_version_failure(pkg, req_version, version)
                    continue
            _print_version_ok(pkg)
        except ImportError:
            if pkg == 'ffmpeg':
                try:
                    pkg_info = json.loads(os.popen('conda list -f ffmpeg --json').read())[0]
                    if pkg_info:
                        if pkg_info['version'] != req_version:
                            _print_version_failure(pkg, req_version, pkg_info['version'])
                            continue
                        _print_version_ok(pkg)
                        continue
                except IndexError:
                    pass
            _print_version_failure(pkg, req_version, None)

def despine(ax):
    """Hide the top and right spines on a Matplotlib Axes object."""
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    return ax

def mpl_svg_config(hashsalt):
    """Help configure the SVG backend for Matplotlib and make it reproducible."""
    from matplotlib import rc
    rc('svg', hashsalt=hashsalt)

    return {
        'metadata': {
            'Date': f'(c) 2021-{dt.date.today().year} Stefanie Molin'
        }
    }

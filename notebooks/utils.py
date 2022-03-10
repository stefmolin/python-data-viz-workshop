"""Utility functions for the workshop."""

from packaging.version import LegacyVersion as Version
import importlib
import json
import os
import sys
import yaml


OK = '\x1b[42m[ OK ]\x1b[0m'
FAIL = '\x1b[41m[FAIL]\x1b[0m'


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
    print('Using Python in %s:' % sys.prefix)
    python_version = sys.version_info
    required_version = requirements.pop('python')
    for component, value in zip(['major', 'minor', 'micro'], required_version.split('.')):
        if getattr(python_version, component) != int(value):
            print(FAIL, 'Python version %s is required, but %s is installed.\n' % (required_version, sys.version))
            break
    else:
        print(OK, 'Python is version %s\n' % sys.version)

    # check the requirements
    for pkg, req_version in requirements.items():
        try:
            mod = importlib.import_module(pkg)
            if req_version:
                version = mod.__version__
                if Version(version) != Version(req_version):
                    print(FAIL, '%s version %s is required, but %s installed.' % (pkg, req_version, version))
                    continue
            print(OK, '%s' % pkg)
        except ImportError:
            if pkg == 'ffmpeg':
                try:
                    pkg_info = json.loads(os.popen('conda list -f ffmpeg --json').read())[0]
                    if pkg_info:
                        if pkg_info['version'] != req_version:
                            print(
                                FAIL, 
                                '%s version %s is required, but %s installed.' % (pkg, req_version, pkg_info['version'])
                            )
                            continue
                        print(OK, '%s' % pkg)
                        continue
                except IndexError:
                    pass
            print(FAIL, '%s not installed.' % pkg)

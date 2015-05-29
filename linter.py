#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Gavin Elster
# Copyright (c) 2015 Gavin Elster
#
# License: MIT
#

"""This module exports the SlimLint plugin class."""

from SublimeLinter.lint import RubyLinter


class SlimLint(RubyLinter):

    """Provides an interface to slim-lint."""

    defaults = {
        'bundle-exec': False
    }

    syntax = 'ruby slim'
    executable = 'slim-lint'
    tempfile_suffix = '-'
    config_file = ('--config', '.slim-lint.yml', '~')

    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = ' >= 0.4.0'

    regex = (
        r'^.+?:(?P<line>\d+) '
        r'(?:(?P<error>\[E\])|(?P<warning>\[W\])) '
        r'(?P<message>[^`]*(?:`(?P<near>.+?)`)?.*)'
    )

    def cmd(self):
        """Dynamically generate the command line that is executed in order to lint."""

        if self.get_view_settings().get('bundle-exec'):
            return ('bundle', 'exec', self.executable)

        return (self.executable_path)

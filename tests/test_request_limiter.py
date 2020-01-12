#!/usr/bin/env python

"""Tests for `request_limiter` package."""


import unittest
from click.testing import CliRunner

from request_limiter import request_limiter
from request_limiter import cli


class TestRequest_limiter(unittest.TestCase):
    """Tests for `request_limiter` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'request_limiter.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

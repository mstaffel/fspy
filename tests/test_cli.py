#!/usr/bin/env python

"""Tests for `cli` package."""

import pytest
from fspy import FileSystem
from fspy import handle_crud


@pytest.fixture
def small_sys() -> FileSystem:
    small_system = FileSystem()
    small_system.make_directory("school")
    small_system.move_up_one_directory("school")
    return small_system


def test_small_cli(capsys, small_sys):
    split_response = ["get", "working", "directory"]
    handle_crud(split_response, small_sys)
    assert capsys.readouterr().out == "/school/\n"

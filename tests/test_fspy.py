#!/usr/bin/env python

"""Tests for `fspy` package."""

import pytest
from fspy import FileSystem


@pytest.fixture
def empty_sys() -> FileSystem:
    empty_system = FileSystem()
    return empty_system


def test_empty_sys(empty_sys):
    assert empty_sys is not None


@pytest.fixture
def small_sys() -> FileSystem:
    small_system = FileSystem()
    small_system.make_directory("school")
    return small_system


def test_small(small_sys):
    assert small_sys is not None
    small_sys.move_up_one_directory("school")
    assert small_sys.current_directory.name == "school"
    assert small_sys.current_directory.path == "/school/"
    small_sys.move_to_parent()


def test_small_file(small_sys):
    assert small_sys.current_directory.path == "/"
    small_sys.make_file("test.txt")
    current_dir_contents = list(small_sys.current_directory.children.keys())
    assert current_dir_contents == ["school", "test.txt"]
    small_sys.delete_file("test.txt")
    current_dir_contents = list(small_sys.current_directory.children.keys())
    assert current_dir_contents == ["school"]
    assert small_sys.current_directory.path == "/"


def test_small_file_write(small_sys):
    small_sys.make_file("test.txt")
    small_sys.write_to_file("test.txt", "Test Info")
    contents = small_sys.read_from_file("test.txt")
    assert(contents == "Test Info")
    small_sys.delete_file("test.txt")


# Leave this fixture as you found it please
@pytest.fixture
def med_sys() -> FileSystem:
    med_system = FileSystem()
    med_system.make_directory("school")
    med_system.move_up_one_directory("school")
    med_system.make_directory("homework")
    med_system.move_up_one_directory("homework")
    med_system.make_directory("math")
    med_system.make_directory("lunch")
    med_system.make_directory("history")
    med_system.make_directory("spanish")
    med_system.move_to_parent()
    med_system.move_to_parent()
    return med_system


def test_med_contents(med_sys):
    assert med_sys is not None
    assert med_sys.current_directory.path == "/"
    med_sys.move_up_one_directory("school")
    assert med_sys.current_directory.path == "/school/"
    med_sys.move_up_one_directory("homework")
    assert med_sys.current_directory.path == "/school/homework/"
    current_dir_contents = set(med_sys.current_directory.children.keys())
    assert current_dir_contents == set(["history", "lunch", "math", "spanish"])
    med_sys.move_to_parent()
    med_sys.move_to_parent()
    assert med_sys.current_directory.path == "/"


def test_med_delete(med_sys):
    assert med_sys.current_directory.path == "/"
    med_sys.move_up_one_directory("school")
    assert med_sys.current_directory.path == "/school/"
    med_sys.make_directory("cheatsheet")
    current_dir_contents = list(med_sys.current_directory.children.keys())
    assert current_dir_contents == ["homework", "cheatsheet"]
    med_sys.delete_directory("cheatsheet")
    current_dir_contents = list(med_sys.current_directory.children.keys())
    assert current_dir_contents == ["homework"]
    med_sys.move_to_parent()
    assert med_sys.current_directory.path == "/"


def test_med_search(med_sys):
    node_list = med_sys.find_fs_node("school")
    assert node_list == ["/school/"]
    node_list = med_sys.find_fs_node("history")
    assert node_list == ["/school/homework/history/"]
    med_sys.make_directory("history")
    correct_path_set = set(["/history/",
                            "/school/homework/history/"])
    node_list = med_sys.find_fs_node("history")
    assert correct_path_set == set(node_list)
    med_sys.move_up_one_directory("school")
    correct_path_set = set(["/school/homework/history/"])
    node_list = med_sys.find_fs_node("history")
    assert correct_path_set == set(node_list)
    med_sys.move_to_parent()
    med_sys.delete_directory("history")

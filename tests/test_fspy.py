#!/usr/bin/env python

"""Tests for `fspy` package."""

import pytest


from fspy import FSNode


@pytest.fixture
def single_node_maker() -> FSNode:
    resp = FSNode("apples")
    return resp
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(single_node_maker):
    assert single_node_maker.name is not None
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

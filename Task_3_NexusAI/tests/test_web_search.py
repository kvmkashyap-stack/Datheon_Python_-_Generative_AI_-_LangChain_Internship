from unittest.mock import patch
import pytest
from tools.web_search import web_search

def test_rejects_empty_query():
    with pytest.raises(ValueError):
        web_search("  ")


def test_rejects_long_query():
    with pytest.raises(ValueError):
        web_search("a" * 501)


@patch("tools.web_search.DDGS")
def test_formats_search_results(mock_ddgs):
    mock_ddgs.return_value.text.return_value = [
        {
            "title": "Python Official Website",
            "body": "Python is a programming language.",
            "href": "https://www.python.org/",
        }
    ]

    result = web_search("Python programming")

    assert "Python Official Website" in result
    assert "Python is a programming language." in result
    assert "https://www.python.org/" in result


@patch("tools.web_search.DDGS")
def test_handles_no_results(mock_ddgs):
    mock_ddgs.return_value.text.return_value = []

    result = web_search("some obscure query")

    assert "No search results" in result


@patch("tools.web_search.DDGS")
def test_handles_search_failure(mock_ddgs):
    mock_ddgs.return_value.text.side_effect = RuntimeError("Connection failed")

    result = web_search("Python")

    assert "Web search failed" in result
    assert "Connection failed" in result

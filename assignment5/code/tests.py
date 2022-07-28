import requesting_urls as request
import pytest


def test_find_urls():
    html = """
    <a id="some-id" href="/relative/path#fragment">relative link</a>
    <a href="#fragment -only">anchor link</a>
    <a href="//other.host/same-protocol">same-protocol link</a>
    <a href="https://example.com">absolute URL</a>
    """

    base_url = 'en.wikipedia.org'
    print('dot')

    urls = find_urls(html, base_url=base_url, output='testtest.txt')

    assert urls == [
        "https://en.wikipedia.org/relative/path",
        "https://other.host/same-protocol",
        "https://example.com",
    ]


def test_find_articles():
    html = """
    <a id="some-id" href="/relative/path#fragment">relative link</a>
    <a href="#fragment -only">anchor link</a>
    <a href="//other.host/same-protocol">same-protocol link</a>
    <a href="https://example.com">absolute URL</a>
    """

    base_url = 'en.wikipedia.org'

    urls = find_articles(html, base_url=base_url, output='testtest.txt')

    assert urls == [
        "https://en.wikipedia.org/relative/path"
    ]

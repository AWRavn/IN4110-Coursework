import re
from requesting_urls import *
import os

def find_urls(html, base_url=None, output=None):
    """
    Returns list of urls found in a html page.

    Args:
        html (string):          Website html code.
        base_url (string):      Optional. Base website url for partial urls. Default None.
        output (string):        Optional. Name of the output file. Default None.

    Returns:
        url_list (list[string]):List of cleaned urls.

    """

    # Find all <a href="..." ...> snippets and get text contained in href strings
    a_pattern = re.compile(r"<a[^>]+>", flags=re.IGNORECASE)
    href_pattern = re.compile(r'(?<=href=")(.*?)(?=")')

    url_list = []
    for a in a_pattern.findall(html):
        for href in href_pattern.findall(a):
            url = clean_url(href, base_url)

            # Append if viable after cleaning
            if url!='':
                url_list.append(url)

    # Remove duplicates
    url_list=list(dict.fromkeys(url_list))

    # Create directory if needed
    os.makedirs('../filter_urls', exist_ok=True)

    # Save output to file
    if output!=None:
        report = open("../filter_urls/" + output, "w")
        for u in url_list:
            report.write('{}\n'.format(u))
        report.close()

    return url_list


def clean_url(url, base_url=None):
    """
    Cleans up the provided url link by reformatting partial urls and removing trailing fragment identiiers.

    Args:
        url (string)            Website url.
        base_url (string):      Optional. Base website url for partial urls. Default None.

    Returns:
        url (string):           Cleaned website url.
    """

    # Adjust formatting of partial urls
    if url[0:8]!='https://':
        if url[0:2]=='//':
            url = 'https:' + url
        elif url[0]=='/' and url[1]!='/':
            if base_url!=None:
                url = 'https://' + base_url + url
            else:
                raise ValueError("base_url can't be None for url format: {}".format(url))

    # Remove fragment identifiers
    url = url.split("#")[0]

    # Remove articles with a colon
    if ':' in url[9:]:
        url=''

    return url


def find_articles(html, base_url=None, output=None):
    """
    Returns list of urls found in a html page that lead to wikipedia articles.

    Args:
        html (string):          Website html code.
        base_url (string):      Optional. Base website url for partial urls. Default None.
        output (string):        Optional. Name of the output file. Default None.

    Returns:
        url_list (list[string]):List of cleaned urls.

    """

    urls = find_urls(html, base_url)

    # Filter out wikipedia articles
    url_list = [url for url in urls if 'wikipedia.org' in url]

    # Create directory if needed
    os.makedirs('../filter_urls', exist_ok=True)

    # Save output to file
    if output!=None:
        report = open("../filter_urls/" + output, "w")
        for u in url_list:
            report.write('{}\n'.format(u))
        report.close()

    return url_list


def main():
    """
    Create output files for test webpages.
    """

    urls=['https://en.wikipedia.org/wiki/Nobel_Prize',
        'https://en.wikipedia.org/wiki/Bundesliga',
        'https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup']
    names=['nobelprize', 'bundesliga', 'alpineskiworldcup']
    base_url = 'en.wikipedia.org'

    for i in range(len(urls)):
        html = get_html(urls[i], output=names[i] + '.txt')
        find_urls(html , base_url=base_url, output='find_urls_' + names[i] + '.txt')
        find_articles(html , base_url=base_url, output='find_articles_' + names[i] + '.txt')


if __name__ == '__main__':
    main()

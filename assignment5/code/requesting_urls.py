import requests as req
import os

def get_html(url, parameters=None, output=None):
    """
    Returns html of a given website.

    Args:
        url (string):           Website url
        parameters (dict):      Optional. A dictionary, list of tuples or byttes to send as  aquery string.
                                Default None.
        output (string):        Optional. Name of the output file. Default None.

    Return:
        html.text (string):     Content of the response in unicode.

    """

    html = req.get(url, params=parameters)

    # Create directory if needed
    os.makedirs('../requesting_urls/', exist_ok=True)

    # Save output to file
    if output!=None:
        report = open("../requesting_urls/" + output, "w")
        report.write('url: {}\n'.format(html.url))
        report.write(html.text)
        report.close()

    return html.text


def main():
    """
    Create output files for test webpages.
    """

    urls=['https://en.wikipedia.org/wiki/Studio_Ghibli',
        'https://en.wikipedia.org/wiki/Star_Wars']
    names=['studioghibli', 'starwars']

    for i in range(len(urls)):
        get_html(urls[i], output=names[i] + '.txt')
        get_html(urls[i], output=names[i] + '.txt')

    url_with_params='https://en.wikipedia.org/w/index.php'
    params={'title': 'Main_Page', 'action': 'info'}

    get_html(url_with_params, parameters=params, output='index.txt')


if __name__ == '__main__':
    main()

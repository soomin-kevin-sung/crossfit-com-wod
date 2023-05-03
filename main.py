import os
import datetime as dt
import crawlingtools
import githubtools

# crossfit.com main url
crossfit_com_url = "https://www.crossfit.com/"
access_token = os.environ['ACCESS_TOKEN']
repository_name = 'crossfit-com-wod'


def main():
    """
    main of program
    """

    # Get WOD Contents.
    now = dt.datetime.now()
    date_string = now.strftime("%y%m%d")
    soup = crawlingtools.get_beautifulsoup(f'{crossfit_com_url}{date_string}')

    # Cannot Load WOD Page.
    if soup is None:
        # Parse WOD contents and title.
        wod_contents = f"[ERROR] Cannot load WOD {date_string}"
        wod_title = f"[ERROR] Cannot load WOD {date_string}"
    else:
        # Parse WOD contents and title.
        wod_contents = crawlingtools.extract_wod_contents(soup)
        wod_title = crawlingtools.extract_date_title(soup)

    # Open Repository Issue.
    repo = githubtools.get_repo(access_token, repository_name)
    githubtools.create_issue(repo, wod_title, wod_contents)


if __name__ == '__main__':
    main()

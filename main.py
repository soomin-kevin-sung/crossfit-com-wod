import os
import datetime as dt
import crawlingtools
import githubtools

# crossfit.com main url
crossfit_com_url = "https://www.crossfit.com/"
access_token = os.environ['ACESS_TOKEN']
repository_name = 'crossfit-com-wod'


def main():
    """
    main of program
    """

    # Get WOD Contents.
    now = dt.datetime.now()
    soup = crawlingtools.get_beautifulsoup(f'{crossfit_com_url}/{now.strftime("%y%m%d")}')
    wod_contents = crawlingtools.extract_wod_contents(soup)

    # Open Repository Issue.
    repo = githubtools.get_repo(access_token, repository_name)
    githubtools.create_issue(repo, 'test', wod_contents)


if __name__ == '__main__':
    main()

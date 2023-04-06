from github import Github


def get_repo(access_token, repo_name):
    """
    Get repository by access_token, repository_name.
    :param access_token:
    :param repo_name:
    :return: The Repository [github.Repository]
    """
    github = Github(access_token)
    return github.get_user().get_repo(repo_name)


def create_issue(repo, title, body):
    """
    Create issue at repo.
    :param repo: repository to open issue.
    :param title: issue's title.
    :param body: issus's body
    :return: None
    """
    repo.create_issue(title, body)

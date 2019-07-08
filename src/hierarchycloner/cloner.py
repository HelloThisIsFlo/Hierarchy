import git

from src.hierarchycloner.hierarchy import RepoToClone


def clone_all(repo_hierarchy: [RepoToClone]):
    for repo in repo_hierarchy:
        git.Repo.clone_from(url=repo.url, to_path=repo.path)

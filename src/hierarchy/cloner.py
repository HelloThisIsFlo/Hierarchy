import git

from hierarchy.loader import RepoToClone
from hierarchy.utils import display


def clone_all(repo_hierarchy: [RepoToClone]):
    for repo in repo_hierarchy:
        display(f"Cloning '{repo.url}' in '{repo.path}'")
        display('')

        git.Repo.clone_from(url=repo.url, to_path=repo.path)

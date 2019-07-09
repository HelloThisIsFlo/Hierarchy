import click
import git

from hierarchy.hierarchy import RepoToClone


def clone_all(repo_hierarchy: [RepoToClone]):
    for repo in repo_hierarchy:
        click.echo(f"Cloning '{repo.url}' in '{repo.path}'")
        click.echo('')

        git.Repo.clone_from(url=repo.url, to_path=repo.path)

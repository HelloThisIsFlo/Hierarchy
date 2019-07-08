import click
import git

from src.hierarchycloner.hierarchy import RepoToClone


def clone_all(repo_hierarchy: [RepoToClone]):
    for repo in repo_hierarchy:
        full_path = repo.path / repo.name

        click.echo('')
        click.echo(f"Cloning '{repo.url}' in '{full_path}'")

        git.Repo.clone_from(url=repo.url, to_path=full_path)

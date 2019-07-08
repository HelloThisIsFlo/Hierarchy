from pathlib import Path
from unittest import mock
from unittest.mock import call

from git import Repo

from src.hierarchycloner import cloner
from src.hierarchycloner.hierarchy import RepoToClone


@mock.patch.object(Repo, 'clone_from')
def test_clone_repo_with_gitpython(clone_from):
    hierarchy = [RepoToClone(url='git@github.com:FlorianKempenich/Hierarchy-Cloner.git',
                             root_path=Path('/this/is/a/path'),
                             name='hc'),
                 RepoToClone(url='git@github.com:FlorianKempenich/kata.git',
                             root_path=Path('/some/other/path'),
                             name='kata')]

    cloner.clone_all(hierarchy)

    clone_from.assert_has_calls(
            [call(url='git@github.com:FlorianKempenich/Hierarchy-Cloner.git', to_path=Path('/this/is/a/path/hc')),
             call(url='git@github.com:FlorianKempenich/kata.git', to_path=Path('/some/other/path/kata'))],
            any_order=True)


@mock.patch.object(Repo, 'clone_from')
@mock.patch('click.echo')
def test_log_each_repo_cloned_via_click(click_echo, _clone_from):
    hierarchy = [RepoToClone(url='git@github.com:FlorianKempenich/Hierarchy-Cloner.git',
                             root_path=Path('/this/is/a/path'),
                             name='hc'),
                 RepoToClone(url='git@github.com:FlorianKempenich/kata.git',
                             root_path=Path('/some/other/path'),
                             name='kata')]

    cloner.clone_all(hierarchy)

    click_echo.assert_has_calls(
            [call("Cloning 'git@github.com:FlorianKempenich/Hierarchy-Cloner.git' in '/this/is/a/path/hc'"),
             call("Cloning 'git@github.com:FlorianKempenich/kata.git' in '/some/other/path/kata'")],
            any_order=True)

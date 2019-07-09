from pathlib import Path
from unittest import mock
from unittest.mock import call

from git import Repo

from hierarchy import cloner
from hierarchy.loader import RepoToClone


@mock.patch.object(Repo, 'clone_from')
def test_clone_repo_with_gitpython(clone_from):
    hierarchy = [RepoToClone(url='git@github.com:FlorianKempenich/Hierarchy.git',
                             root_path=Path('/this/is/a/path'),
                             name='hc'),
                 RepoToClone(url='git@github.com:FlorianKempenich/kata.git',
                             root_path=Path('/some/other/path'),
                             name='kata')]

    cloner.clone_all(hierarchy)

    clone_from.assert_has_calls(
            [call(url='git@github.com:FlorianKempenich/Hierarchy.git', to_path=Path('/this/is/a/path/hc')),
             call(url='git@github.com:FlorianKempenich/kata.git', to_path=Path('/some/other/path/kata'))],
            any_order=True)


@mock.patch.object(Repo, 'clone_from')
@mock.patch('hierarchy.cloner.display')
def test_log_each_repo_cloned_via_click(display, _clone_from):
    hierarchy = [RepoToClone(url='git@github.com:FlorianKempenich/Hierarchy.git',
                             root_path=Path('/this/is/a/path'),
                             name='hc'),
                 RepoToClone(url='git@github.com:FlorianKempenich/kata.git',
                             root_path=Path('/some/other/path'),
                             name='kata')]

    cloner.clone_all(hierarchy)

    display.assert_has_calls(
            [call("Cloning 'git@github.com:FlorianKempenich/Hierarchy.git' in '/this/is/a/path/hc'"),
             call("Cloning 'git@github.com:FlorianKempenich/kata.git' in '/some/other/path/kata'")],
            any_order=True)

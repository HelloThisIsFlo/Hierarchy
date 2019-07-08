from pathlib import Path
from unittest import mock
from unittest.mock import call

from git import Repo

from src.hierarchycloner import cloner
from src.hierarchycloner.hierarchy import RepoToClone


@mock.patch.object(Repo, 'clone_from')
def test_clone_repo_with_gitpython(clone_from):
    hierarchy = [RepoToClone(url='git@github.com:FlorianKempenich/Hierarchy-Cloner.git',
                             path=Path('/this/is/a/path'),
                             name='hc'),
                 RepoToClone(url='git@github.com:FlorianKempenich/kata.git',
                             path=Path('/some/other/path'),
                             name='kata')]

    cloner.clone_all(hierarchy)

    clone_from.assert_has_calls(
            [call(url='git@github.com:FlorianKempenich/Hierarchy-Cloner.git', to_path=Path('/this/is/a/path')),
             call(url='git@github.com:FlorianKempenich/kata.git', to_path=Path('/some/other/path'))],
            any_order=True)

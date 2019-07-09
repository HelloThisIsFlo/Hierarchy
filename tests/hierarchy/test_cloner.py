from pathlib import Path
from unittest import mock
from unittest.mock import call

from callee import Contains
from git import Repo, GitCommandError

from hierarchy import cloner
from hierarchy.loader import RepoToClone

MOCK_HIERARCHY = [RepoToClone(url='git@github.com:FlorianKempenich/Hierarchy.git',
                              root_path=Path('/this/is/a/path')),
                  RepoToClone(url='git@github.com:FlorianKempenich/kata.git',
                              root_path=Path('/some/other/path'),
                              name='kata')]


@mock.patch.object(Repo, 'clone_from')
def test_clone_repo_with_gitpython(clone_from):
    hierarchy = MOCK_HIERARCHY

    cloner.clone_all(hierarchy)

    clone_from.assert_has_calls(
            [call(url='git@github.com:FlorianKempenich/Hierarchy.git', to_path=Path('/this/is/a/path/Hierarchy')),
             call(url='git@github.com:FlorianKempenich/kata.git', to_path=Path('/some/other/path/kata'))],
            any_order=True)


@mock.patch.object(Repo, 'clone_from')
@mock.patch('hierarchy.cloner.display')
def test_log_each_repo_cloned_via_click(display, _clone_from):
    hierarchy = MOCK_HIERARCHY

    cloner.clone_all(hierarchy)

    display.assert_has_calls(
            [call("Cloning 'git@github.com:FlorianKempenich/Hierarchy.git' in '/this/is/a/path/Hierarchy'"),
             call("Cloning 'git@github.com:FlorianKempenich/kata.git' in '/some/other/path/kata'")],
            any_order=True)


@mock.patch.object(Repo, 'clone_from')
@mock.patch('hierarchy.cloner.display')
def test_error_while_cloning_skip(display, clone_from):
    error = GitCommandError(command='git clone etc ....', status=218)

    def raise_error_only_for_hierachy_project(*args, url=None, **kwargs):
        if 'Hierarchy' in url:
            raise error

    hierarchy = MOCK_HIERARCHY
    clone_from.side_effect = raise_error_only_for_hierachy_project

    cloner.clone_all(hierarchy)

    # THEN
    # - Error message was displayed
    display.assert_any_call(Contains('Hierarchy'), variant='ERROR', reason=error)
    # - But next repo is still processed
    clone_from.assert_called_with(url='git@github.com:FlorianKempenich/kata.git', to_path=mock.ANY)

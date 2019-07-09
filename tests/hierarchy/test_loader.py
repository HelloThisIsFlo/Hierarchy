from pathlib import Path

import pytest
from pytest import fixture

from hierarchy import loader
from hierarchy.loader import RepoToClone


@fixture
def tmp_file(tmp_path):
    return tmp_path / 'tmp_file.yaml'


class TestLoadHierarchy:
    def test_file_does_not_exist__raise(self):
        doesnt_exist = Path('/does/not/exist')
        assert not doesnt_exist.exists()

        with pytest.raises(ValueError, match=r'File .* does not exist!') as e:
            loader.load_from_file(doesnt_exist)

    def test_file_empty__raise(self, tmp_file):
        tmp_file.write_text('''
        ''')

        with pytest.raises(ValueError, match='Invalid Hierarchy') as e:
            loader.load_from_file(tmp_file)

    def test_file_invalid__raise(self, tmp_file):
        tmp_file.write_text('''
        { 'this': is not yaml}
        ''')

        with pytest.raises(ValueError, match='Invalid Hierarchy') as e:
            loader.load_from_file(tmp_file)

    def test_file_invalid_2__raise(self, tmp_file):
        tmp_file.write_text('''
        - path: '/this/is/a/path'
          name: hc
        ''')

        with pytest.raises(ValueError, match='Invalid Hierarchy') as e:
            loader.load_from_file(tmp_file)

    def test_valid_hierarchy(self, tmp_file: Path):
        tmp_file.write_text('''
        - url: 'git@github.com:FlorianKempenich/Hierarchy.git'
          path: '/this/is/a/path'
          name: hc
          
        - url: 'git@github.com:FlorianKempenich/kata.git'
          path: '/some/other/path'
          name: kata
        ''')

        repos = loader.load_from_file(tmp_file)

        assert repos == [
                RepoToClone(url='git@github.com:FlorianKempenich/Hierarchy.git',
                            root_path=Path('/this/is/a/path'),
                            name='hc'),
                RepoToClone(url='git@github.com:FlorianKempenich/kata.git',
                            root_path=Path('/some/other/path'),
                            name='kata')]

    def test_no_explicit_name__extract_from_url(self, tmp_file):
        tmp_file.write_text('''
        - url: 'git@github.com:FlorianKempenich/Hierarchy.git'
          path: '/this/is/a/path'
        ''')

        repos = loader.load_from_file(tmp_file)

        assert repos[0].path == Path('/this/is/a/path/Hierarchy')

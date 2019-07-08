from pathlib import Path

import yaml


class RepoToClone:
    url: str
    path: Path
    name: str

    def __init__(self, url: str, path: Path, name: str = None):
        self.url = url
        self.path = path
        if name:
            self.name = name
        else:
            self.name = self._extract_name_from_url()

    def _extract_name_from_url(self):
        return self.url.split('/')[-1].replace('.git', '')

    def __repr__(self) -> str:
        return f'<url: {self.url} | path: {self.path} | name: {self.name}>'

    def __eq__(self, other):
        return self.url == other.url and self.path == other.path and self.name == other.name


def load_from_file(hierarchy_file: Path):
    if not hierarchy_file.exists():
        raise ValueError('File does not exist!')

    hierarchy_yaml = yaml.safe_load(hierarchy_file.read_text())

    hierarchy = []
    for repo_yaml in hierarchy_yaml:
        if 'url' not in repo_yaml or 'path' not in repo_yaml:
            raise ValueError('Invalid Hierarchy. Please check Hierarchy file!')

        repo_to_clone = RepoToClone(repo_yaml['url'], Path(repo_yaml['path']), repo_yaml.get('name'))
        hierarchy.append(repo_to_clone)

    return hierarchy

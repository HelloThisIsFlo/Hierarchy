import os
from pathlib import Path

from git import Repo


def main():
    # repo = Repo('git@github.com:FlorianKempenich/Front-End-Sandbox.git')

    sandbox_dir = Path('../sandbox')
    # repo = Repo.clone_from(url='git@github.com:FlorianKempenich/The-Tiny-Mindblows-Log.git', to_path=sandbox_dir)

    home = Path(os.path.expanduser('~'))
    print(os.listdir(home))



    # print(os.listdir(sandbox_dir))
    # repo =

    # print(repo)

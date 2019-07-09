# Hierarchy
[![Travis](https://img.shields.io/travis/FlorianKempenich/hierarchy.svg)](https://travis-ci.org/FlorianKempenich/hierarchy) [![PyPI](https://img.shields.io/pypi/v/hierarchy.svg)](https://pypi.org/project/hierarchy/)

Hierarchy is a simple tool that allows you to clone and maintain an entire hierarchy of Git repository in _one single command_:
```
$ hierarchy
```
> TODO: Add picture of `hierarchy` in action

## Quick-Start

1. **Install**
   ```bash
   $ pip install hierarchy
   ```

2. **Create the _Hierarchy_ file**
   ```bash
   $ nano ~/.hierarchy
   ```

   > _Sample Hierarchy File_
   > ```yaml
   > - url: 'git@github.com:FlorianKempenich/Hierarchy.git'
   >   path: '~/Dev/Tools'
   >   
   > - url: 'git@github.com:FlorianKempenich/kata.git'
   >   path: '/Some/Other/Location'
   >   name: kata-cli
   > ```

3. **Run _Hierarchy_**
   ```bash
   $ hierarchy
   ```

## _Hierarchy_ file structure

The _Hierarchy_ file represent the flat hierarchy of all the git repository to clone and automatically maintain. 

It consists of a list of entries, each representing a repository to clone.  Each repository has the following structure:
```yaml
url: "URL of the project. The same used to clone the repository with `git clone`"
path: "The local path where to clone the repository. It can contain `~` to represent HOME"
name: "OPTIONAL - A name to override the default repository name when cloning"
```

**The repository will be cloned at:** `path/name`  
If no `name` is provided, the repository name will be used.


A sample _Hierarchy_ file might look like this:
```yaml
- url: 'git@github.com:FlorianKempenich/Hierarchy.git'
  path: '~/Dev/Tools'
  
- url: 'git@github.com:FlorianKempenich/kata.git'
  path: '/Some/Other/Location'
  name: kata-cli
```

## Options

* ### `-f` / `--file HIERARCHY_FILE`
  A hierarchy file to use.  
  _Default:_ `~/.hierarchy`



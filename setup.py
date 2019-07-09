from setuptools import find_packages, setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='hierarchy',
      version='0.1.2',
      description='Clone and Maintain an entire hierarchy of Git repositories in one command',
      long_description=readme(),
      keywords='git batch',
      classifiers=[
              'Environment :: Console',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: MIT License',
              'Topic :: Utilities'
      ],
      url='https://github.com/FlorianKempenich/Hierarchy',
      author='Florian Kempenich',
      author_email='Flori@nKempenich.com',
      packages=find_packages(where="src"),
      package_dir={"": "src"},
      license='MIT',
      scripts=['bin/hierarchy'],
      install_requires=[
              'click',
              'gitpython',
              'pyyaml'
      ],
      include_package_data=True)

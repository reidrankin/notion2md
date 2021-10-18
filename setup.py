from setuptools import find_packages, setup
import setuptools
import io
# Read in the README for the long description on PyPI
def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(
      name='notion2md',
      version='2.0',
      description='Export notion page to markdown using official notion api',
      long_description=long_description(),
      long_description_content_type="text/markdown",
      url='https://github.com/echo724/notion2md.git',
      author='echo724',
      author_email='eunchan1001@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(include=['notion2md']),
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          'Programming Language :: Python :: 3.9',
          ],
)

from setuptools import setup, find_packages

import re, io, os

class getPackageInfo:
    def __init__(self):
        self._package_name = self.__getPackageNameFromProject()
        self._long_Description = self.__getLongDescription()
        self._description = self.__getDescription()
        self._package_main_file = self.__getPacketInitFileContent()
        self._version = self.__getVersion()
        self._author = self.__getAuthor()
        self._author_email = self.__getAuthorEmail()


    def __getPackageNameFromProject(self):
        for dir in next(os.walk(".\src"))[1]:
            if not ".egg-info" in str(dir):
                return dir

    def __getLongDescription(self):
        with open("README.md", "r", encoding="utf-8") as fh:
            return  fh.read()

    def __getDescription(self):
        return re.search(
                r'(?<=\"\"\")((.|\n)*)(?=\"\"\")', 
                self._package_main_file
            ).group(1)

    def __getPacketInitFileContent(self):
        return io.open(
                os.path.join('src', self.package_name,'__init__.py'),
                encoding='utf_8_sig'
            ).read()

    def __getVersion(self):
        return re.search(
            r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
            self._package_main_file
        ).group(1)

    def __getAuthor(self):
        return re.search(
            r'__author__\s*=\s*[\'"]([^\'"]*)[\'"]',
            self._package_main_file
        ).group(1)

    def __getAuthorEmail(self):
        return re.search(
                r'__email__\s*=\s*[\'"]([^\'"]*)[\'"]',
                self._package_main_file
            ).group(1)

    @property
    def package_name(self):
        return self._package_name

    @property
    def long_descroption(self):
        return self._long_Description

    @property
    def description(self):
        return self._description

    @property
    def version(self):
        return self._version

    @property
    def author(self):
        return self._author

    @property
    def author_email(self):
        return self._author_email


PACKAGE_INFO = getPackageInfo()

setup(
    name = "example-package-robert-rijnbeek",
    version = PACKAGE_INFO.version,
    author = PACKAGE_INFO.author ,
    author_email = PACKAGE_INFO.author_email ,
    description = "Robert rijnbeek test package!!",
    long_description = PACKAGE_INFO.long_descroption,
    long_description_content_type = "text/markdown",
    url = "https://github.com/R-Rijnbeek/robert_rijnbeek_test_package",
    project_urls = {
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = { "": "src"},
    packages = find_packages(where = "src"),
    python_requires = ">=3.6",
)
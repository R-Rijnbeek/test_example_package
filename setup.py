from setuptools import setup, find_packages

import re, io, os

class getPackageInfo:
    def __init__(self):
        self._package_name = self.__getPackageNameFromProject()
        self._package_main_file = self.__getPacketInitFileContent()
        self._git_config_file = self.getconfigGIT()
        self._long_description = self.__getLongDescription()
        self._description = self.__getDescription()
        self._version = self.__getVersion()
        self._author = self.__getAuthor()
        self._author_email = self.__getAuthorEmail()
        self._git_host = self.__getGITHost()
        self._git_issues_host = self.__getGITIssuesHost()


    def __getPackageNameFromProject(self):
        for dir in next(os.walk(".\src"))[1]:
            if not ".egg-info" in str(dir):
                return dir


    def __getLongDescription(self):
        with open("README.md", "r", encoding="utf-8") as fh:
            return  fh.read()

    def __getPacketInitFileContent(self):
        return io.open(
                os.path.join('src', self.package_name,'__init__.py'),
                encoding='utf_8_sig'
            ).read()

    def getconfigGIT():
        with open(os.path.join(".git","config"), "r", encoding="utf-8") as fh:
            return  fh.read()

    def __getDescription(self):
        return re.search(
                r'(?<=\"\"\")((.|\n)*)(?=\"\"\")', 
                self._package_main_file
            ).group(1)

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

    def __getGITHost(self):
        return re.search(
                r'(?<=\[remote "origin"\]\n\turl = )((.|\n)*)(?=\.git)',
                self._git_config_file
            ).group(1)

    def __getGITIssuesHost(self):
        return self._git_host + "/issues"

    @property
    def package_name(self):
        return self._package_name

    @property
    def long_description(self):
        return self._long_description

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

    @property
    def git_host(self):
        return self._git_host

    @property
    def git_issues_host(self):
        return self._git_issues_host


PACKAGE_INFO = getPackageInfo()

setup(
    name = "example-package-robert-rijnbeek",
    version = PACKAGE_INFO.version,
    author = PACKAGE_INFO.author ,
    author_email = PACKAGE_INFO.author_email ,
    description = PACKAGE_INFO.description,
    long_description = PACKAGE_INFO.long_description,
    long_description_content_type = "text/markdown",
    url = PACKAGE_INFO.git_host,
    project_urls = {
        "Bug Tracker": PACKAGE_INFO.git_issues_host,
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


import re, io, os
class getPackageInfo:
    def __init__(self):
        self._package_module_name = None
        self._package_main_file = None
        self._git_config_file = None
        self._long_description = None
        self._description = None
        self._version = None
        self._author = None
        self._author_email = None
        self._git_host = None
        self._package_name = None
        self._git_issues_host = None
        self.Process()
    
    def Process(self):
        self.__getPackageModuleNameFromProject()
        self.__getPacketInitFileContent()
        self.__getconfigGIT()
        self.__getLongDescription()
        self.__getDescription()
        self.__getVersion()
        self.__getAuthor()
        self.__getAuthorEmail()
        self.__getGITHost()
        self.__getPackageName()
        self.__getGITIssuesHost()

    def __getPackageModuleNameFromProject(self):
        for dir in next(os.walk(".\src"))[1]:
            if not ".egg-info" in str(dir):
                self._package_module_name = dir
                return True

    def __getLongDescription(self):
        with open("README.md", "r", encoding="utf-8") as fh:
            self._long_description = fh.read()
            return  True

    def __getPacketInitFileContent(self):
        self._package_main_file = io.open(
                os.path.join('src', self._package_module_name,'__init__.py'),
                encoding='utf_8_sig'
            ).read()
        return True

    def __getconfigGIT(self):
        with open(os.path.join(os.getcwd(), '.git', 'config'), "r", encoding="utf-8") as fh:
            self._git_config_file = fh.read()
            return  True

    def __getDescription(self):
        self._description = re.search(
                r'(?<=\"\"\")((.|\n)*)(?=\"\"\")', 
                self._package_main_file
            ).group(1)
        return True

    def __getVersion(self):
        self._version = re.search(
            r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
            self._package_main_file
        ).group(1)
        return True

    def __getAuthor(self):
        self._author = re.search(
            r'__author__\s*=\s*[\'"]([^\'"]*)[\'"]',
            self._package_main_file
        ).group(1)
        return True
    
    def __getAuthorEmail(self):
        self._author_email = re.search(
                r'__email__\s*=\s*[\'"]([^\'"]*)[\'"]',
                self._package_main_file
            ).group(1)
        return True

    def __getGITHost(self):
        self._git_host = re.search(
                r'(?<=\[remote "origin"\]\n\turl = )((.|\n)*)(?=\.git)',
                self._git_config_file
            ).group(1)
        return True

    def __getGITIssuesHost(self):
        self._git_issues_host = self._git_host + "/issues"
        return True

    def __getPackageName(self):
        self._package_name = self._git_host.rsplit('/', 1)[-1]
        return True

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



print(PACKAGE_INFO.version)
print(PACKAGE_INFO.author )
print(PACKAGE_INFO.author_email )
print(PACKAGE_INFO.description)
print(PACKAGE_INFO.long_description)

print(PACKAGE_INFO.git_host)

print(PACKAGE_INFO.git_issues_host)

print(PACKAGE_INFO.package_name)

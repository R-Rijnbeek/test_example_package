# <REPOSITORY_NAME>

The function of this test package template is to make it easier to build and deploy new packages on https://pypi.org/ 
It does not pretend to fit the demadnd of all type of packages but make some steps easier to fullfit using this package as template. And afther importing the repository. Adapt is for each usecase.

## Instalation protocol
1. Use the content of this repository in your own git/github environment. With your own repository name and self builded package content

2. Clone the github repository.
````
$ git clone https://github.com/<GITHUB_USERNAME>/<REPOSITORY_NAME>.git
````
3. Enter the project folder.
````
$ cd <REPOSITORY_NAME>
````
## how deploy package on pipy

1. Before execute the deploy command. There must be prerequisites:
    * It the ``__init__.py`` Ther must be defined: 
        * ``__doc__`` description of the module information insite """ .... """ on the header of the docuemnt
        * An defined release version of the package ``__version__`` 
        * An defined author of the package ``__author__``
        * An defined author email of the package ``__email__``
    * If there are pip dependencies that the package need to have installed to work. They must be listed on the 'requirement.txt' file.
    * The Project need to be part of an "git" environment connected to an github repository. If it is part of it. Some information is used as metadata of the pip project. Such as:
        * The package name will be the repository name of the project
        * The webside will be directly the github repository.
        * The bugtracker web will be the issues part of the repoitory on github.
    * There must be an defined ``README.md`` on the root of the project.

    **If this information is not correct. The build process wil be interupted and the deploy will not happen**

2. You must be registered on https://pypi.org/ with a defined "username" and "password"

3. Execute the command:
`````
$ deploy.bat 
`````

* This command will create and temporary virtual environment. Install the requirement packages on it. Build the new release. And deploy it on https://pypi.org/ (will ask username and password) and as last will destroy the builded virtual environment asking if you will delete it or not. 

Now you have deployed your package on PIPY so you can use it with PIP installations

## How to test it (on VSCode):

1. Change ``<YOUR_PACKAGE_NAME>`` your your deployed package name inside ``build.bat`` (on the last line)
````
...
python -m venv env
call .\env\Scripts\activate
pip install <YOUR_PACKAGE_NAME>
````

2. Build the virtual environment on the repository with the package content by running:
````
$ build.bat
````
3. After that you can use method located in the tests directory .\\tests\\__init__.py
````
$ cd tests
$ python __init__.py
````
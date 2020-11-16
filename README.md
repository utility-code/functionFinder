Function Finder
-------


An efficient Python library to help you to visually keep track fo your functions and classes
It aims to make easier to work with those libraries with so many files that one usually
loses track of where which function or class comes from


Example Usage
-------------
> This also takes Jupyter notebooks into account

    import functionvis
    functionvis.mainrunner()


In case you want to change the output on a specific format

    import functionvis
    functionvis.mainrunner(".", "svg")

You can also specify the path

    import functionvis
    functionvis.mainrunner("path-to-dir", "svg")

Install
-------

The latest stable version can always be installed or updated via [pip](https://pypi.org/project/functionvis/):



    $ pip install functionvis

Make sure to also install the requirements (Pathlib, graphviz, jupytext):

    $ pip install graphviz==0.14.2
    $ Pip install jupytext==1.6.0
    $ pip install pathlib

If the above fails for graphviz (If you have linux you can get it from apt/aur ; For windows install it from their site)   

For conda users:

    conda create --name <NAME_OF_THE_ENV> python=3.6
    pip install functionvis
    Pip install jupytext==1.6.0
    Pip install fire
    conda install graphviz python-graphviz


Supports
-------

- .py (Normal python file)
- .ipynb (If you have it for python that is)


 Outputs
 -------

(Find them in your project directory as classes.png and functions.png)

 - Functions
![](./classes.png)

 - Modules
 ![](./functions.png)

supported Outputs format
-------

| Format        | Suported (tested)      |
| ------------- |:-------------:|
| pdf           | YES           |
| png           | YES           |  
| svg           | YES           |
| jpg           | YES           |
| gif           | YES           |


ToDo + Contributions
-------
 - Other languages such as Julia/C/Java etc.
 - Contributions welcome
 - Bugs will be squashed if you tell me what they are

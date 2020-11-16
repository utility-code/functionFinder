# Function Finder 
 -----

 - This is now on pypi!!! [Link](https://pypi.org/project/functionvis/)

 - Every found a library with so many files you lose track of which function/class comes from where?
 - What if you could see it visually :o
 
 I keep facing this problem everytime and I decided to act on it once and for all.

## Supports

- .py (Normal python file)
- .ipynb (If you have it for python that is)

## How to run

 - Do a pip install functionvis
 - Get requirements (Pathlib, graphviz, jupytext)
 - Install graphviz (If you have linux you can get it from apt/aur ; For windows install it from their site)
 - python
 - ```py
    import functionvis
    functionvis.mainrunner()
    ```
> This also takes Jupyter notebooks into account

 ## Outputs

(Find them in your project directory as classes.png and functions.png)

 - Functions
![](./classes.png)
 
 - Modules
 ![](./functions.png)
 
## Contribution Rules
- Contributions are welcome :)
- If you want to add support for a new language/add specific functions, use the testing branch.
- Be sure to add a proper explanation with each commit. 
- Keep your commits short. I cannot go through 100 lines of change at once
- Radical idea? Amazing!! Put it as an issue first
- Suggestion? Add it as an issue / drop a PR
- Did I miss something? Let me know.

## ToDo
 
 - Other languages such as Julia/C/Java etc.
 - Bugs will be squashed if you tell me what they are

# Function Finder 
 -----
 
 - Every found a library with so many files you lose track of which function/class comes from where?
 - What if you could see it visually :o
 > Note: this will only work with python files (for now atleast)
 
 I keep facing this problem everytime and I decided to act on it once and for all.
 
 ## How to run
 
 - Get requirements (Pathlib, graphviz)
 ```
 pip install -r requirements.txt
 ```
 - Just invoke the main.py file with the argument as the directory which you want to visualize
 - eg:
 ```py
 python main.py -d "Your directory path"
 ```
 - Arguments (Default is True. Change only if you want False)
   - -f Generate for Functions
   - -c Generate for Classes
   - ef:
   ```py
    python main.py -fc -d "../datafly/" 
   ```
 
 ## Outputs

(Find them in your project directory as classes.png and functions.png)

 - Functions
! [](./classes.png)
 
 - Modules
 ![](./functions.png)
 
 ## ToDo + Contributions
 
 - Other languages such as Julia/C/Java etc.
 - Contributions welcome
 - Bugs will be squashed if you tell me what they are

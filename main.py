#!/usr/bin/env python3

from pathlib import Path
import argparse
import ast
from graphviz import Digraph

opt = argparse.ArgumentParser("Function grapher")
opt.add_argument("-d", "--dir", help="Enter directory")
opt.add_argument(
    "-f", type=bool, help="Generate for functions. True by default", default=True)
opt.add_argument(
    "-c", type=bool, help="Generate for classes. True by default", default=True)
opt.add_argument(
    "-fo", help="Format to save. Default pdf. Choose between svg/pdf/png etc.", default="png")
args = opt.parse_args()


def top_level_functions(body):
    return (f for f in body if isinstance(f, ast.FunctionDef))


def top_level_classes(body):
    return (f for f in body if isinstance(f, ast.ClassDef))


def get_all_functions(filename):
    with open(str(filename), 'r') as f:
        temp = ast.parse(f.read())
        classes = [func.name for func in top_level_classes(temp.body)]
        functions = [func.name for func in top_level_functions(temp.body)]
        return {"classes": classes, "functions": functions}


def get_files(file_path):
    print("[INFO] Creating list of files")
    all_files = Path(file_path)
    py_files = {path: [] for path in all_files.rglob("*.py")}
    fils = list(py_files.keys())
    for fil in fils:
        py_files[fil] = get_all_functions(fil)
    print("[INFO] Done creating list of files")
    return py_files


def graph_creator(dictionary, retType="functions"):
    # Create the graph
    dot = Digraph("Project")
    dot.format = args.fo
    # Create node names
    for file in dictionary:
        dot.node(file.name)
        # Add functions/classes
        for methods in dictionary[file][retType]:
            dot.edge(file.name, methods)

    print(dot.source)
    # Save graphs in required location
    dot.render(Path.joinpath(Path(args.dir), retType))
    Path.unlink(Path.joinpath(Path(args.dir), retType))
    print("[INFO] Saved Graph")


processed = get_files(args.dir)
graph_creator(processed, "functions")
graph_creator(processed, "classes")
print("[INFO] Please check the project directory for the graphs")

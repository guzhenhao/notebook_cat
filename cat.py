import json
import sys

notebook_path_lst= sys.argv[1:]
target_notebook = {}
cells_str = []


for path in notebook_path_lst:
    notebook = open(path)
    notebook_str = notebook.read()
    notebook_json = json.loads(notebook_str)
    cells1 = notebook_json['cell']
    cells_str += cells

target_notebook['cells'] = cells_lst    




cells2 = notebook2_json['cells']


del notebook1_json['cells']

target_cells = cells1 + cells2




target_notebook.update(notebook1_json)

target_str = json.dumps(target_notebook)

target = open('target_notebook.ipynb','w')
target.write(target_str)
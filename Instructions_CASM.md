## How to start _with CASM_

CASM(Crime Analysis and Scenario Mapping) Tool will help you to organize your investigation process.
Currently, there are 2 import methods available, 

* Open Case (.casm)
* Import from (.csv)

For shorter, brainstorming level mapping, we recommend adding the necessary nodes(text-box for your content) with the GUI buttons and saving the nodes as .casm file.
To map out an entire case file, we recommend using our _Import from '.csv'_ feature. 
By defining the node type and the content in csv format, CASM can automatically generate the nodes. Refer to table below to create a csv file for CASM.

| Node type  | Node abbreviation |
| ------------- | ------------- |
| Evidence  | e, evidence  |
| Sub-source  | sub, subsource  |
| Source  | s, source  |
| Activity  | a, activity |
| Story  | st, story |

For example, you could save a csv file containing

```
a, Suspect X entered house
e, CCTV footage
```

and this will create an Activity node and Evidence node in CASM.

After the import, you can add additional nodes or delete ones you don't need. Save the nodes as a .casm file.


## Main features

### Modifying the nodes

Use right-mouse-click after selecting a node. The following features will be available:

* Changing shape of node
* Changing color of node
* Changing size of node
* DELETE node
* Create connection (line) FROM node 
* Create connection (line) TO node

### Making connection lines between nodes

1. Select one node(_Starting Point_) and use right-mouse-click to go to the node menu. 
2. Click on **'Make Connection From This Node'**
3. Select a different node (_Destination Point_) and use right-mouse-click to go to the node menu.
4. Click on **'Make Connection To This Node'**
5. Then, you will have a connection line between the two nodes.

### Toggle arrow tips to the connection line

Click on the connection line between the nodes to open the connection menu.
You can toggle arrows tips pointing to one node or both nodes.

### Changing connection line color

Click on the connection line between the nodes to open the connection menu.
You have four options: 

* Strong Support (Black)
* Weak Support (Grey)
* Strong Contradiction (Red)
* Weak Contradiction (Light-red)

### Changing connecting side of node

Another feature in the connection menu is changing the connecting side of the nodes.
You have four options for both nodes:

* top
* left
* right
* bottom

For example, if you want to connect the right side of node 1 to the bottom side of node 2, 
click on the right button on the right cross(dpad-like button) and the bottom button on the left cross. This feature can be used to separate lines that overlap or simply serve to neatly organize the map.

## Shortcuts

### To select multiple nodes

Use left-mouse-click and drag over the nodes.
If the header of the node turns light-blue, it is selected and you can move multiple nodes at the same time.

### Align Horizontal

Select the nodes to align and press 'h' on your keyboard.

### Align Vertical

Select the nodes to align and press 'v' on your keyboard.

### Undo

Use Ctrl + z to undo.





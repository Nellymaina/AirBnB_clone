![image](https://user-images.githubusercontent.com/99280364/183242557-dcc6e14a-b2a1-4db1-a0eb-cb459eec97de.png)
### DESCRIPTION

AirBnB is a complete web application, integrating database storage, a back-end API, and front-end interface. The purpose of this project is to make a command interpreter that manages our AirBnb objects.This project, done in pairs and is the first step into web application.

### AirBnB Clone - The Console

The console is the first segment of the AirBnB project that collectively covers the fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

## Functionalities of the command interpreter:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

### Installation:

Clone this repository: `git clone "https://github.com/17Keith/AirBnB_clone.git"`

Access AirBnb directory: `cd AirBnB_clone`
### How to start it:

Run hbnb(interactively): `./console and enter command`
Run hbnb(non-interactively): `echo "<command>" | ./console.py`
 
### How to use it:

To run the console in non-interactive mode, pipe any command(s) into an execution of the file console.py at the command line.

**Example:**

```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$
```
Alternatively, to use the HBnB console in interactive mode, run the 
file `console.py` by itself:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb) 
```

To quit the console, enter the command `quit`, or input an EOF signal 
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```
Type help within the console to get a list of command options and its functions.
**Example:**
 ```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  create  help  quit

Undocumented commands:
======================
all  destroy  show  update

(hbnb) help quit
Quit command to exit the program
(hbnb) quit
$
```

## File Descriptions
[console.py](console.py) - the console contains the entry point of the command interpreter. 
List of commands this console current supports:
* `EOF` - exits console 
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 


### OBJECTS IMPLEMENTED
This repository contains the following files:

| Folder | File | Description |
| :--- | :--- | :--- |
| tests |  | Contains test files for AirBnb Clone |
|  | console.py | Command line Interpreter for managing AirBnB objects |
| models | base_model.py | Defines all common attributes/methods for other classes |
| models | amenity.py | Creates class `amenity` |
| models | city.py | Creates class `city` |
| models | place.py | Creates class `place` |
| models | review.py | Creates class `review` |
| models | state.py | Creates class `state` |
| models | user.py | Creates class `user` |
| models/engine/ | file_storage.py | Serializes instances to a JSON file and deserializes JSON file to instances |

 
 
## Authors :black_nib::
* **Nelly Maina**
* **Keith Obando**

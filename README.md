# PyQtCross

PyQtCross is a very simple picross game made with PyQt6. It is a personal project to learn PyQt6 and to have fun, but mostly have fun with my family by sharing picross models.

Currently, the project is in a very early stage, try it and you'll see what I am talking about.

## Installation

Some day I will release an executable for Windows 10, but for now you have to clone the repository and run the `main.py` file after installing the requirements. Here's how to do that :

```bash
git clone https://github.com/ZWerduex/pyqtcross.git
cd pyqtcross
```

I recommend using a virtual environment, but it's not mandatory. I will ensure that you know how to do it with `venv`, but you can use any other virtual environment manager. Once you're done with that part, you can install the requirements :

```bash
pip install -r requirements.txt
```

And finally, you can run the game :

```bash
python src/main.py
```

## Usage

Left click on a cell fills it, while right click on a cell crosses it. Repeating the same action on a cell will remove the fill or the cross. Pretty simple, right ?

## So, what's next ?

BUGFIXES, of course. I have already noticed some of them. If you find one, please report it in the issues section of this repository.

I have a lot of ideas for this project, but I don't know if I will have the time to implement them all. Here's a list of what I want to do :

- Add a cool menu for managing cool things such as saving, loading, profiles, etc.
- Add a model editor (*GOD I WANT THIS SO BAD*)
- Add a model library (*GOD I WANT THIS SO BAD TOO*)
    * With a search bar :O
    * With a "random" button :O
    * With a "download" button :O so you can share with people your models
    * MAYBE EVEN A GLOBAL LIBRARY

> I will need a server for that, with an API that delivers JSON or some black magic thing, another project to do !

- Add an in-game sidebar with i.e. :
    * A timer for the speedrunners (*I'm not one of them, but I know they exist*)
    * A "hint" button that will fill a random cell for you
    * A "check" button that will check if you made a mistake
    * A "solve" button for the laziests, that will solve the model for you (*I'm one of them*)

## Contributing

I don't know if anyone will ever contribute to this project, but if you want to, you can. I will be very happy to see that someone is interested in my project. If you want to contribute, please follow these steps :

1. Contact me on Discord : **zwx**
2. ???
3. Repeat


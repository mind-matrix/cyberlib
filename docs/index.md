# Cyberlib
A cool cyber-security python library.

<a class="github-button" href="https://github.com/mind-matrix/cyberlib" data-color-scheme="no-preference: light; light: light; dark: light;" data-icon="octicon-star" data-size="large" aria-label="Star mind-matrix/cyberlib on GitHub">Star</a> <a class="github-button" href="https://github.com/mind-matrix" data-color-scheme="no-preference: light; light: light; dark: light;" data-size="large" aria-label="Follow @mind-matrix on GitHub">Follow @mind-matrix</a> <a class="github-button" href="https://github.com/mind-matrix/cyberlib/fork" data-color-scheme="no-preference: light; light: light; dark: light;" data-icon="octicon-repo-forked" data-size="large" aria-label="Fork mind-matrix/cyberlib on GitHub">Fork</a>

<script async defer src="https://buttons.github.io/buttons.js"></script>

## Installation
Cyberlib is available on PyPI Repository. You can use pip package manager to install cyberlib.
```
pip install cyberlib
```
On Windows using Python 3.7 -
```
pip3 install cyberlib
```

## CLI
This project comes with a CLI interface. The commands are

* `cy encrypt [--input I] [--output O] [--passcode P]` - Encrypts a file (input) using a passcode. If passcode is not provided, it generates one.
* `cy decrypt [--input I] [--output O] [--passcode P]` - Decrypts a file (input) using a given passcode. If a wrong passcode is entered, the data a new layer of encryption is added with a random passcode.
* `cy yolo [--input I] [--passcode P]` - Builds a YOLO file from a given input file using a passcode (if not provided, generates one).

## Python
You can import and use the cyberlib package using the `cy` module.
```
import cy
```
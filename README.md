# Cyberlib
A utility box for encryption/decryption.

## Installation

From PyPI Repository -

```
pip install cyberlib
```

## Encrypt
To encrypt a file using the CLI -
```
cy encrypt [--input I] [--output O] [--passcode P]
```
The input is required for encryption. If a passcode is not provided, it will generate a 32 character passcode for you.

## Decrypt
To decrypt a file using the CLI -
```
cy decrypt [--input I] [--output O] [--passcode P]
```
The input is required for decryption. The passcode is required for decryption. If a wrong passcode is provided, the file is locked forever with a random key.

## YOLO
You can create a YOLO box (executable file) from any normal file. The yolo executables are designed to accept a passcode and decrypt the data. If the passcode is correct, it will decrypt and present the actual data. However, if the passcode is wrong, it will lock the data with a random key. To create a yolo executable using the CLI -
```
cy yolo [--input I] [--passcode P]
```
The input is required. A 32 character passcode is generated if no passcode is provided.

## Documentation
You can find the entire documentation for the latest version of the project at https://cyberlib.readthedocs.io/en/latest/.
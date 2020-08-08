from cy.Box import Box, AESBox
import argparse
import PyInstaller.__main__
import os
import pickle
from chardet import detect

__pdoc__ = {}
def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']

def encrypt(args):
    if args.input is None:
        raise 'An input file must be provided'
    if not args.binary:
        encoding = get_encoding_type(args.input)
        print("Detected file encoding %s" % (encoding))
        with open(args.input, "r") as fd:
            crypt = AESBox(fd.read().encode(encoding), encoding=encoding)
            fd.close()
    else:
        print("Opening %s as binary" % (args.input))
        with open(args.input, "rb") as fd:
            crypt = AESBox(pickle.load(fd))
            fd.close()
    if args.passcode is None:
        passcode = AESBox.generate_passcode()
    else:
        passcode = args.passcode
    crypt.encrypt(passcode)
    print(crypt.data)
    with open(args.output or './encrypted', "wb") as fd:
        pickle.dump(crypt.serialize(), fd)
        fd.flush()
        fd.close()
    return passcode

def decrypt(args):
    with open(args.input, "rb") as fd:
        crypt = Box.deserialize(pickle.load(fd), boxtype=AESBox)
        print(crypt.data)
        crypt.decrypt(args.passcode)
        fd.close()
        with open(args.input, "wb") as fd:
            pickle.dump(crypt.serialize(), fd)
            fd.flush()
            fd.close()
        if crypt.encoding is not None:
            with open(args.output or './decrypted', "w") as fd:
                fd.write(crypt.data.decode(crypt.encoding))
                fd.close()
        else:
            with open(args.output or './decrypted', "wb") as fd:
                fd.write(crypt.data)
                fd.close()

def generate(file):
    PyInstaller.__main__.run([
        '--noconfirm',
        '--onefile',
        '--console',
        '--hidden-import=%s' % 'cyberlib',
        '--add-data=%s%sdata' % (os.path.abspath(file), ';' if os.name == 'nt' else ':'),
        os.path.join(__file__, '../../template', 'yolo.py')
    ])

def main():
    parser = argparse.ArgumentParser(description='You Only Live Once!')
    parser.add_argument('action', metavar='encrypt | decrypt | generate', type=str, help='The action to perform on input file')
    parser.add_argument('--passcode', metavar='P', default=None, type=str, help='The passcode of life and death')
    parser.add_argument('--output', metavar='O', default=None, type=str, help='The output file')
    parser.add_argument('--input', metavar='I', default=None, type=str, help='The input file')
    parser.add_argument('--binary', default=False, action="store_true", help='If this flag is set the file will be handled as binary')

    args = parser.parse_args()

    if (args.action == 'encrypt'):
        passcode = encrypt(args)
        print('Generated encrypted file: %s' % (args.output or os.path.abspath('./encrypted')))
        print('Your Access Passcode is: %s' % passcode)
    elif (args.action == 'decrypt'):
        decrypt(args)
        print('Generated decrypted file: %s' % (args.output or os.path.abspath('./decrypted')))
    elif (args.action == 'yolo'):
        passcode = encrypt(args)
        generate(args.output or './encrypted')
        print('Find the yolo executable file inside dist/ folder')
        print('Your Access Passcode is: %s' % passcode)
    else:
        raise 'No valid action found'

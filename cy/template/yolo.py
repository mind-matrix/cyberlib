from cy.Box import AESBox, Box
import pickle
import argparse
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='You Only Live Once!')
    parser.add_argument('passcode', metavar='P', default=None, type=str, help='The passcode of life and death')

    args = parser.parse_args()

    root = resource_path('data')

    files = [ f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f)) ]

    if len(files) > 0:
        df = os.path.join(root, files[0])
        with open(df, "rb") as fd:
            crypt = Box.deserialize(pickle.load(fd), boxtype=AESBox)
            crypt.decrypt(args.passcode)
            fd.close()
            with open(df, "wb") as fd:
                pickle.dump(crypt.serialize(), fd)
                fd.flush()
                fd.close()
            if crypt.encoding is not None:
                with open('./decrypted', "w") as fd:
                    fd.write(crypt.data.decode(crypt.encoding))
                    fd.close()
            else:
                with open('./decrypted', "wb") as fd:
                    fd.write(crypt.data)
                    fd.close()

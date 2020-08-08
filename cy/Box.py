from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import secrets
import random
from Crypto.Random import get_random_bytes
from abc import ABC, abstractmethod, abstractstaticmethod, abstractclassmethod
import hashlib

class Box(ABC):
    '''Generic Box class for data encryption, storage and retrieval'''
    @classmethod
    def __init__(self, data, encoding=None, headers=None):
        self.data = data
        self.encoding = encoding
        self.headers = headers or {}
    
    @abstractstaticmethod
    def generate_passcode(length):
        '''Generates a passcode of a given length'''
        raise NotImplementedError
    
    @abstractclassmethod
    def generate_key(self, passcode):
        '''Generates the encryption key from a passcode'''
        raise NotImplementedError
    
    @abstractclassmethod
    def encrypt_data(self, key):
        '''Internal data encryption method'''
        raise NotImplementedError

    @abstractclassmethod
    def decrypt_data(self, key):
        '''Internal data decryption method'''
        raise NotImplementedError
    
    @classmethod
    def encrypt(self, passcode=None, length=32):
        '''Encrypts the data'''
        if passcode is None:
            passcode = self.generate_passcode(length)
        key = self.generate_key(passcode)
        self.headers.update(self.encrypt_data(key))
    
    @classmethod
    def decrypt(self, passcode=None):
        '''Decrypts the data'''
        if passcode is None:
            self.encrypt()
        else:
            key = self.generate_key(passcode)
            self.decrypt_data(key)
    
    @classmethod
    def serialize(self):
        '''Serializes the data and relevant headers for storage'''
        return [
            self.data,
            self.encoding,
            self.headers
        ]
    
    @staticmethod
    def deserialize(payload, boxtype):
        '''Deserializes the data and relevant headers into a derivative of the Box class'''
        return boxtype(
            data=payload[0],
            encoding=payload[1],
            headers=payload[2]
        )

class AESBox(Box):
    '''AES implementation for generic Box class'''
    def generate_passcode(length=32):
        return secrets.token_hex(length)
    
    @classmethod
    def generate_key(self, passcode):
        if 'salt' not in self.headers:
            self.headers['salt'] = self.generate_passcode(32)
        return PBKDF2(passcode, self.headers['salt'])
    
    @classmethod
    def encrypt_data(self, key):
        md5 = hashlib.md5()
        md5.update(self.data)
        self.headers['hash'] = md5.hexdigest()
        cipher = AES.new(key, AES.MODE_OCB)
        nonce = cipher.nonce
        ciphered_data, tag = cipher.encrypt_and_digest(self.data)
        self.data = ciphered_data
        return {
            'nonce': nonce,
            'tag': tag
        }
    
    @classmethod
    def decrypt_data(self, key):
        try:
            cipher = AES.new(key, AES.MODE_OCB, nonce=self.headers['nonce'])
            deciphered_data = cipher.decrypt_and_verify(self.data, self.headers['tag'])
            md5 = hashlib.md5()
            md5.update(deciphered_data)
            data_hash = md5.hexdigest()
            if self.headers['hash'] != data_hash:
                raise ValueError
            self.data = deciphered_data
        except ValueError as KeyError:
            self.encrypt()
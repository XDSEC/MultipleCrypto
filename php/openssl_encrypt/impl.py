import base64
# pycryptodome / pycrypto
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
SUPPORTED_METHODS = []


# AES encryptions
AES_MODE_LIST = ['ECB', 'CBC'] # +['CFB', 'PGP', 'OFB', 'CTR']
#TODO: tests fails on commented modes


def _aes_encrypt(data: bytes, key, mode, iv) -> bytes:
    enc = AES.new(key, AES_MODE_LIST.index(mode.upper())+1, iv)
    data = pad(data, 16)
    return enc.encrypt(data)


SUPPORTED_METHODS.extend(['aes-128-'+i.lower() for i in AES_MODE_LIST])
SUPPORTED_METHODS.extend(['aes-192-'+i.lower() for i in AES_MODE_LIST])
SUPPORTED_METHODS.extend(['aes-256-'+i.lower() for i in AES_MODE_LIST])


#! export
def openssl_encrypt(
    data: bytes, method: str, key: str,
    options: str = '',
    iv: bytes = b"\0"*16,
    tag="",
    aad="",
    tag_length=16
) -> str:
    '''
    Implements openssl_encrypt() for php

    Args:
        data: The plaintext message data to be encrypted.
        method: The cipher method. For a list of available 
            cipher methods, use openssl_get_cipher_methods().
        key: The key.
        options: a bitwise disjunction of the flags OPENSSL_RAW_DATA
            and OPENSSL_ZERO_PADDING.
        iv: A non-NULL Initialization Vector.
        tag: The authentication tag passed by reference when using
            AEAD cipher mode (GCM or CCM).
        aad: Additional authentication data.
        tag_length: The length of the authentication tag. Its value
            can be between 4 and 16 for GCM mode.
    
    Returns:
        Returns the encrypted string on success or `False` on failure.

    Caution:
        On PHP:
            7.1.0	The tag, aad and tag_length parameters were added.
            5.4.0	The raw_output was changed to options.
            5.3.3	The iv parameter was added.
    '''
    if type(data) != bytes:
        if type(data) == str:
            data = data.encode('utf-8')
        else:
            raise TypeError('data must be bytes')
    if method not in SUPPORTED_METHODS:
        raise NotImplementedError('Encrytpion Method Not Implemented')
    if method.lower().startswith('aes'):
        return base64.b64encode(_aes_encrypt(data, key, method[-3:], iv)).decode()
    pass

from php.openssl_encrypt._aes import _aes_encrypt, AES_MODE_LIST
import base64
# pycryptodome / pycrypto
SUPPORTED_METHODS = []

SUPPORTED_METHODS.extend(['aes-128-'+i.lower() for i in AES_MODE_LIST])
SUPPORTED_METHODS.extend(['aes-192-'+i.lower() for i in AES_MODE_LIST])
SUPPORTED_METHODS.extend(['aes-256-'+i.lower() for i in AES_MODE_LIST])

#! export
def openssl_encrypt(
    data: bytes, method: str, key: str,
    options: str = '',
    iv: bytes = b'',
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
    method = method.lower()
    if method not in SUPPORTED_METHODS:
        raise NotImplementedError('Encrytpion Method Not Implemented')
    method = method.split('-')
    if method[0] == 'aes':
        raw_encrypted = _aes_encrypt(data, key, method[2], method[1], iv)
    # elif method[0] == '':
    return base64.b64encode(raw_encrypted).decode()

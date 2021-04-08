from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

AES_MODE_LIST = ['ECB', 'CBC', 'CFB', 'PGP', 'OFB', 'CFB1', 'CFB8']
#TODO: CTR mode, CFB1 mode
# what on earth does "1" mean?

def get_encryptor(key, iv, mode):
    if mode == 'CBC':
        return AES.new(key.encode(), AES.MODE_CBC, iv)
    elif mode == 'OFB':
        return AES.new(key.encode(), AES.MODE_OFB, iv)
    elif mode.startswith('CFB'):
        if mode == 'CFB':
            segment_size = 128
        elif mode == 'CFB8':
            segment_size = 8
        else: #mode == 'CFB1':
            segment_size = 8*1
            raise NotImplementedError('Unknown Mode')
        return AES.new(
            key.encode(), AES.MODE_CFB, iv,
            segment_size=segment_size
        )
    else:
        return AES.new(key.encode(), AES_MODE_LIST.index(mode)+1)
    raise NotImplementedError('Unknown Mode')

# php behavior

def format_key(key, key_bit):
    try:
        key = key[:key_bit//8]
    except IndexError:
        key = key.ljust(key_bit//8, '\0')
    return key


def _aes_encrypt(data: bytes, key: str, mode, key_bit: str, iv) -> bytes:
    # assert(len(key)*8 == int(key_bit))
    key = format_key(key, int(key_bit))
    mode = mode.upper()
    if mode[:3] not in ['CFB', 'OFB', 'CTR']:
        data = pad(data, 16)

    return get_encryptor(key, iv, mode).encrypt(data)

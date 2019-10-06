import php.openssl_encrypt.impl as impl
import os
import pytest
td = []
for i in impl.SUPPORTED_METHODS:
    if i.startswith('aes-128'):
        td.append(['a'*16, i])
    elif i.startswith('aes-256'):
        td.append(['a'*32, i])
    elif i.startswith('aes-192'):
        td.append(['a'*24, i])


@pytest.mark.parametrize('key, method', td)
def test_aes(key, method):
    print('testing with '+method)
    cmd = f'''php -r "print(openssl_encrypt('testtesttesttesttesttest', '{method}', '{key}'));"'''
    res = os.popen(cmd).read().split('\n')[-1]
    print(cmd)
    assert(res == impl.openssl_encrypt(
        "testtesttesttesttesttest", method, key
    ))
    print('ok')

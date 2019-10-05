import openssl_encrypt.impl as impl
import os


def test_aes(key, bit):
    for i in impl.SUPPORTED_METHODS:
        if i.startswith('aes-'+bit):
            print('testing with '+i)
            res = os.popen(
            f'''php -r "print(openssl_encrypt('testtesttesttesttesttest', '{i}', '{key}'));"
            '''
            ).read().split('\n')[-1]
            try:
                assert(
                    res == 
                    impl.openssl_encrypt("testtesttesttesttesttest", i, key)
                )
                print('ok')
            except:
                print('result differs with '+i)
test_aes('a'*16, '128') # fails on commented modes
test_aes('a'*32, '256') # fails on commented modes
test_aes('a'*24, '192') # fails

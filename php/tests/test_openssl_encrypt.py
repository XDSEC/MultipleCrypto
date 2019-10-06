import php.openssl_encrypt.impl as impl
import os
import pytest
ecb = [  # without iv
    ["aes-128-ecb", "testtesttesttesttesttest", "test keytest key",
        "fH0UhUyxByLqscU7ObIocqC3Y8S0xTHrhiP6yIQsJnI="],
    ["aes-192-ecb", "testtesttesttesttesttest", "test keytest keytest key",
        "Ac9k6tdeYs3/RSC04wC5CUxYD8LxUQ6WKmF5316LKH4="],
    ["aes-256-ecb", "testtesttesttesttesttest", "test keytest keytest keytest key",
        "mniFOVowpLoyJptUat7ZDGfA1P7L6j4g+VlCBz2CiUQ="],
]
cbc = [
    ["aes-128-cbc", "testtesttesttesttesttest", "test keytest key",
        "1234567890123456", "0JAafjNSSlfnidG6Ta+RF5BRaxxLkIn3ca7cLBeg8MI="],
    ["aes-192-cbc", "testtesttesttesttesttest", "test keytest keytest key",
        "1234567890123456", "1dmtE0ywmdciqQr2C+ZhTLSo8N/QEoLVhWQby+KArLk="],
    ["aes-256-cbc", "testtesttesttesttesttest", "test keytest keytest keytest key",
        "1234567890123456", "P86TH2o//ap85yrNcOOQi/PpzBQEiPrT6JkzKo7PrFc="],
]
cfb = [
    ["aes-128-cfb", "testtesttesttesttesttest", "test keytest key",
        "1234567890123456", "R4nuLVgTeJ3JnCYemo34zHq2jqDT91U+"],
    ["aes-192-cfb", "testtesttesttesttesttest", "test keytest keytest key",
        "1234567890123456", "K8uay8YYOy+Ekzsa8h8fDWKvc4fugyhb"],
    ["aes-256-cfb", "testtesttesttesttesttest", "test keytest keytest keytest key",
     "1234567890123456", "gGrcsiPCrd8AUYxDqvYrVgkLBbfUGG/H"],
]
ofb = [

    ["aes-128-ofb", "testtesttesttesttesttest", "test keytest key",
        "1234567890123456", "R4nuLVgTeJ3JnCYemo34zFMpKiLnTsV4"],
    ["aes-192-ofb", "testtesttesttesttesttest", "test keytest keytest key",
        "1234567890123456", "K8uay8YYOy+Ekzsa8h8fDdhRFI04rn37"],
    ["aes-256-ofb", "testtesttesttesttesttest", "test keytest keytest keytest key",
        "1234567890123456", "gGrcsiPCrd8AUYxDqvYrVs6EVYlFkS+p"],
]


@pytest.mark.parametrize('method, data, key, iv, expect', cbc)
def test_aes_with_iv(method, data, key, iv, expect):
    assert(expect == impl.openssl_encrypt(data, method, key, 0, iv.encode()))


@pytest.mark.parametrize('method, data, key, expect', ecb)
def test_aes_without_iv(method, data, key, expect):
    assert(expect == impl.openssl_encrypt(data, method, key))


if __name__ == '__main__':
    for i in cbc:
        test_aes_with_iv(*i)
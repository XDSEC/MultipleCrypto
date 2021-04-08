import php.openssl_encrypt as impl
import os
import pytest
with_iv = [
["testtesttesttesttesttest", "test keytest key", "aes-128-cbc", "1234567890123456", "0JAafjNSSlfnidG6Ta+RF5BRaxxLkIn3ca7cLBeg8MI="],
["testtesttesttesttesttest", "test keytest key", "aes-128-cfb", "1234567890123456", "nVJHGwG33NiPqtt9PH+ikYXzyp1WSAkv"], 
["testtesttesttesttesttest", "test keytest key", "aes-128-ofb", "1234567890123456", "nVJHGwG33NiPqtt9PH+ikarwk0pi2f2f"],
# ["testtesttesttesttesttest", "test keytest key", "aes-128-ctr", "1234567890123456", "nVJHGwG33NiPqtt9PH+ikYWtQmPJP88I"],
# ["testtesttesttesttesttest", "test keytest key", "aes-128-cfb1", "1234567890123456", "+zNQhL1/FOP2HDgt+RMGFIXHsVIisQnY"],
["testtesttesttesttesttest", "test keytest key", "aes-128-cfb8", "1234567890123456", "nSOd05BAnNrlwJV2lhq1RFTbQq0i1pd3"],
["testtesttesttesttesttest", "test keytest keytest key", "aes-192-cbc", "1234567890123456", "1dmtE0ywmdciqQr2C+ZhTLSo8N/QEoLVhWQby+KArLk="],
["testtesttesttesttesttest", "test keytest keytest key", "aes-192-cfb", "1234567890123456", "K8uay8YYOy+Ekzsa8h8fDWKvc4fugyhb"],
["testtesttesttesttesttest", "test keytest keytest key", "aes-192-ofb", "1234567890123456", "K8uay8YYOy+Ekzsa8h8fDdhRFI04rn37"],
# ["testtesttesttesttesttest", "test keytest keytest key", "aes-192-ctr", "1234567890123456", "K8uay8YYOy+Ekzsa8h8fDWFWXVendSzj"],
# ["testtesttesttesttesttest", "test keytest keytest key", "aes-192-cfb1", "1234567890123456", "T6h1RhxWTvFinfv2ey3I4gh7UdjZ1hm1"],
["testtesttesttesttesttest", "test keytest keytest key", "aes-192-cfb8", "1234567890123456", "K80s02flGqlD58jxx9nmVeciJsDXXR/w"],
["testtesttesttesttesttest", "test keytest keytest keytest key", "aes-256-cbc", "1234567890123456", "P86TH2o//ap85yrNcOOQi/PpzBQEiPrT6JkzKo7PrFc="],
["testtesttesttesttesttest", "test keytest keytest keytest key", "aes-256-cfb", "1234567890123456", "gGrcsiPCrd8AUYxDqvYrVgkLBbfUGG/H"],
["testtesttesttesttesttest", "test keytest keytest keytest key", "aes-256-ofb", "1234567890123456", "gGrcsiPCrd8AUYxDqvYrVs6EVYlFkS+p"],
# ["testtesttesttesttesttest", "test keytest keytest keytest key", "aes-256-ctr", "1234567890123456", "gGrcsiPCrd8AUYxDqvYrVq1kUXiWk5kN"],
# ["testtesttesttesttesttest", "test keytest keytest keytest key", "aes-256-cfb1", "1234567890123456", "nWIsvKtJvwcQTW73HuHTnRabP7IeiBb4"],
["testtesttesttesttesttest", "test keytest keytest keytest key", "aes-256-cfb8", "1234567890123456", "gAtvBgan3oxs+KoPlZ6EVYK6UvcVTDTE"]
]
without_iv = [
["testtesttesttesttesttest", "test keytest key", "aes-128-ecb", "fH0UhUyxByLqscU7ObIocqC3Y8S0xTHrhiP6yIQsJnI="],
["testtesttesttesttesttest", "test keytest keytest key", "aes-192-ecb", "Ac9k6tdeYs3/RSC04wC5CUxYD8LxUQ6WKmF5316LKH4="],
["testtesttesttesttesttest", "test keytest keytest keytest key", "aes-256-ecb", "mniFOVowpLoyJptUat7ZDGfA1P7L6j4g+VlCBz2CiUQ="]
]

@pytest.mark.parametrize('data, key, method, iv, expect', with_iv)
def test_aes_with_iv(data, key, method, iv, expect):
    assert(expect == impl.openssl_encrypt(data, method, key, 0, iv.encode()))


@pytest.mark.parametrize('data, key, method, expect', without_iv)
def test_aes_without_iv(data, key, method, expect):
    assert(expect == impl.openssl_encrypt(data, method, key))


if __name__ == '__main__':
    print(impl.SUPPORTED_METHODS)

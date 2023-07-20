from woke.testing import *

from pytypes.test.sait import SaiTestBase
from pytypes.src.tub import SaiTub

@default_chain.connect()
def main():
    default_chain.set_default_accounts(default_chain.accounts[0])
    print('1')
    stb = SaiTestBase.deploy()
    print('2')
    tub = SaiTub.deploy(
        Address("0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef"),
        Address("0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef"),
        Address("0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef"),
        Address("0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef"),
        Address("0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef"),
        Address("0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef"),
        Address("0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef"),
        Address("0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef"),
        Address("0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef"),
    )
    print('2')
    # stb.setUp()
    print('3')



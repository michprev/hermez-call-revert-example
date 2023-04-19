from woke.deployment import *
from pytypes.contracts.Dummy import Dummy


@default_chain.connect("https://rpc.public.zkevm-test.net")
def main():
    acc = Account.from_mnemonic("YOUR MNEMONIC HERE")
    estimate = Dummy.deploy(request_type="estimate", from_=acc)

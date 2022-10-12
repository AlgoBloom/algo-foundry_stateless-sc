import sys
sys.path.insert(0,'.')

from algobpy.parse import parse_params
from pyteal import *

def htlc(acc1_addr, acc2_addr, hash, timeout):

    # write your code here
    basic_checks = And(
        Txn.rekey_to() == Global.zero_address(),
        Txn.close_remainder_to() == Global.zero_address()
    )

    fund_withdraw_checks = And(
        Txn.
    )

    fund_recovery_check = And(

    )

    receiver_checks = Cond(
        [Txn.receiver() == Addr("WDAQAZX5OAOHXI6I6EN5M7RFKE6ZOWKQHHSOVJOVMSGFNZQCHOZKNTMN5A"), fund_withdraw_checks],
        [Txn.receiver() == Addr("Y7QD5UTGLEIHX6LQMDRGGAQMIUFOWUWFS3C4Z3JYO6EOTPQA723Y5OMRC4"), fund_recovery_check]
    )

    program = (
        basic_checks,
        receiver_checks
    )

    return program

if __name__ == "__main__":
    # Default receiver address used if params are not supplied when deploying this contract
    params = {
        "acc1": "WDAQAZX5OAOHXI6I6EN5M7RFKE6ZOWKQHHSOVJOVMSGFNZQCHOZKNTMN5A",
        "acc2": "Y7QD5UTGLEIHX6LQMDRGGAQMIUFOWUWFS3C4Z3JYO6EOTPQA723Y5OMRC4",
        "hash": "QzYhq9JlYbn2QdOMrhyxVlNtNjeyvyJc/I8d8VAGfGc=",
        "timeout": 3001
    }

    # Overwrite params if sys.argv[1] is passed
    if(len(sys.argv) > 1):
        params = parse_params(sys.argv[1], params)

    print(compileTeal(htlc(
        params["acc1"], 
        params["acc2"], 
        params["hash"], 
        params["timeout"]), mode=Mode.Signature, version=6))
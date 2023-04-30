from web3 import Web3
from web3.auto import w3
from eth_account.messages import encode_defunct


def createburnerwallet():
    w3instance = Web3()
    return w3.eth.account.create()

def getaddr(acc):
    return acc.address


def getpk(acc):
    return acc.key


testaddress = '0xA70caF9eAeEe87336E845E6b1628449224Dd024B'
testhexpk = b'\xe7\xcd\xe8\xf8\xee\x97\xaa[\x81\xba\x18\xfd\xef\xb8\xb6\xdd\xbfG\xd6\x8c\xa9\xde\x13\x0f\xc4\xfaZ\xe8\x82\x12\xa5z'
testpk = '0xe7cde8f8ee97aa5b81ba18fdefb8b6ddbf47d68ca9de130fc4fa5ae88212a57a'


def signmess(msg,pk):
    message = encode_defunct(text=msg)
    return w3.eth.account.sign_message(message, private_key=pk)


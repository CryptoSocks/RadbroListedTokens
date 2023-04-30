from moralis import evm_api
import Constants



def getRadPrice():
    params = {
        "address": "0xdDc6625FEcA10438857DD8660C021Cd1088806FB",
        "chain": "eth"
    }
    result = evm_api.token.get_token_price(
        api_key=Constants.moralis_key,
        params=params,
    )
    return result['usdPrice']

def getEthPrice():
    params = {
        "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "chain": "eth"
    }
    result = evm_api.token.get_token_price(
        api_key=Constants.moralis_key,
        params=params,
    )
    return result['usdPrice']


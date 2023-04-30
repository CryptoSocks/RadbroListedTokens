import Web3Connect
import GetBlurListings
import GetPrice

radprice = GetPrice.getRadPrice()
ethprice = GetPrice.getEthPrice()


"""
id : radbro ID
calls the RadCoin contract and checks how many rad a radbro has 
returns the total rad unclaimed 
"""


def get_rewards(id):
    return (Web3Connect.contract.functions.getClaimRewards(Web3Connect.Radbrov2, [id]).call()) / (10 ** 18)


"""
id(optional) : if included it prints the amount of unclaimed rad for a certain radbro also prints its usd equivalent
rebate(optional): defaults to 10% rebate when searching listings with unclaimed rad
p(optional): defaults to 0.3 eth for radbro listings

if Id is not included it gets all radbro listings on opensea and blur and prints out all radbros that have a rebate
greater than rebate and a price less than p
"""


def get_radcoins(rebate=10.0, p=0.3, id=False ):

    if not id:
        alllistings = GetBlurListings.listListings(GetBlurListings.getAllListings())
        alllistings.sort(key=lambda e: e['price'])
        for l in alllistings:
            radreward = get_rewards(int(l['id'])) * radprice
            radrebate= radreward*100/(l['price']*ethprice)
            price = l['price']
            if radrebate > rebate and price < p:
                print("Radbro " + l['id'] + " on " + l['marketplace'])
                print("Eth " + str(price) + " ~$" + str(round(l['price']*ethprice, 2)))
                print("Unclaimed Rad: " + str(round(get_rewards(int(l['id'])), 2)))
                print("Unclaimed Rad (in USD): " + str(round(radreward, 2)))
                print("Rad Rebate: " + str(round(radrebate, 2)) + "%")
                print("--------------------------------------")

    else:
        rewards = get_rewards(id)
        print("Unclaimed Rad: " + str(rewards))
        print("Unclaimed Rad (in USD): " + str(rewards * radprice))


"""
add rebate(float) for the lowest percentage you want to look for
add p for the highest price you are willing to payment
or add id if you only want to check one radbro
"""
get_radcoins()
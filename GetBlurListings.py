import requests
import Constants
import GetBlurAuthKey
import SignMessage

url = "https://blur.p.rapidapi.com/v1/collections/radbro-webring/tokens"

headers = {
	"content-type": "application/octet-stream",
	"authToken": GetBlurAuthKey.GetAccessToken(GetBlurAuthKey.getAuthChallenge())['accessToken'],
	"walletAddress": SignMessage.getaddr(GetBlurAuthKey.burnerwallet),
	"X-RapidAPI-Key": Constants.X_RapidAPI_Key,
	"X-RapidAPI-Host": "blur.p.rapidapi.com"
}

def getAllListings():
	response = requests.get(url, headers=headers)
	return response.json()

def listListings(response):
	Listings = []
	for o in response['tokens']:
		Listings.append({'id': o['tokenId'], 'price': float(o['price']['amount']), 'marketplace': o['price']['marketplace']})

	return Listings
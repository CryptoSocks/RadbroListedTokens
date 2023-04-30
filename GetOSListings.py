import requests
import Constants

"""
This File has been deprecated since the blur listings also includes opensea listings
"""


url = "https://opensea15.p.rapidapi.com/v2/listings/collection/radbro-webring/all"

headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": Constants.X_RapidAPI_Key,
	"X-RapidAPI-Host": "opensea15.p.rapidapi.com"
}

def GetListings(page):
	querystring = {"next": page}
	if not page:
		return requests.get(url, headers=headers).json()
	else:
		return requests.get(url, headers=headers, params=querystring).json()

def GetAllOSListings():
	page = False
	olist = []
	while page is not None:
		currentlist = GetListings(page)
		page = currentlist['next']
		olist += currentlist['listings']

	return olist


def ListListings(response):
	Listings = []
	for o in response:
		Listings.append({'id': o['protocol_data']['parameters']['offer'][0]['identifierOrCriteria'], 'price': int(o['price']['current']['value'])/10**18})

	return Listings



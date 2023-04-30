import requests
import SignMessage
import Constants

burnerwallet = SignMessage.createburnerwallet()

def getAuthChallenge():
	url = "https://blur.p.rapidapi.com/auth/challenge"

	payload = { "walletAddress": SignMessage.getaddr(burnerwallet) }
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": Constants.X_RapidAPI_Key,
		"X-RapidAPI-Host": "blur.p.rapidapi.com"
	}

	response = requests.post(url, json=payload, headers=headers)

	return response.json()

def GetAccessToken(response):
	url = "https://blur.p.rapidapi.com/auth/login"
	payload = {
		"message": response['message'],
		"walletAddress": response['walletAddress'],
		"expiresOn": response['expiresOn'],
		"hmac": response['hmac'],
		"signature": SignMessage.signmess(response['message'], SignMessage.getpk(burnerwallet)).signature.hex()
	}
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": Constants.X_RapidAPI_Key,
		"X-RapidAPI-Host": "blur.p.rapidapi.com"
	}

	access_token = requests.post(url, json=payload, headers=headers)

	return access_token.json()

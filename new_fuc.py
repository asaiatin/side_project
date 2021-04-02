import json
import urllib.parse
import urllib.request


def my_function(userPreference):
	url = "http://www.tropicalfruitandveg.com/api/tfvjsonapi.php?search=" + userPreference
	req = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
	#print(req)
	with urllib.request.urlopen(req) as response:
		the_page = response.read()

	resp = json.loads(the_page.decode('latin-1'))
	#print(type(resp))
	
	if "error" in resp:
		print("Unhealthy")
	else:
		print("Healthy")

			
userPreference = input("Please tell us your preferred food item :- ").lower();
my_function(userPreference)

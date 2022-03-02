# importing requests package
import requests
import draw

def NewsFromBBC():
	
	# BBC news api
	# following query parameters are used
	# source, sortBy and apiKey
	query_params = {
	"source": "bbc-news",
	"sortBy": "top",
	"apiKey": "7480c0efe38b49b49d9d0c2a9a1d37c4"
	}
	main_url = " https://newsapi.org/v1/articles"

	# fetching data in json format
	res = requests.get(main_url, params=query_params)
	open_bbc_page = res.json()

	# getting all articles in a string article
	article = open_bbc_page["articles"]

	# empty list which will
	# contain all trending news
	results = []
	
	for ar in article:
		results.append(ar["title"])
	
	return(results)
	# for i in range(len(results)):
		
	# 	draw.display(results[i])
		# printing all trending news
		#print(i + 1, results[i])

	#to read the news out loud for us
	#from win32com.client import Dispatch
	#speak = Dispatch("SAPI.Spvoice")
	#speak.Speak(results)				

# Driver Code
if __name__ == '__main__':
	
	# function call
	NewsFromBBC()

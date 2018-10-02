import requests

def main():
		
	response = requests.get(input("URL: "))
	print(response.status_code)
	print(response.headers['content-type'])
	print("Tamanho: ",len(response.content))

if __name__ == '__main__':
	main()
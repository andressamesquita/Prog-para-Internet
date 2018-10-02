from bs4 import BeautifulSoup
import requests

def main():

	url = requests.get(input('URL: '))

	html = BeautifulSoup(url.text, 'html.parser')
	links = html.find_all('a')

	[print(link['href']) for link in links]
		


if __name__ == '__main__':
	main()
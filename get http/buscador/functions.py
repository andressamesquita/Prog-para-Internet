from bs4 import BeautifulSoup
import requests

sitio = []



def search(keyword, deth, url_response, profundidade_atual):
	#tratamento do html e busca de keyword
	html = BeautifulSoup(url_response.text, 'html.parser')
	tamanho = len(html.find_all('p'))

	for tag_p in range(tamanho):
		paragrafo = html.find_all('p')[tag_p].get_text().split(" ")
		[print("Palavra: " + paragrafo[indice] + " - profundidade: " + str(profundidade_atual) + " - Link: " + url_response.url) for indice in range(len(paragrafo)) if keyword.upper() in paragrafo[indice].upper()]


	if deth > profundidade_atual:
		recursiva(keyword, deth, url_response, profundidade_atual)



def recursiva(keyword, deth, url_response, profundidade_atual):
	#Todos os links
	html = BeautifulSoup(url_response.text,'html.parser')
	sites = []

	links = html.find_all('a')

	
	for link in links:
		if link['href'] not in sitio:
			sites.append(link['href'])
			sitio.append(link['href'])
	
	for i in range(len(sites)):
		if sites[i][0] == "h":
			url_response = requests.get(sites[i])

		elif sites[i][0] == "/" and len(sites[i]) > 4:
			url_response = requests.get("http:" + sites[i])

		search(keyword, deth, url_response, profundidade_atual +1)



def formatando_url(url):

	if "http" not in url:
		url = "http://" + url
	elif "www" not in url:
		url = url.replace('http://','http://www.')

	return requests.get(url)



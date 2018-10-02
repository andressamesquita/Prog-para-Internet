from functions import *

def main():
	profundidade_atual = 0
	keyword = input("Palavra-chave: ")
	deth = int(input("Profundidade: "))
	url = input("URL: ")
	url_response = formatando_url(url)

	search(keyword, deth, url_response, profundidade_atual)


if __name__ == '__main__':
	main()
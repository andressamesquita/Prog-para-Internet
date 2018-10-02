import requests

def main():
	
	img_response = requests.get(input("URL da img: "))
	open('figura.jpg','wb').write(img_response.content)

if __name__ == '__main__':
	main()
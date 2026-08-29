import requests
from bs4 import BeautifulSoup
url_to_scrape = input("what url would you like to scrape ")
tag = input("which tag would you like to find ")
def get_page(url, option, tag, attribute_choice):
    headers = {
            "User-Agent": "Mozilla/5.0"
        }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(response.status_code)
    if option == "first":
        print(soup.find(tag))
    elif option == "all":
        if attribute_choice == "y":
            chosen_attrib = input("what is the attribute you want to find ")
            for t in soup.find_all(tag):
                attrib_output = t.get(chosen_attrib)
                print(attrib_output)
        elif attribute_choice == "n":
            print(soup.find_all(tag))
while True:
    option = input("would you like to find everything containing that tag or just the first thing? first/all: ")

    if option == "first" or option == "all":
        break
    else:
        print("invalid choice, it's either first or all")
while True:
    attribute_choice = input("would you like to find a certain attribute? y/n ")
    if attribute_choice == "y" or attribute_choice == "n":
        break
    else:
        print("invalid choice it's either y or n")
get_page(url_to_scrape, option, tag, attribute_choice)
# Imports
from tokenize import Name
import requests
import json as js
from pprint import pprint

# # # Functions


# Returns GET request from url
def get_info(call):
    r = requests.get(call)
    return r.json()

# Returns auction info from player uuid
def get_auctions_from_player(uuid):
    return get_info(f"https://api.hypixel.net/skyblock/auction?key={API_KEY}&player={uuid}") 

# Returns a list of all recently finished auctions
def get_recently_ended_auctions(): 
    return get_info("https://api.hypixel.net/skyblock/auctions_ended") 

# Returns a list of all active auctions
def get_auction_data():  
    all_auctions = []

    first_page = get_info("https://api.hypixel.net/skyblock/auctions?page=0")

    auction_data = first_page.get("auctions", [])

    for page in range(1, first_page.get("totalPages", 0) + 1):
        current_page = get_info("https://api.hypixel.net/skyblock/auctions?page={page}")

        all_auctions += (current_page.get("auctions", [])) 
        return all_auctions

    


    

    # Returns auction items after passing through filter
     
def filter_auction_items (auction_data, item_filter):
        filtered_items = []

        for auction in auction_data:
           if(item_filter["name"] in auction.get("item_name", "")):
             filtered_items.append(auction)


        return filtered_items

# Variables
API_FILE = open("C:/Users/Offic/AppData/Local/Temp/Rar$DIa20132.28119/index.js", "r")
# print(type(API_FILE))
API_KEY = js.loads(API_FILE.read())["API_KEY"]
example_player_id = "ceb15bec59b64d4caedcdff5e3b4b0c0"
item_filter = {"name": "Drill"}








# Code
pprint (get_auctions_from_player(example_player_id))

auction_data = get_auction_data()

print (f"Amount of items : {len(auction_data)}")

print (f"Amount of filtered items : {len(filter_auction_items(auction_data, item_filter))}")
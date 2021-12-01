#you need to install the following libraries
#pip install lxml  this is the parser we need to use
#pip install requests
#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

#We need those lists to append the value of each currency in it
bnb_list = [] 
ani_list = []
xmr_list = []
eth_list = [] 


#get the html code of the page you want to get the informations from
bnb_url = requests.get("https://coinmarketcap.com/de/currencies/binance-coin/")
bnb_src = bnb_url.content

ani_url = requests.get("https://coinmarketcap.com/de/currencies/anime-token/")
ani_src = ani_url.content

xmr_url = requests.get("https://coinmarketcap.com/de/currencies/monero/")
xmr_src = xmr_url.content

eth_url = requests.get("https://coinmarketcap.com/de/currencies/ethereum/")
eth_src = eth_url.content


#Using the lxml parser
bnb_soup = BeautifulSoup(bnb_src, "lxml")
ani_soup = BeautifulSoup(ani_src, "lxml")
xmr_soup = BeautifulSoup(xmr_src, "lxml")
eth_soup = BeautifulSoup(eth_src, "lxml")


#Search on each CoinMarketCap html for the value we need
bnb_ = bnb_soup.find("div", {"class":"priceValue"})   #this is a list
bnb_list.append(bnb_.text)   #get just the text and append it in bnb_list

x = bnb_list[0][0]    # this is the "€" symbol we want to remove from the string
bnb_list[0] = bnb_list[0].replace(x, '').replace(",", '')
BNB = float(bnb_list[0])  #typecast the string to float



#same steps as before
ani_ = ani_soup.find("div", {"class":"priceValue"})   #this is a list
ani_list.append(ani_.text)   

x = ani_list[0][0]    
ani_list[0] = ani_list[0].replace(x, '').replace(",", '')
ANI = float(ani_list[0])   



#same steps as before
xmr_ = xmr_soup.find("div", {"class":"priceValue"})  
xmr_list.append(xmr_.text)  

x = xmr_list[0][0]
xmr_list[0] = xmr_list[0].replace(x, '').replace(",", '')
XMR = float(xmr_list[0])



#same steps as before
eth_ = eth_soup.find("div", {"class":"priceValue"})   #this is a list
eth_list.append(eth_.text)   #get just the text

x = eth_list[0][0]
eth_list[0] = eth_list[0].replace(x, '').replace(",", '')
ETH = float(eth_list[0])



#how much you own of each currency (you have to put values that suit you)
my_BNB = 0.5
my_ANI = 1000000
my_XMR = 5.234
my_ETH = 12


#value in euro
BNB_EUR = my_BNB * BNB
ANI_EUR = my_ANI * ANI
XMR_EUR = my_XMR * XMR
ETH_EUR = my_ETH * ETH

#how much you have in total 
summary = BNB_EUR + ANI_EUR + XMR_EUR + ETH_EUR

print ("\n\n==================================\n\n  - Binance: %f BNB\n  ==== %f € ====\n\n  - AnimeToken: %f ANI\n  ==== %f € ====\n\n  - Monero: %f XMR \n  ==== %f € ====\n\n  - Etherium: %f ETH  \n  ==== %f € ====\n\n\n======== %f € ========\n\n==================================" %(BNB, BNB_EUR, ANI, ANI_EUR, XMR, XMR_EUR, ETH, ETH_EUR, summary))
    





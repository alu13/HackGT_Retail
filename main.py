from Shops.Athleta import search_athleta
from Shops.BananaRepublic import search_bananarepublic
from Shops.Bloomingdales import search_bloomingdales
from Shops.Forever21 import search_forever21
from Shops.Gap import search_gap
from Shops.Kohls import search_kohls
from Shops.Macys import search_macys
from Shops.Nordstrom import search_nordstrom
from Shops.OldNavy import search_oldnavy

keywords = ("blue", "dress")
def main():
    for entry in search_kohls(*keywords) \
                 + search_nordstrom(*keywords) \
                 + search_bloomingdales(*keywords) \
                 + search_oldnavy(*keywords) \
                 + search_forever21(*keywords) \
                 + search_macys(*keywords) \
                 + search_athleta(*keywords) \
                 + search_bananarepublic(*keywords) \
                 + search_gap(*keywords):
        print(entry)

if __name__ == "__main__":
    main()
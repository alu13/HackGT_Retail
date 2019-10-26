from Bloomingdales import search_bloomingdales
from Forever21 import search_forever21
from Kohls import search_kohls
from Macys import search_macys
from Nordstrom import search_nordstrom
from OldNavy import search_oldnavy

keywords = ("blue", "dress")
def main():
    for entry in search_kohls(*keywords) \
                 + search_nordstrom(*keywords) \
                 + search_bloomingdales(*keywords) \
                 + search_oldnavy(*keywords) \
                 + search_forever21(*keywords) \
                 + search_macys(*keywords):
        print(entry)

if __name__ == "__main__":
    main()
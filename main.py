from Bloomingdales import search_bloomingdales
from Kohls import search_kohls
from Nordstrom import search_nordstrom
from OldNavy import search_oldnavy

keywords = ("blue", "dress")
def main():
    for entry in search_kohls(*keywords) \
                 + search_nordstrom(*keywords) \
                 + search_bloomingdales(*keywords) \
                 + search_oldnavy(*keywords):
        print(entry)

if __name__ == "__main__":
    main()
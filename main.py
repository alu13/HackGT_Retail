from Bloomingdales import search_bloomingdales
from Kohls import search_kohls
from Nordstrom import search_nordstrom
from OldNavy import search_oldnavy

for i in search_kohls("red","jeans"):
    print(i.text.strip())
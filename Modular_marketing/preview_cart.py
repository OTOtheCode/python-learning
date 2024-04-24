def view_cart(cart): #კალათის ნახვის ფუნქცია
    if not cart:#თუ ცარიელია ვბეჭდავთ რომ ცარიელია
        print("Cart is empty")
    else:# სხვა შემთხევაში ვბეჭდავთ კალათს შიგთავსს
        for product in cart:
           print(f"{product['name']} - {product['price']} $ - quantity: {product['quantity']}")
       
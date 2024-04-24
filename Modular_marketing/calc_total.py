def calc_total(cart): #ღირებულების დათვლის ფუნქცია
    total_price = 0 #განვსაზღვრავთ მთლიანი ჯამის საწყის მნიშვნელობას
    for product in cart: #პროდუქტისათვის კალათაში
        total_price += product["price"]*product["quantity"] #მთ₾იანი ჯამი += პროდუქტის ფასი გამრავლებული რაოდენობაზე
        print(f"{product['name']} - {product['price']} $ - quantity: {product['quantity']}") # ვბეჭდავთ პროდუქციის ჩამონათვალს უფრო. 
                                                                                             # მარტივად ასათქმელია
    print(f"Total price is: {total_price} $") # ვბეჭდავთ ფასის ჯამს
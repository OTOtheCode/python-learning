def remove_prod(cart): # პრდუქტის წაშლის ფუნქცია
    name = input("Which product do you want to remove: ")#ვეკითხებით თუ რისი წაშლა სურს
    for product in cart: #პროდუქტის სახელს ვეძებთ კალათაში
        if product["name"] == name:# თ სახელი ეხმთხვევა პროდუქტს 
            cart.remove(product) #ვშლით ლექსიკონიდან
            print(f"{name} was removed from cart") 
            return
    print("There is no such product") #სხვა შემთხვევაში ვწერთ რომ არ არის ასეთ პროდუქტი
def add_prod(cart):  #პროდუქციის დამატების ფუნქციონალი
    name, price, quantity = input("Enter Name, Price, and Quantity separately:  ").split() #შევიყვანეთ გავყავით
    price = float(price) #ფასი ფლოათად
    quantity = int(quantity) #რაოდენობა ინტეჯერად
    cart.append({"name": name, "price": price, "quantity": quantity}) #ლექსიკონში დამატება
    print(f"{name} was added to cart")

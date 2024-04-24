from add_product_to_cart import add_prod
from calc_total import calc_total
from preview_cart import view_cart
from remove_product_from_cart import remove_prod
   

def logic(): #ძირითადი ლოგიკა
    cart = [] #ვქმნით ცარიელ კალათას
    while True: #ვაძლევ მომხმარებელს ჩამონათვალს
        print("\n1. Add product to cart")
        print("2. View all products")
        print("3. Remove product from cart")
        print("4. Total price")
        print("5. Exit program")

        choice = input("Please chose what you want to do (Number): ") #ვაძლევთ საშუალებას რომ აირჩოს შესაბამისი ციფრი და დაბლა განვსაზღვრავთ ლოგიკას 
        #ზემოთ წინასწარ განსაზღვრული ფუნქციებით

        if choice == '1': #დამატება
            add_prod(cart)
        elif choice == '2':#ნახვა
            view_cart(cart)
        elif choice == '3':#წაშლა
            remove_prod(cart)
        elif choice == '4':#ჯამი
            calc_total(cart)
        elif choice == '5':#პროგრამიდან გასვლა
            print("Thank you and good luck")
            break
        else:
            print("Wrong choice")


logic() #ვიძახებთ ძირითად ფუნქციას
products={
    1:("laptop",50000),
    2:("mobile",20000),
    3:("headphone",1500),
    4:("keyboard",1000)
}
cart=[]
while True:
    print("\n====E-commerce store=====")
    print("1.View products")
    print("2. Add to cart")
    print("3. View cart")
    print("4. Checkout")
    print("5.Exit")
    
    choice=int(input("Enter your choice:"))
    if choice ==1:
        print("\nAvailable Products:")
        for pid,(name,price)in products.items():
            print(f"{pid}.{name}-${price}")
    elif choice==2:
        product_id=int(input("Enter Product ID:"))
        if product_id in products:
            cart.append(products[product_id])
            print("products added to cart!")
        else:
            print("invalid product Id")
    elif choice==3:
        if len(cart)==0:
            print("cart is empty!")
        else:
            print("\n your cart:")
            total=0
            for item in cart:
                print(item[0],"- $",item[1])
                total +=item[1]
            print("total = $",total)
    elif choice ==4:
        if len(cart)==0:
            print("cart is empty!")
        else:
            total=0
            print("\n order summary:")
            for item in cart:
                print(item[0],"- $",item[1])
                total +=item[1]
            print("total amount = $",total)
            confirm=input("confirm order(Y/N:")
            if confirm.upper()=="Y":
                print("order placed successfuly")
                cart.clear()
            else:
                print("order cancelled")
    elif choice==5:
        print("thank you for visiting!")
        break
    else:
        print("invalid choice!")

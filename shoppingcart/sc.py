cart=[]

cart.append("banana")
cart.append("apple")
cart.append("kiwi")
print(cart)

cart[1] = "fig"
print(cart)


cart.remove("banana")
print(cart)

print("cart after slicing",cart[1:3])

cart.sort()
print("cart after sorting",cart)

cart.reverse()
print("cart after reversing",cart)

if "fig" in cart:
    print("yes fig is in cart")
    
else:
    print("not in cart")
    
print("length of cart",len(cart))
    
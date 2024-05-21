pw={"User1":"123456789","Andrew":"Password123","Bob":"ABC123","Yusuf":"PQRSTuvw"}
x = input("Enter User name : ")
if(x in pw):
    y = input("Enter Pasword : ")
    if(y==pw[x]):
        print("You are successfully logged in")
    else:
        print("Incorrect password! ")
else:
    print("Username not found")
      


	
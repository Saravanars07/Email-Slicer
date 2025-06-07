email=input("Enter a email address:").strip()

#check if the eamil contains '@'
if "@" in email:
    #split the email and domain
    username=email[:email.index("@")]
    domain=email[email.index("@")+1:]
    print(f"Your username is:{username}")
    print(f"Your domain is {domain}")

else:
    print("Please enter a vaild Email id.")
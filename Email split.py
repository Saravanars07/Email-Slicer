# Its split method
email=input("Enter your email address:").strip()

if "@" in email:
    username,domain=email.split("@",1)
    print(f"Your username is:{username}")
    print(f"Your domain is:{domain}")
else:
    print("Please enter a valid Email address.")
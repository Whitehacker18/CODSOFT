import string
import random

def generate_password(length):
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    
    all_chars = lower + upper + digits + symbols
    
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
    
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length < 1:
            print("Length should be a positive integer.")
            
        
        password = generate_password(length)
        
        
        print("Generated Password:",password)
    
    except :
        print("Invalid input")
if __name__ == "__main__":
    main()

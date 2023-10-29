import hashlib
import time
import sys

def calculate_md5(input_str):
    
    md5_hash = hashlib.md5()
    input_bytes = input_str.encode('utf-8')
    md5_hash.update(input_bytes)
    md5_value = md5_hash.hexdigest()

    return md5_value

time.sleep(1.5)
print (""" 
    (¯`·.¸¸.·´¯`·.¸¸.-> Hash Maker <-.¸¸.·´¯`·.¸¸.·´¯)   
    (¯`·.¸¸.·´¯`·.¸¸.-> Hash Maker <-.¸¸.·´¯`·.¸¸.·´¯)
    (¯`·.¸¸.·´¯`·.¸¸.-> Hash Maker <-.¸¸.·´¯`·.¸¸.·´¯)
    (¯`·.¸¸.·´¯`·.¸¸.-> Hash Maker <-.¸¸.·´¯`·.¸¸.·´¯)
    --------------------------------------------------
    Manufacturer: SHAYAN ----> 'ERO-HACK'
    Version: 1.0
    telegram: https://t.me/eRohack123900+
    --------------------------------------------------
""")

time.sleep(3)

while True:
    
    user_input = input("Please enter the password of the feed ====>> ")
    result = calculate_md5(user_input)
    time.sleep(7)
    print(f'Your hash ====>> {result}')
    time.sleep(1)

    option = input("""
[1] Run Again 
[99] Exit
Which option ====>> """)

    if option == '1':
        continue
    elif option == '99':
        sys.exit()

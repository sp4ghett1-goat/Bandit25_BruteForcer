import base64
choice = str(input("do you want to encode or decode?? encode/decode: "))
choice = choice.lower()
if choice == "encode":
    def encode_pass(password):
        encoded_pass = base64.b64encode(password.encode())
        print(encoded_pass)
    user_pass = str(input("what is the password you want to encode? "))
    encode_pass(user_pass)
elif choice == "decode":
    def decode_pass(encrypted_pass):
        decoded_pass = base64.b64decode(encrypted_pass).decode()
        print(decoded_pass)
    coded_pass = str(input("what is the password you want to decode? "))
    decode_pass(coded_pass)
else:
    print("bro it's either encode or decode is it too hard for your small brain")
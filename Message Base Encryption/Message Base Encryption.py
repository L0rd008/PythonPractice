def convert_to_base(n, base):
    """Converts a given integer n to a specified base."""
    if n == 0:
        return '0'
    digits = []
    while n > 0:
        digits.insert(0, str(n % base)) #insert the remainder at the beginning of the list
        n //= base
    return ''.join(digits)

def encrypt_message(message, base):
    """Encrypts a message by converting each character's ASCII value to a given base."""
    encrypted_message = ''.join(convert_to_base(ord(char), base) for char in message)
    return encrypted_message

try:
    message_str = input('Enter message: ') #take the message to be encoded as input
    base_int = int(input('Enter base: ')) #take the preferred base for encoding as input
    if not (1 < base_int <= 10):  #check if the base is within the valid range
        raise ValueError("Base must be between 2 and 10.")
    encrypted_message = encrypt_message(message_str, base_int)
    print(encrypted_message) #print the encoded message
except ValueError as e:
    print(f"Invalid input: {e}")

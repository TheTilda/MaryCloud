import random 

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-'

def gen_hash(rang):
    text = ''
    for i in range(rang):
        text += random.choice(chars)
    return text

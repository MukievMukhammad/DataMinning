import re
import hashlib
import math

text = '''От улыбки хмурый день светлей, 
От улыбки в небе радуга проснется... 
Поделись улыбкою своей, 
И она к тебе не раз еще вернется. 

И тогда наверняка, вдруг запляшут облака, 
И кузнечик запиликает на скрипке... 
С голубого ручейка начинается река, 
Ну, а дружба начинается с улыбки. 
С голубого ручейка начинается река, 
Ну, а дружба начинается с улыбки. 

От улыбки солнечной одной 
Перестанет плакать самый грустный дождик. 
Сонный лес простится с тишиной 
И захлопает в зеленые ладоши. 

От улыбки станет всем теплей - 
И слону и даже маленькой улитке... 
Так пускай повсюду на земле, 
Будто лампочки, включаются улыбки! 
'''

def hash1(value):
    hash = int(hashlib.sha1(value.encode('utf-8')).hexdigest(), 16) % (10 ** 8)
    return hash % 321

def hash2(value):
    hash = int(hashlib.md5(value.encode('utf-8')).hexdigest(), 16) % (10 ** 8)
    return hash % 321


def main():
    bloom_filter = [0] * 321
    words = set(re.findall(r'[\w]+', text, re.U))
    print(len(words))
    for word in words:
        h1 = hash1(word)
        h2 = hash2(word)
        bloom_filter[h1] += 1
        bloom_filter[h2] += 1


if __name__ == "__main__":
    main()

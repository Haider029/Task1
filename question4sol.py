alphabet = input("please insert any alphabet : ")
alphabet=alphabet.lower()
if(alphabet >= 'A' and alphabet <= 'z'):
    if(alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u'  ):
        print("It is vowel")
    else: 
        print("It is consonent")
else:
    print("It is not an alphabet")

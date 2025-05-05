import string

abc = list(string.ascii_letters + string.punctuation)

upsideDown = ['ɐ','q','ɔ','p','ǝ','ɟ','ɓ','ɥ','ı','ɾ','ʞ','l','ɯ','u','o','d','b','ɹ','s','ʇ','n','ʌ','ʍ','x','ʎ','z',
              '∀','ᙠ','Ɔ','ᗡ','Ǝ','Ⅎ','⅁','H','I','ſ','⋊','˥','W','N','O','Ԁ','Ό','ᴚ','S','⊥','∩','Λ','M','X','⅄','Z',
              '¡','„','#','$','%','⅋',',',')','(','*','+',"'",'-','˙','/',':','؛','>','=','<','¿','@',']','\\','[',' ̮','¯',' ̖','}','|','{','~']

word = input('upsidedownify word: ')

reverseword = ''.join([word[x] for x in range(len(word)-1, -1, -1)])


for i in range(len(abc)):
    reverseword = reverseword.replace(abc[i], upsideDown[i])



print(reverseword)
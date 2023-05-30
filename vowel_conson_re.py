original = input('문자열을 입력하세요: ')
word = original.lower()
vowels=0
consonants=0
space=0
space2=0
if len(original)>0:
    for char in word:
        if char in 'aeiou' and char.isalpha():
            vowels=vowels+1
        elif char.isalpha():
            consonants=consonants+1
        elif char.isspace():
            space +=1
        else:
            space2 +=1
print("모음의 개수",vowels)
print("자음의 개수",consonants)
print("공백의 개수",space)
print("그 외의 개수",space2)
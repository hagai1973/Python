name_1 = input("type your name: ").lower()
name_2 = input("type second name: ").lower()
word_1 = "true"
word_2 = "love"
num_1 = 0
num_2 = 0



i = 0
j = 0



while i < len (word_1): 
 num_1 += name_1.count(word_1[i])
 num_1 += name_2.count(word_1[i])
 i+=1


while j < len (word_2): 
 num_2 += name_1.count(word_2[j])
 num_2 += name_2.count(word_2[j])
 j+=1

print(num_1)
print(num_2)

score = str(num_1)+str(num_2)
print(f"your score is: {score}")

scoreToInt = int(score)

if (scoreToInt < 10) or (scoreToInt > 90):
 print(f"your score is {score} your are not feet")
elif (scoreToInt >= 40) and (scoreToInt <= 50):
 print(f"your score is {score} your are ok")
else:
 print(f"your score is {score}")


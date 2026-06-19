import time

print("TYPING SPEED TEST")
sentence="Python is a very powerful programminglanguage"
print("\ntype this sentence exactly:\n")
print(sentence)

#start time
start_time=time.time()

#user input
typed_text=input("\n start typing:")

#end time
end_time=time.time()

#time taken
time_taken=end_time- start_time

#count words
word_count=len(typed_text.split())

#speed calculation
speed=(word_count/time_taken)*60

#Acuuray check#
if typed_text==sentence:
    accuracy=100
    result="Your sentence is correct "
else:
    correct_chars=0
    for i in range(min(len(sentence),len(typed_text))):
        if sentence[i]==typed_text[i]:
            correct_chars +=1
    accuracy=(correct_chars/len(sentence))*100
    result="Your sentence is not correct"
    

    
print("\n===========RESULT============")
print(result)
print("time taken:",round(time_taken,2),"seconds")
print("typing speed:",round(speed,2),"words per minute")
print("accuracy:",round(accuracy,2),"%")

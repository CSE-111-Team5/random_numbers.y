# Week 07 Team Activity due 06/01/2023
# worked on by Terral, Maria, 
#https://byui-cse.github.io/cse111-course/lesson07/teach.html

import random

def main():
    numbers = [16.2, 75.1, 52.3,]
    words_list = []
    print(numbers)
    append_random_numbers(numbers,)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)
    append_random_words(words_list, 3)
    print(words_list)

def append_random_numbers(alist, quantity=1):
    for _ in range(quantity):
        random_number = random.uniform(0,100)
        alist.append(round(random_number,1))


def append_random_words(alist, quantity=1):
   wordlist=['defiant','vigorous','unknown','laborer','soggy','handsome','correct','horrible','lame','synonymous','fix','jittery']
   
   for _ in range(quantity):
       random_word=random.choice(wordlist)
       alist.append(random_word) 
       
if __name__ == '__main__':
     main()
       
       
       
       
       # any questions i worked through it before that is what i keep refering to on the other tab :)
        #no its ok :D now i think we need to ... the words list. the words list is the strech did you want to do that?
        #oh yes well yes:D ok we can do that i had also done that on my practice through earlier today. but we should 
        # finish this one up first. Ok
        #YAY! It All worked and passed the test yes:D CONGRratulations to us! ok good night go get some rest for tomorrow. till next time. thakns same for you :D
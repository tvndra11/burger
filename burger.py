import threading
import random
import functionsforburger
foodlist = ['burger','fries','hotdog','cheeseburger','chicken','soda','slice of ham','pasta','smoothie','crisps']
print('intro here')

while money < 1000000: 
    while customers > 0:
        
        food = foodlist[random.randint(0,9)]
        print(food,'please')
        answer = ""
        while answer != food:
            answer = input("")
        print('order done')

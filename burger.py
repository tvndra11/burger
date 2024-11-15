import threading
import random
import functionsforburger
money = 0
customers = 0
timestring = threading.Thread(target=functionsforburger.customerline,time = 1)
timestring.start
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

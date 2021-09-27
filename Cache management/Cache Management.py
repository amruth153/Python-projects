#Student Name :Amruth Kanakaraj
#StudentID:201527965

#Simulating cache management system with two techniques 
#FIFO & LFU

# Global list  which stores the request when input from the user.
requests = []
# Gloabl List for cache
cache = []
# Global dictionary for LFU.
lfuCacheDic = {}

#Function to add & delete items to cache for FIFO.
def fifo() :
    fifo_pos = 0
    for rp in requests:    
        if rp in cache :
            print("HIT")
            print(cache)

        elif len(cache) < 8: #setting the size of the cache.
            cache.append(rp)
            print("MISS")
            print(cache)
        else :
            # If cache limit isn't reached, adding cache.
            print("MISS")
            cache[fifo_pos] = rp
            fifo_pos = (fifo_pos + 1) % 8
            print(cache)
    return 0


#Function to add & delete items to cache for LFU.
def lfu():
    for rp in requests:    
        if rp in cache :
            #adding of item isn't required if it's already there.
            print("HIT")
            print(cache)
            lfuCacheDic[rp] += 1
        elif len(cache) < 8 : #setting the size of the cache.
            cache.append(rp)
            print("MISS")
            print(cache)
            lfuCacheDic[rp] = 1
        else:
            round = 0
            for key in lfuCacheDic.keys() :
                if round == 0 :
                    small = lfuCacheDic[key]
                    small_key = key
                    round = 1
                
                elif small == lfuCacheDic[key] :
                    if small_key > key :
                        small_key = key
                
                elif small > lfuCacheDic[key] :
                    small = lfuCacheDic[key]
                    small_key = key
            #print statements thats shows miss and then updates the arrays / lists. 
            #also shows the current array and removes the least used cache. 
            print("MISS")
            print(cache)
            print("least used page is :", small_key,"used only ",small, "times")
            print("removing it")
            cache.remove(small_key)
            lfuCacheDic.pop(small_key)
            print("Adding", rp)
            cache.append(rp)
            lfuCacheDic[rp] = 1
            print(cache)
        
    return 0

#main functions to excute the whole program.
def main():
    print("This is your Cachemanagement system: \n")
    #input values from user stored as requests until & unless '0' is entered.
    while True:
        try:    
            print("Please enter your requests\n(after every request press enter, enter 0 to stop): ")
            while True:
                request = int(input())

                if request == 0:
                    break
                requests.append(request)
        #using try and except to make user enter proper input.
        except:
            print("error in input, Enter correct value")
            continue
        while True:   
            #prompting user to enter the request for cache management.
            choice = input("Enter options \n1.FIFO or 2.LFU or q to exit: \n")
            if choice == '1':
                fifo()
            elif choice == '2':
                lfu()
            elif choice == 'q':
                print("exiting")
                break
            else :
                print("invalid choice exit")
                #if invalid input is given then the program exits
                exit()
        
            cache.clear()
            lfuCacheDic.clear()
        requests.clear()
        #the user is asked wheather to continue the program or not, and accordingly exceuted.
        c = input("Do you want to continue program?(y/n)")
        if c == 'n':
            print("Program has now been terminated")
            exit()   
    
    return 0

#Calling main function
main()
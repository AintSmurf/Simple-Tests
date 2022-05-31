import numbers
import random
from this import d


def main():
    
    numbers =[x for x in range(12)]
    random.shuffle(numbers)
    print(numbers)
    print("List Of Numbers: \n\n")
    
    
    names = ['Johnny', 'Billy', 'John', 'Joe', 'Alexa']
    names.sort()
    print(names)
    print("List Of Names: \n\n")


    
    dic = {y:x for x,y in zip(numbers,names)}
    print(dic)
    print("Dictionary: \n\n")








if __name__ == '__main__':
    main()
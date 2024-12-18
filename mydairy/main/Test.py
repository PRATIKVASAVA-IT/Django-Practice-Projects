from random import randint,choices

f1='4 digit'
f2='3plainAlphabate'
f3='1 number and 1 alphabate'
f4='1 digit 1 specialchar 1 aplha'

'''
ff1=[chr(n) for n in range (65,122)]
print(ff1)

k=''
for i in range(4):
    k=randint(65,123)
    k=chr(k)
    print(k)
    




'''
def get_id():
    v=randint(1111-111-11-111,9999-999-99-999)
    return v





def  get_price(w,f,p):
     if type(w) and type(f) and type(p)=='int': 
          if (f>0) and (f <= 5) and (w<10):
               print('condition 1')
               a=w*p
               s=(w*p)*20/100
               p=a-s
               return p

          
        
          
          elif (f > 0) and (f <= 5) and (w>10):
                print('condition 2')
                a=w*p
                s=(w*p)*12/100
                p=a-s
                return p

          elif (f>5) and (f<=8) and (w <10):
                print('condition 3')
                a=w*p
                s=(w*p)*10/100
                p=a-s
                return p
          elif (f>5) and (f<=8) and (w>10):
                print('condition 4')
                a=w*p
                s=(w*p)*8/100
                p=a-s
                return p
          elif f==9:
                print('condition 5')
                return p*w
          elif f>=10:
                print('condition 6')
                
                a=w*p
                s=(w*p)*0.1
                p=a+s

        
                return p
     else:
          print('Enter Valid Input {Note: only Digit is allowed }')
     
     
# print(get_price(8,4.6,60)) #  condition 1      answer : 384
# print(get_price(14,4,60))  #  condition 2      answer:  739.2
# print(get_price(9,7,60)) #    condition 3        answer:  486
# print(get_price(20,7,60)) #   condition 4       answer:  1104
# print(get_price(5,9,60)) # condition 5        answer:  300
# print(get_price(30,9,60)) # condition 5        answer:  1800
#print(get_price(20,10,60))  # condition 6        answer: 1320

print(get_price(2,5,'pratik'))

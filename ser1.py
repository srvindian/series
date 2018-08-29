# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 21:29:59 2018

@author: Sourav
"""
def fibo(val=0):
    if (val==0 or val==1):
        return 1
    else: return fibo(val-1)+fibo(val-2) 
def nextprime(val=1):
    val+=1 
    while True:
       tag=1
       for i in range(2,val//2+1):
           if val%i==0:
               tag=0
               val+=1 
               break
       if tag==1:
           return val
       
if __name__=="__main__":
    n=int(input('enter term:'))
    j,k=0,1
    for i in range(1,n+1):
        if(i%2==1):
            print(fibo(j))
            j+=1
        else:
            k=nextprime(k)
            print(k)

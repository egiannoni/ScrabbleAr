# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:23:57 2020

@author: Victoria
"""

def charCount(word): 
    dict = {} 
    for i in word: 
        dict[i] = dict.get(i, 0) + 1
    return dict
  
  
def possible_words(lwords, charSet): 
    for word in lwords: 
        flag = 1
        chars = charCount(word) 
        for key in chars: 
            if key not in charSet: 
                flag = 0
            else: 
                if charSet.count(key) != chars[key]: 
                    flag = 0
        if flag == 1: 
            print(word) 
  
if __name__ == "__main__": 
    input = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run'] 
    charSet = ['e', 'o', 'b', 'a', 'm', 'g', 'l'] 
    possible_words(input, charSet) 
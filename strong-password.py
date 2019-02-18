#!/bin/python

import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    lst = { 'lower':0, 'upper':0, 'number':0, 'special':0}
    if len(password) < 6 :
        req_ln = 6 - len(password)
    else:
        req_ln = 
        
    for i in password:
        if i.isupper() == True:
            lst['upper'] = 
        elif i.islower() == True:

        elif i.isdigit() == True:
            lst['number'] = 
        else:
            lst['special'] = 
    #print lst, req_ln
    x = 
    for key, value in lst.iteritems():
        if value == 0:
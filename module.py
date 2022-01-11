# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 23:34:38 2021

@author: praveent

Purpose: 
    This module comprises of functions required to produce sum of numbers in a given list.
    
    The standard response format is a dictionary defined in the Global section.
    
"""
response = {'code':' ','total':'','Message':''}
def total_sum(numbers_to_add: list):
    '''This Function Reads in a list and calculates sum of elements of the list
       and create response messages and returns a response dictionary'''
    global response
    try:
        if len(numbers_to_add) == 0 :
            response['total']   = 'None'
            response['code']    = 'R01'
            response['Message'] = 'Input is Empty'
        else:
            response['total']   = str(sum(numbers_to_add))
            response['code']    = 'R00'
            response['Message'] = 'Success'
    except TypeError:
        response['total']   = 'None'
        response['code']    = 'R02'
        response['Message'] = 'Invalid Inputs Passed'
    return response

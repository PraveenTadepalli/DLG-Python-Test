# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 17:28:03 2022

@author: praveent

Purpose: This is a REST API, implements below resources
         1. /total : This retrieves a Total sum of integers supplied in 
                     the form of list

Change Log:

******************************************************************************
Changed By |Change purpose                              |Changed Date
Praveen T  |Initial Draft                               |11-01-2022 
******************************************************************************                     
"""
#import flask module and jsonify module from Flask framework
from flask import Flask,jsonify
#Import funtion total_sum
from module import total_sum

app = Flask(__name__)

@app.route('/')  
@app.route('/total')
def get_sum():
    numbers_to_add = list(range(10000001))
    resp = total_sum(numbers_to_add)
#Return total sum of all numbers as json response message, with http status 
#code 200
    return jsonify(resp),200

@app.errorhandler(500)
def internal_server_error(e):
    return str('Internal Server Error, Please contact support saps.prav9@gmail.com'),500

#Main Logic to trigger REST API.
if __name__ == "__main__":
    app.run(port=5000)

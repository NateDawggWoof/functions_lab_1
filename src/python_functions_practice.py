def return_10():
    return 10

def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def length_of_string(word):
    return len(word)

def join_string(str1,str2):
    return str1+str2

def add_string_as_number(num1,num2):
    return int(num1)+int(num2)

def number_to_full_month_name(num1):
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    return months[num1-1]

def number_to_short_month_name(num1):
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    return months[num1-1][0:3]

def volume_of_cube(side):
    return side**3

def reverse_string(string):
    return string[::-1]

def fahrenheit_to_celsius(fa):
    return (fa-32)/1.8
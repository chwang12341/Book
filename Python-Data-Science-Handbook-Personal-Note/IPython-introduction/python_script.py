## python_script.py

def multiply(a,b):
    '''a multiply of b'''
    
    return a*b


if __name__ == '__main__':
    
    for i in range(10):
        print(str(i) + ' multiply of ' + str(i+1) + ' : ' , multiply(i,i+1))
    

    
    
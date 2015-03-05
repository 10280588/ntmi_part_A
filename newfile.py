import sys

if __name__ == '__main__':
    filename = sys.argv[1]    
    f = open(filename + '.txt' ,'w')
    a = raw_input('is python good?')
    f.write('answer:'+str(a))
    f.close()
    
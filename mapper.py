#!/usr/bin/env python
import sys
# Mapper function
def mapper():
    for line in sys.stdin:
        values=line.strip().split()
        for value in values:
            try:
                num=float(value)
                print('%.2f\t%s' %(num,1)) # ouput(value,count)
            except ValueError:
                pass   # Ignore non numeric values


if __name__=="__main__" :
    mapper()

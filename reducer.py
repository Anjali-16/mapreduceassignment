#!/usr/bin/env python
import sys

# reducer function
def reducer():
    total_sum=0
    total_count=0

    for line in sys.stdin:
       value, count= line.strip().split('\t')
       total_sum += float(value) * int(count)
       total_count += int(count)
    
    if total_count > 0 :
        average = total_sum/total_count
        print('AVERAGE=%.2f' % average)
    else :
        print("No Numeric values found.")
if __name__=='__main__':
    reducer()



   
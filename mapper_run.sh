#!/bin/bash
/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files mapper.py,reducer.py \
-input /mapreduce/Assignment/test.txt \
-output /mapreduce/Assignment/output01 \
-mapper mapper.py \
-reducer reducer.py 


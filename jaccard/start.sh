
hadoop dfs -rm -r /user/hadoop/input 
hadoop dfs -copyFromLocal ../format-data/out /user/hadoop/input


hadoop dfs -rm -r /user/hadoop/output_temp &
hadoop dfs -rm -r /user/hadoop/output

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-file ./mapper1.py \
-mapper ./mapper1.py \
-file ./reducer1.py \
-reducer ./reducer1.py \
-input /user/hadoop/input/* \
-output /user/hadoop/output_temp

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-file ./mapper2.py \
-mapper ./mapper2.py \
-file ./reducer2.py \
-reducer ./reducer2.py \
-input /user/hadoop/output_temp/* \
-output /user/hadoop/output

rm -rf output
hadoop dfs -copyToLocal /user/hadoop/output
cat output/part-00000
cat output/part-00001
cat output/part-00002

rm -rf output_temp
hadoop dfs -copyToLocal /user/hadoop/output_temp
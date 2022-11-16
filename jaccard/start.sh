
hadoop dfs -rm -r /user/hadoop/input
hadoop dfs -rm -r /user/hadoop/output_temp
hadoop dfs -rm -r /user/hadoop/output
hadoop dfs -copyFromLocal ../format-data/out /user/hadoop/input

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-file /home/hadoop/jaccard/mapper1.py \
-mapper /home/hadoop/jaccard/mapper1.py \
-file /home/hadoop/jaccard/reducer1.py \
-reducer /home/hadoop/jaccard/reducer1.py \
-input /user/hadoop/input/* \
-output /user/hadoop/output_temp

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-file /home/hadoop/jaccard/mapper2.py \
-mapper /home/hadoop/jaccard/mapper2.py \
-file /home/hadoop/jaccard/reducer2.py \
-reducer /home/hadoop/jaccard/reducer2.py \
-input /user/hadoop/output_temp/* \
-output /user/hadoop/output
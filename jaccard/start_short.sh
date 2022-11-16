
hadoop dfs -rm -r /user/hadoop/input/short
hadoop dfs -copyFromLocal ../format-data/out/short /user/hadoop/input/short


hadoop dfs -rm -r /user/hadoop/output_short_temp &
hadoop dfs -rm -r /user/hadoop/output_short

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-file ./mapper1.py \
-mapper ./mapper1.py \
-file ./reducer1.py \
-reducer ./reducer1.py \
-input /user/hadoop/input/short/* \
-output /user/hadoop/output_short_temp

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-file ./mapper2.py \
-mapper ./mapper2.py \
-file ./reducer2.py \
-reducer ./reducer2.py \
-input /user/hadoop/output_short_temp/* \
-output /user/hadoop/output_short

rm -rf output_short
hadoop dfs -copyToLocal /user/hadoop/output_short
cat output_short/part-00000
cat output_short/part-00001
cat output_short/part-00002

rm -rf output_short_temp
hadoop dfs -copyToLocal /user/hadoop/output_short_temp
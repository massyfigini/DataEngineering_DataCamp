###############
# PySpark SQL #
###############

### Create a SQL table from a dataframe

# Load trainsched.txt
df = spark.read.csv("trainsched.txt", header=True)

# Create temporary table called table1
df.createOrReplaceTempView('table1')


### Determine the column names of a table

# Inspect the columns in the table df
spark.sql("DESCRIBE schedule").show()


### Running sums using window function SQL

# Add col running_total that sums diff_min col in each group
query = """
SELECT train_id, station, time, diff_min,
SUM(diff_min) OVER (PARTITION BY train_id ORDER BY time) AS running_total
FROM schedule
"""

# Run the query and display the result
spark.sql(query).show()


### Fix the broken query

query = """
SELECT 
ROW_NUMBER() OVER (ORDER BY time) AS row,
train_id, 
station, 
time, 
LEAD(time,1) OVER (ORDER BY time) AS time_next 
FROM schedule
"""
spark.sql(query).show()

# Give the number of the bad row as an integer
bad_row = 7

# Provide the missing clause, SQL keywords in upper case
clause = 'PARTITION BY train_id'


### Aggregation, step by step

# Give the identical result in each command
spark.sql('SELECT train_id, MIN(time) AS start FROM schedule GROUP BY train_id').show()
df.groupBy('train_id').agg({'time':'min'}).withColumnRenamed('MIN(time)', 'start').show()

# Print the second column of the result
spark.sql('SELECT train_id, MIN(time), MAX(time) FROM schedule GROUP BY train_id').show()
result = df.groupBy('train_id').agg({'time':'min', 'time':'max'})
result.show()
print(result.columns)


### Aggregating the same column twice

# Write a SQL query giving a result identical to dot_df
query = "SELECT train_id, min(time) as start, MAX(time) as end FROM schedule GROUP BY train_id"
sql_df = spark.sql(query)
sql_df.show()


### Aggregate dot SQL

# Obtain the identical result using dot notation 
dot_df = df.withColumn('time_next', lead('time', 1)
        .over(Window.partitionBy('train_id')
        .orderBy('time')))


### Convert window function from dot notation to SQL

# Create a SQL query to obtain an identical result to dot_df
query = """
SELECT *, 
(UNIX_TIMESTAMP(LEAD(time, 1) OVER (PARTITION BY train_id ORDER BY time),'H:m') 
 - UNIX_TIMESTAMP(time, 'H:m'))/60 AS diff_min 
FROM schedule 
"""
sql_df = spark.sql(query)
sql_df.show()
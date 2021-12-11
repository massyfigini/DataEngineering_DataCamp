########################################
# Downloading Data on the Command Line #
########################################

### Downloading single file using curl

# Use curl to download the file from the redirected URL
curl -L https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# Download and rename the file in the same step
curl -o Spotify201812.zip -L https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip


### Downloading multiple files using curl

# Download all 100 data files
curl -O https://s3.amazonaws.com/assets.datacamp.com/production/repositories/4180/datasets/files/datafile[001-100].txt

# Print all downloaded files to directory
ls datafile*.txt


### Downloading single file using wget

# Fill in the two option flags 
wget -c -b https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# Verify that the Spotify file has been downloaded
ls 

# Preview the log file 
cat wget-log


### Creating wait time using Wget

# View url_list.txt to verify content
cat url_list.txt

# Create a mandatory 1 second pause between downloading all files in url_list.txt
wget --wait=1 -i url_list.txt

# Take a look at all files downloaded
ls


### Data downloading with Wget and curl

# Use curl, download and rename a single file from URL
curl -o Spotify201812.zip -L https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# Unzip, delete, then re-name to Spotify201812.csv
unzip Spotify201812.zip && rm Spotify201812.zip
mv 201812SpotifyData.csv Spotify201812.csv

# View url_list.txt to verify content
cat url_list.txt

# Use Wget, limit the download rate to 2500 KB/s, download all files in url_list.txt
wget --limit-rate=2500k -i url_list.txt

# Take a look at all files downloaded
ls




#################################################
# Data Cleaning and Munging on the Command Line #
#################################################

### Installation and documentation for csvkit

# Upgrade csvkit using pip  
pip install --upgrade csvkit

# Print manual for in2csv
in2csv -h

# Print manual for csvlook
csvlook -help


### Converting and previewing data with csvkit

# Use ls to find the name of the zipped file
ls

# Use Linux's built in unzip tool to unpack the zipped file 
unzip SpotifyData.zip

# Check to confirm name and location of unzipped file
ls


### File conversion and summary statistics with csvkit

# Check to confirm name and location of the Excel data file
ls

# Convert sheet "Worksheet1_Popularity" to CSV
in2csv SpotifyData.xlsx --sheet "Worksheet1_Popularity" > Spotify_Popularity.csv

# Check to confirm name and location of the new CSV file
ls

# Print high level summary statistics for each column
csvstat Spotify_Popularity.csv 

# Check to confirm name and location of the Excel data file
ls

# Convert sheet "Worksheet2_MusicAttributes" to CSV
in2csv SpotifyData.xlsx --sheet "Worksheet2_MusicAttributes" > Spotify_MusicAttributes.csv

# Check to confirm name and location of the new CSV file
ls

# Print preview of Spotify_MusicAttributes
csvlook Spotify_MusicAttributes.csv


### Printing column headers with csvkit

# Check to confirm name and location of data file
ls

# Print a list of column headers in data file 
csvcut -n Spotify_MusicAttributes.csv


### Filtering data by column with csvkit

# Print a list of column headers in the data 
csvcut -n Spotify_MusicAttributes.csv

# Print the first column, by position
csvcut -c 1 Spotify_MusicAttributes.csv

# Print the first, third, and fifth column, by position
csvcut -c 1,3,5 Spotify_MusicAttributes.csv

# Print the first column, by name
csvcut -c "track_id" Spotify_MusicAttributes.csv

# Print the track id, song duration, and loudness, by name 
csvcut -c "track_id","duration_ms","loudness" Spotify_MusicAttributes.csv


### Filtering data by row with csvkit

# Print a list of column headers in the data 
csvcut -n Spotify_MusicAttributes.csv

# Filter for row(s) where track_id = 118GQ70Sp6pMqn6w1oKuki
csvgrep -c "track_id" -m 118GQ70Sp6pMqn6w1oKuki Spotify_MusicAttributes.csv


### Stacking files with csvkit

# Stack the two files and save results as a new file
csvstack SpotifyData_PopularityRank6.csv SpotifyData_PopularityRank7.csv > SpotifyPopularity.csv

# Preview the newly created file 
csvlook SpotifyPopularity.csv


### Chaining commands using operators

# If csvlook succeeds, then run csvstat 
csvlook Spotify_Popularity.csv && csvstat Spotify_Popularity.csv

# Use the output of csvsort as input to csvlook
csvsort -c 2 Spotify_Popularity.csv | csvlook

# Take top 15 rows from sorted output and save to new file
csvsort -c 2 Spotify_Popularity.csv | head -n 15 > Spotify_Popularity_Top15.csv

# Preview the new file 
csvlook Spotify_Popularity_Top15.csv


### Data processing with csvkit

# Convert the Spotify201809 tab into its own csv file 
in2csv Spotify_201809_201810.xlsx --sheet "Spotify201809" > Spotify201809.csv

# Check to confirm name and location of data file
ls

# Preview file preview using a csvkit function
csvlook Spotify201809.csv

# Create a new csv with 2 columns: track_id and popularity
csvcut -c "track_id","popularity" Spotify201809.csv > Spotify201809_subset.csv

# While stacking the 2 files, create a data source column
csvstack -g "Sep2018","Oct2018" Spotify201809_subset.csv Spotify201810_subset.csv > Spotify_all_rankings.csv




###########################################
# Database Operations on the Command Line #
###########################################

### Practice pulling data from database

# Verify database name 
ls

# Pull the entire Spotify_Popularity table and print in log
sql2csv --db "sqlite:///SpotifyDatabase.db" \
        --query "SELECT * FROM Spotify_Popularity" 

# Verify database name 
ls

# Query first 5 rows of Spotify_Popularity and print in log
sql2csv --db "sqlite:///SpotifyDatabase.db" \
        --query "SELECT * FROM Spotify_Popularity LIMIT 5" \
        | csvlook     

# Verify database name 
ls

# Save query to new file Spotify_Popularity_5Rows.csv
sql2csv --db "sqlite:///SpotifyDatabase.db" \
        --query "SELECT * FROM Spotify_Popularity LIMIT 5" \
        > Spotify_Popularity_5Rows.csv

# Verify newly created file
ls

# Print preview of newly created file
csvlook Spotify_Popularity_5Rows.csv


### Applying SQL to a local CSV file

# Preview CSV file
ls

# Apply SQL query to Spotify_MusicAttributes.csv
csvsql --query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" Spotify_MusicAttributes.csv

# Reformat the output using csvlook 
csvsql --query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" \
	Spotify_MusicAttributes.csv | csvlook

# Re-direct output to new file: LongestSong.csv
csvsql --query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" \
	Spotify_MusicAttributes.csv > LongestSong.csv
    
# Preview newly created file 
csvlook LongestSong.csv


### Cleaner scripting via shell variables

# Preview CSV file
ls

# Store SQL query as shell variable
sqlquery="SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1"

# Apply SQL query to Spotify_MusicAttributes.csv
csvsql --query "$sqlquery" Spotify_MusicAttributes.csv


### Joining local CSV files using SQL

# Store SQL query as shell variable
sql_query="SELECT ma.*, p.popularity FROM Spotify_MusicAttributes ma INNER JOIN Spotify_Popularity p ON ma.track_id = p.track_id"

# Join 2 local csvs into a new csv using the saved SQL
csvsql --query "$sql_query" Spotify_MusicAttributes.csv Spotify_Popularity.csv > Spotify_FullData.csv

# Preview newly created file
csvstat Spotify_FullData.csv


### Pushing data back to database

# Preview file
ls

# Upload Spotify_MusicAttributes.csv to database
csvsql --db "sqlite:///SpotifyDatabase.db" --insert Spotify_MusicAttributes.csv

# Store SQL query as shell variable
sqlquery="SELECT * FROM Spotify_MusicAttributes"

# Apply SQL query to re-pull new table in database
sql2csv --db "sqlite:///SpotifyDatabase.db" --query "$sqlquery" 


### Database and SQL with csvkit

# Store SQL for querying from SQLite database 
sqlquery_pull="SELECT * FROM SpotifyMostRecentData"

# Apply SQL to save table as local file 
sql2csv --db "sqlite:///SpotifyDatabase.db" --query "$sqlquery_pull" > SpotifyMostRecentData.csv



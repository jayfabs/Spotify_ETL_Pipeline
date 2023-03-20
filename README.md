Spotify New Music Friday ETL 🎵
=========

This project connects to the Spotify API to extract data from the "New Music Friday" playlist. The extracted data is then exported as a JSON file and loaded into a MongoDB database using Apache Airflow as the ETL (Extract, Transform, Load) tool.

Prerequisites
=========

To run this project, you will need the following:

A Spotify account and access to the Spotify API
Python 3 installed on your local machine
MongoDB installed on your local machine
Apache Airflow installed on your local machine
Astro CLI installed on your local machine
requirements.txt downloaded

Getting Started
====

Clone this repository to your local machine.
Create a virtual environment and activate it.
Install the required dependencies by running pip install -r requirements.txt in your terminal.
Set up your Spotify API credentials from the Spotify developer site.
Set up your MongoDB server, databse/collection and connection information using Mongodb Atlas.
Connect to Airflow using the Astro CLI
Verify dag is set up in Airflow and manual run the task
Verify that the data is being extracted from Spotify, transformed, and loaded into MongoDB by checking the logs in Airflow.


The ETL process is as follows:
======

### Extraction: 
The data is extracted from the "New Music Friday" playlist on Spotify using the Spotify API and a python script. This script uses the Spotipy python library to make that connection easy.
### Transformation: 
The extracted data is transformed into a JSON file.
### Loading: 
The JSON file is loaded into a MongoDB database using the load_data() function in mongo.py.
### Airflow Task
The Airflow task is scheduled to run every Friday at 2am est using a cron expression (0 6 * * 5). This ensures that new data from the "New Music Friday" playlist is automatically added to the database each week after the playlist is updated.

Conclusion
====

This project demonstrates how to use ETL to extract data from an API, transform it into a usable format, and load it into a database. By using Apache Airflow, the process can be automated and scheduled to run at a specified time, ensuring that the database is always up-to-date and grows.



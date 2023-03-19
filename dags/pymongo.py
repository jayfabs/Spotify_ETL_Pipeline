import os
import json
from pymongo import MongoClient
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from pendulum import datetime

#define the read and upload to mongodb task
#Using MongoDB Atlas to create the server
# Replace the username and password fields with your own 
def upload_to_mongo():
    # Create a MongoDB connection pool with a max pool size of 10
    client = MongoClient("mongodb+srv://<username>:<password>@cluster0.jiir8wj.mongodb.net/musicdb?retryWrites=true&w=majority")
    db = client['musicdb']
    playlist_df = db['playlist_df']
    print(f"Connected to MongoDB - {client.server_info()}")
    with open('/usr/local/airflow/dags/main_files/playlist.json') as f:
        data = json.load(f)
        playlist_df.insert_many(data)
    # Close the MongoDB connection when finished
    client.close()

#Define the default arguments replace the name with your own
default_args = {
    "owner": "name",
    "start_date": datetime(2022, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
}

#Define the task to run the python file located in main_files folder
def run_python_file():
    # Path to your Python file that needs to be executed
    file_path = '/usr/local/airflow/dags/main_files/main.py'
    # Execute the Python file
    exec(open(file_path).read())
    print("Python file has been executed successfully!")

#write the DAG pipeline 
with DAG(
    dag_id="run_main_upload_mongo",
    schedule='0 2 * * 5', # Runs every Friday at 2am
    default_args=default_args,
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id='run_python_task',
        python_callable=run_python_file,
        dag=dag
    )

    t2 = PythonOperator(
        task_id="upload_to_mongo",
        python_callable=upload_to_mongo,
        dag=dag
    )

    t1 >> t2

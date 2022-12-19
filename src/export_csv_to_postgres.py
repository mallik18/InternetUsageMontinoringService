""" Modules """
import logging
import os
import csv

import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv



load_dotenv()

logging.basicConfig(filename='logs/database.log',
                        level=logging.DEBUG)
while True:

    try:
        conn = psycopg2.connect(host=os.getenv('HOST'), dbname=os.getenv('DBNAME'),
                                user=os.getenv('POSTGRES_USER'), password=os.getenv('PASSWORD'),
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull!")
        logging.info("Database connection was successfull!")
        break
    except psycopg2.Error as err:
        print("Connecting to database failed", err)
        logging.error(err)


def insert_csvdata_in_postgresql():
    """ Insert csv data into postgresql database """
    with open('user_internet_session_dataset_for_mishipay_hackerearch_hiring_challenge_december_2022.csv',
                'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            cursor.execute("INSERT INTO userstats(username, mac_address, start_time, usage_time, upload, download) VALUES (%s, %s, %s, %s, %s, %s)",row)
    conn.commit()

insert_csvdata_in_postgresql()

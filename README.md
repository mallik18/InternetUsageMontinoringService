# InternetUsageMontinoringService

## HTTP Service for Internet Usage Monitoring Service:

## Platform Used:
- Linux, Ubuntu 22.04

## Framework Used:
- FastAPI (Python)

## Database Used:
- PostgreSQL Database:
    
    Download and Setup:                
    https://www.postgresql.org/download/linux/ubuntu/

    Install pgadmin4 to work with PostgreSQL GUI:
    
    https://www.pgadmin.org/download/pgadmin-4-apt/

## Setup:

1. Create python virtual environment with below command:
    - python3 -m venv venv

2. Acticate the following environment:
    - source venv/bin/activate

3. Install all the python packages with below command:
    - pip install -r requirements.txt

4. Setup the Database for further opeartions:
    - Open the PostgreSQL pgadmin and setup usename and password for login purposes.
    - Next create a Database named 'InternetUsersStats'.
    - To create tables in the database run the following command:
            
            - $psql create_database_tables.sql

    - The dataset used in the project is user_internet_session_dataset_2022.csv which has 6 columns named:
        1. username
        2. mac_address
        3. start_time
        4. usage_time
        5. upload
        6. download

## Objective:

To synchronize Flask database with the data from the HIS. Schema and sample data will be provided below....

## Assumption:
    * no changes can be made on the HIS side
    * HIS db server could be accessable thought internet
    * HIS side has no API to fetch the records but SQL query is applicable
    * HIS side db is SQLAlchemy compatible like Postgres/MySql/Sqlite. In this exmaple another Postgres instance was used

## Setup:
  * Project Directory: his_sync
  * Docker: docker folder
  * Flask app: app.py
  * Bluprint app: sync/sync.py

  Directory structure:
  .
  ├── README.md
  ├── app.py
  ├── config.py
  ├── conn.py
  ├── docker
  │   ├── Dockerfile
  │   ├── docker-compose.yml
  │   ├── his_data.sql
  │   └── requirements.txt
  └── sync
      ├── __init__.py
      ├── model.py
      ├── sync.py
      └── templates
          └── home.html

  ## Docker:
    * Please follow below steps 

      1. pgdb >> Flask app db:
          - port: 5432

      2. pgdb2 >> HIS side db:
          - port: 5434

      3. adminer >> for db navigation:
          - access >> 127.0.0.1:8080
          - login to pgdb2 (server: pgdb2,  user: postgres, password: His123)
          - open his_db
          - create table from sql command: file attached <his_db.sql>

      4. app >> For flask app: 
          - port: 5000
          - access path: 127.0.0.1:5000/sync


    Environment build steps:
    
    1. cd his_sync/docker
    2. docker-compose up --build
    3. db setup [Docker step 3]
    4. open browser > 127.0.0.1:5000/sync [If above steps works fine you will get synchorization interface]


## Comments: 
No policy was taken to change in HIS side. This given codes have been built only for quick challenge accomplishment but not for real life production version. It needs more work to make it more efficient in production version.

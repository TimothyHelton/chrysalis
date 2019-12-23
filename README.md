# Define System Variables
1. Copy the `envfile_template` to `envfile`
1. Enter your username and password for PGAdmin and Postgres

# PGAdmin Setup
1. From the main directory call `make pgadmin`
    - The default browser will open to `localhost:5000`
1. Enter the **PGAdmin** default user and password.
    - These variable are set in the `envfile`.
1. Click `Add New Server`.
    - General Name: Enter the <project_name>
    - Connection Host: Enter <project_name>_postgres
    - Connection Username and Password: Enter **Postgres** username and password
      from the `envfile`.

# PyCharm Setup
## Database Configuration
1. Make sure any new users are added to the database.
    ```postgresql
    GRANT CONNECT ON DATABASE chrysalis TO new_user;
    GRANT USAGE ON SCHEMA public TO new_user;
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO new_user;
    ```
1. `Database` -> `New` -> `Data Source` -> `PostgreSQL`
1. `Name`: chrysalis_postgres@localhost
1. `Host`: localhost
1. `Port`: 5432
1. `Database`: chrysalis
1. `User`: **Postgres** username
1. `Password`: **Postgres** password

1. `Settings` -> `Project` -> `Project Interpreter` -> point to docker compose file
1. Add the system variables defined in the `envfile` to the Project Interpreter

## Unit Test Configuration
1. `Run/Debug Configurations` -> `+` -> `Python tests` -> `pytest`
1. `Target` -> `Script path`
    - Enter the path to the project root directory.
1. Add the following to the `Additional Arguments` field:
    - `-vvv`
    - `-r all`
    - `--basetemp=pytest`
    - `--ff`
    - `doctest-modules`
        - To ignore specific modules add `--ignore=<module_name>`
1. Enter `Environment Variables` (PYTHONPATH, database user, ...)
1. Check Box -> `Add content roots to PYTHONPATH`
1. Check Box -> `Add source roots to PYTHONPATH`

# SNAKEVIZ Execution
1. Create profile file
    - Jupyter Notebook
        - `%prun -D profile.prof enter_cmd_or_file`
    - Command Line
        - `python -m cProfile -o profile.prof program.py`
1. Start server **from the command line** on port 10000
    - `snakeviz profile.prof --hostname 0.0.0.0 --port 10000 -s`
1. Open host web browser
    - `http://0.0.0.0:10000/snakeviz/`

# Memory Profiler
1. Open Jupyter Notebook
1. Load Extension
    - `%load_ext memory_profiler`
1. Run profiler
    - `%memit enter_code_here`

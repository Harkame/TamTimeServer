# TamTimeServer

Server of https://github.com/flyingrub/TamTime

Dependencies
=
Flask

Execution
=

(Execute all files from root (TamTimeServer))

python ./src/database/database_creation.py

python ./src/database/database_insertion.py

export FLASK_APP=src/server.py

flask run --host 0.0.0.0

OR

Run ./run.sh

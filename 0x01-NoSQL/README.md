NoSQL Project

This repository contains my solutions to the NoSQL project tasks as part of a specialization. The project involved working with MongoDB and Python to perform various database operations and develop scripts that interact with a MongoDB database.
Project Tasks

    List all databases: Script to list all databases in MongoDB.
    Create a database: Script to create or use the database my_db.
    Insert document: Script to insert a document in the collection school.
    All documents: Script to list all documents in the collection school.
    All matches: Script to list all documents with name="Holberton school" in the collection school.
    Count: Script to display the number of documents in the collection school.
    Update: Script to add a new attribute address to documents with name="Holberton school" in the collection school.
    Delete by match: Script to delete all documents with name="Holberton school" in the collection school.
    List all documents in Python: Python function to list all documents in a collection using PyMongo.
    Insert a document in Python: Python function to insert a new document in a collection based on kwargs using PyMongo.
    Change school topics: Python function to change all topics of a school document based on the name using PyMongo.
    Log stats: Python script to provide stats about Nginx logs stored in MongoDB.
    Regex filter: Script to list all documents with name starting by Holberton in the collection school.
    Top students: Python function to return all students sorted by average score using PyMongo.

Requirements

    Ubuntu 18.04 LTS
    MongoDB version 4.2
    Python 3.7
    PyMongo 3.10
    pycodestyle for Python code style enforcement

Setup

    Install MongoDB 4.2:

    shell

$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org

Install PyMongo:

ruby

    $ pip3 install pymongo

    Run Scripts: Each task script can be executed with MongoDB running and accessible.

Usage

    Clone the repository:

    shell

$ git clone https://github.com/your-username/alx-backend-storage.git

Navigate to the project directory:

shell

$ cd 0x01-NoSQL

Execute any script using MongoDB:

shell

    $ cat 0-list_databases | mongo

Notes

    Ensure MongoDB is running ($ sudo service mongod start) before executing the scripts.
    Each script is designed to perform a specific database operation as outlined in the task descriptions.
    Ensure proper permissions and dependencies are met according to the project specifications.

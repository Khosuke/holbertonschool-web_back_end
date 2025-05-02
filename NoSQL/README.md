# Project : NoSQL


### Task 0. List all databases
Write a script that lists all databases in MongoDB.

File: 0-list_databases

### Task 1. Create a database
Write a script that creates or uses the database my_db:

File: 1-use_or_create_database

### Task 2. Insert document
Write a script that inserts a document in the collection school:

The document must have one attribute name with value “Holberton school”
The database name will be passed as option of mongo command

File: 2-insert

### Task 3. All documents
Write a script that lists all documents in the collection school:

The database name will be passed as option of mongo command

File: 3-all

### Task 4. All matches
Write a script that lists all documents with name="Holberton school" in the collection school:

The database name will be passed as option of mongo command

File: 4-match

### Task 5. Count
Write a script that displays the number of documents in the collection school:

The database name will be passed as option of mongo command

File: 5-count

### Task 6. Update

Write a script that adds a new attribute to a document in the collection school:

The script should update only document with name="Holberton school" (all of them)
The update should add the attribute address with the value “972 Mission street”
The database name will be passed as option of mongo command

File: 6-update

### Task 7. Delete by match
Write a script that deletes all documents with name="Holberton school" in the collection school:

The database name will be passed as option of mongo command

File: 7-delete

### Task 8. List all documents in Python
Write a Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object

File: 8-all.py

### Task 9. Insert a document in Python
Write a Python function that inserts a new document in a collection based on kwargs:

Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id

File: 9-insert_school.py

### Task 10. Change school topics
Write a Python function that changes all topics of a school document based on the name:

Prototype: def update_topics(mongo_collection, name, topics):
mongo_collection will be the pymongo collection object
name (string) will be the school name to update
topics (list of strings) will be the list of topics approached in the school

File: 10-update_topics.py

### Task 11. Where can I learn Python?
Write a Python function that returns the list of school having a specific topic:

Prototype: def schools_by_topic(mongo_collection, topic):
mongo_collection will be the pymongo collection object
topic (string) will be topic searched

File: 11-schools_by_topic.py



### Task 12. Log stats
Write a Python script that provides some stats about Nginx logs stored in MongoDB:

Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status

File: 12-log_stats.py

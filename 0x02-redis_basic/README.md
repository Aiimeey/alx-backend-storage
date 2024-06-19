Redis Basic

This repository contains a set of exercises focused on integrating Redis into Python applications for caching and data storage. The tasks are designed to familiarize oneself with Redis functionalities such as storing strings, handling data types, using decorators for function counting and history logging, and implementing an expiring web cache.
Contents

    exercise.py: Contains the implementation of the Cache class and its methods, leveraging Redis for data storage and retrieval.
    main.py: Example usage demonstrating the functionalities implemented in exercise.py.
    web.py: Implementation of an advanced task involving web page caching using Redis with a 10-second expiration time.

Installation

To run the exercises, ensure you have Redis installed and Python 3.7 or higher. Use the following commands to set up your environment:

bash

$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf

Usage

Each task is implemented as a method within the Cache class. Example usage can be found in main.py.

bash

$ python3 main.py

Tasks Overview

    Writing strings to Redis: Implementing basic Redis operations, storing different data types.
    Reading from Redis and recovering original type: Retrieving data from Redis with type conversion.
    Incrementing values: Implementing a method call counter using Redis's INCR command.
    Storing lists: Storing history of inputs and outputs for functions using Redis lists.
    Retrieving lists: Displaying history of function calls stored in Redis keys.

Advanced Task:

    Implementing an expiring web cache and tracker: Caching web page content with Redis, tracking access counts and setting expiration times.


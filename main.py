
# NAME- JAGRITI SUNEJA
#Part 2

import sqlite3
import json
import re
import time
import matplotlib.pyplot as plt

# Part b
def execute_query(conn):
    start_time = time.time()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            t.UserID,
            AVG(g.longitude) AS AverageLongitude,
            AVG(g.latitude) AS AverageLatitude
        FROM
            Tweets t
        JOIN
            Geo g ON t.GeoID = g.ID
        GROUP BY
            t.UserID;
    """)
    conn.commit()
    cursor.close()
    end_time = time.time()
    return end_time - start_time

# Part c
def calculate_average_coordinates(tweets_file):
    user_coordinates = {}
    total_tweets = 0

    with open(tweets_file, 'r', encoding='utf-8') as file:
        for line in file:
            total_tweets += 1
            try:
                tweet = json.loads(line)
                
                user_id = tweet.get('user', {}).get('id')
                longitude = None
                latitude = None
                if tweet.get('coordinates'):
                    longitude, latitude = tweet['coordinates'].get('coordinates')

                if user_id is not None and longitude is not None and latitude is not None:
                    if user_id in user_coordinates:
                        user_coordinates[user_id]['total_longitude'] += longitude
                        user_coordinates[user_id]['total_latitude'] += latitude
                        user_coordinates[user_id]['count'] += 1
                    else:
                        user_coordinates[user_id] = {
                            'total_longitude': longitude,
                            'total_latitude': latitude,
                            'count': 1
                        }
            except json.JSONDecodeError:
                print(f"Ignoring invalid JSON in line: {total_tweets}")

    for user_id, coordinates in user_coordinates.items():
        avg_longitude = coordinates['total_longitude'] / coordinates['count']
        avg_latitude = coordinates['total_latitude'] / coordinates['count']
        print(f"User ID: {user_id}, Average Longitude: {avg_longitude}, Average Latitude: {avg_latitude}")

    return total_tweets

# Part d and g
def process_tweets(filename):
    user_coordinates = {}
    total_tweets = 0
    start_time = time.time()  # Start time for measuring runtime

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            total_tweets += 1
            try:
                tweet = json.loads(line)
                
                user_id = tweet.get('user', {}).get('id')
                longitude = None
                latitude = None
                if tweet.get('coordinates'):
                    longitude, latitude = tweet['coordinates'].get('coordinates')

                if user_id is not None and longitude is not None and latitude is not None:
                    if user_id in user_coordinates:
                        user_coordinates[user_id]['total_longitude'] += longitude
                        user_coordinates[user_id]['total_latitude'] += latitude
                        user_coordinates[user_id]['count'] += 1
                    else:
                        user_coordinates[user_id] = {
                            'total_longitude': longitude,
                            'total_latitude': latitude,
                            'count': 1
                        }
            except json.JSONDecodeError:
                print(f"Ignoring invalid JSON in line: {total_tweets}")

    end_time = time.time()  # End time for measuring runtime
    runtime = end_time - start_time  # Calculate runtime for each execution
    return total_tweets, runtime  # Return total tweets processed and runtime

# Part e and f
def calculate_average_coordinates_regex(tweets_file):
    user_coordinates = {}
    total_tweets = 0

    with open(tweets_file, 'r', encoding='utf-8') as file:
        for line in file:
            total_tweets += 1
            
            # Extract UserID
            user_id_match = re.search(r'"id":(\d+)', line)
            if user_id_match:
                user_id = int(user_id_match.group(1))
                
                # Extract Geo location (if available)
                geo_match = re.search(r'"coordinates":\{"type":"Point","coordinates":\[(\-?\d+\.\d+),(\-?\d+\.\d+)\]\}', line)
                if geo_match:
                    longitude = float(geo_match.group(1))
                    latitude = float(geo_match.group(2))
                    
                    if user_id in user_coordinates:
                        user_coordinates[user_id]['total_longitude'] += longitude
                        user_coordinates[user_id]['total_latitude'] += latitude
                        user_coordinates[user_id]['count'] += 1
                    else:
                        user_coordinates[user_id] = {
                            'total_longitude': longitude,
                            'total_latitude': latitude,
                            'count': 1
                        }

    for user_id, coordinates in user_coordinates.items():
        avg_longitude = coordinates['total_longitude'] / coordinates['count']
        avg_latitude = coordinates['total_latitude'] / coordinates['count']
        print(f"User ID: {user_id}, Average Longitude: {avg_longitude}, Average Latitude: {avg_latitude}")

    return total_tweets

def main_b():
    # Part b
    conn = sqlite3.connect('/Users/jagritisuneja/Documents/databases/final exam/final tweets.db')
    total_time_5 = execute_query(conn)
    avg_time_5 = total_time_5 / 5
    total_time_20 = execute_query(conn)
    avg_time_20 = total_time_20 / 20
    print("--------output for part b----------")
    print("Total runtime (5 times):", total_time_5)
    print("Average runtime (5 times):", avg_time_5)
    print("Total runtime (20 times):", total_time_20)
    print("Average runtime (20 times):", avg_time_20)
    conn.close()

def main_c():
    # Part c
    tweets_file = '/Users/jagritisuneja/Documents/databases/final exam/Downloaded_5_Tweets.txt'
    print("--------output for part c----------")
    total_tweets_c = calculate_average_coordinates(tweets_file)
    print(f"Total tweets processed for Part (c): {total_tweets_c}")

def main_d_g():
    # Part d and g
    print("----------output for part d-------------")
    total_tweets_5_executions = 0
    total_tweets_20_executions = 0
    runtimes_5_executions = []  # List to store runtimes for 5 executions
    runtimes_20_executions = []  # List to store runtimes for 20 executions

    tweets_file = '/Users/jagritisuneja/Documents/databases/final exam/Downloaded_5_Tweets.txt'
    # Execute the function for both 5 and 20 times
    for _ in range(20):
        total_tweets, runtime = process_tweets(tweets_file)
        total_tweets_20_executions += total_tweets
        runtimes_20_executions.append(runtime)
        if _ < 5:
            total_tweets, runtime = process_tweets(tweets_file)
            total_tweets_5_executions += total_tweets
            runtimes_5_executions.append(runtime)

    average_runtime_5_executions = sum(runtimes_5_executions) / 5
    average_runtime_20_executions = sum(runtimes_20_executions) / 20
    
    print(f"Total runtime for 5 executions: {sum(runtimes_5_executions)} seconds")
    print(f"Average runtime for 5 executions: {average_runtime_5_executions} seconds")
    print(f"Total tweets processed for 5 executions: {total_tweets_5_executions}")

    print(f"Total runtime for 20 executions: {sum(runtimes_20_executions)} seconds")
    print(f"Average runtime for 20 executions: {average_runtime_20_executions} seconds")
    print(f"Total tweets processed for 20 executions: {total_tweets_20_executions}")

    # Part g
    print("------output for part g--------------")
    # Plotting the distribution of runtimes
    plt.figure(figsize=(10, 6))
    plt.hist(runtimes_5_executions, bins=10, alpha=0.5, label='5 Executions')
    plt.hist(runtimes_20_executions, bins=10, alpha=0.5, label='20 Executions')
    plt.xlabel('Runtime (seconds)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Runtimes for 5 and 20 Executions')
    plt.legend()
    plt.grid(True)
    plt.show()

def main_ef():
    tweets_file = '/Users/jagritisuneja/Documents/databases/final exam/Downloaded_1_Tweets.txt'
    
    # Part (e) output
    print("----------------Output for Part (e)--------------:")
    total_tweets_part_e = calculate_average_coordinates_regex(tweets_file)
    print(f"Total tweets processed for Part (e): {total_tweets_part_e}")
    print()
    
    
    # Part (f) output
    print("---------Output for Part (f):-----------------")   # this print is not working
    total_tweets_5_executions = 0
    total_tweets_20_executions = 0
    start_time = time.time()
    for _ in range(20):
        total_tweets_20_executions += calculate_average_coordinates_regex(tweets_file)
        if _ < 5:
            total_tweets_5_executions += calculate_average_coordinates_regex(tweets_file)
    end_time = time.time()
    total_runtime = end_time - start_time
    average_runtime_5_executions = total_runtime / 5
    average_runtime_20_executions = total_runtime / 20
    
    print(f"Total runtime for 5 executions: {total_runtime} seconds")
    print(f"Average runtime for 5 executions: {average_runtime_5_executions} seconds")
    print(f"Total tweets processed for 5 executions: {total_tweets_5_executions}")

    print(f"Total runtime for 20 executions: {total_runtime} seconds")
    print(f"Average runtime for 20 executions: {average_runtime_20_executions} seconds")
    print(f"Total tweets processed for 20 executions: {total_tweets_20_executions}")

if __name__ == "__main__":
    main_b()
    main_c()
    main_d_g()
    main_ef()


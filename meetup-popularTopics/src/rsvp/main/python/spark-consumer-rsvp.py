'''
Program : spark-consumer-rsvp.py
Description: To find Top N trending topics from RSVP messages
Created on Jun 7, 2019


@author: ravi

Input: 
Use SPARK section of meetup-config.ini file to set desired input parameters as follows
top_n -> Number of trending topics
window_duration -> Per X amount of time (in secs)
slide_duration -> same as window_duration

Tasks: 
This Spark Streaming Consumer performs following tasks
1.Subscribe to 'meetup-rsvp' kafka topic to pull streaming data
2.Filter RSVP Response YES messages and extract topics from these messages
3.Find occurrence of each topic in each window duration per X amount of time (in secs)
4.Find TOP_N Trending topics and save TOP_N Trending topics as a text file on local file system
'''

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8-assembly_2.11:2.2.0,org.apache.spark:spark-streaming-kafka-0-8_2.11:2.2.0 pyspark-shell'

import json
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import ConfigParser
from collections import Counter

#Load parameters from meetup-config.ini configuration file
config = ConfigParser.RawConfigParser()
config.read('../../resources/meetup-config.ini')
ZK_QUORUM  = config.get('KAFKA', 'zookeeper_url')
KAFKA_MEETUP_RSVP_TOPIC = config.get('KAFKA', 'kafka_meetup_rsvp_topic')
BATCH_DURATION = config.getint('SPARK', 'batch_duration')
WINDOW_DURATION = config.getint('SPARK', 'window_duration')
SLIDE_DURATION = config.getint('SPARK', 'slide_duration')
TOP_N = config.getint('SPARK', 'top_n')
OUTPUT_PATH = config.get('SPARK', 'output_path')
RSVP_CHECKPOINT_PATH = config.get('SPARK', 'rsvps_checkpoint_path')

# Function to get all topics from RSVP response YES messages
def get_rsvp_yes_topics(jsonline):
    try:
        rsvp = json.loads(jsonline[1])
        if rsvp.get('response', None) == 'yes':
            group_topics = rsvp.get('group', {}).get('group_topics', {})
            rsvp_yes_topics = [d['topic_name'] for d in group_topics]
            return rsvp_yes_topics
    except ValueError as e:
        print('invalid json: %s' % e)
        return None

# Function to get Top N Trending Topics per X secs of time
def get_topN_trending_topics(rdd):
    top_n = rdd.sortBy(lambda pair: pair[1], ascending=False).take(TOP_N)
    return rdd.filter(lambda record: record in top_n)


'''---------------------------------Main Spark Streaming Section---------------------------------'''

#Set Spark Streaming Context
sc = SparkContext("local[*]",appName="Meetup-RSVP-Streaming")
sc.setLogLevel("ERROR")
ssc = StreamingContext(sc, BATCH_DURATION)

#Subscribe to 'meetup-rsvp' kafka topic to pull data
rsvpStream = KafkaUtils.createStream(ssc, ZK_QUORUM, "1", {KAFKA_MEETUP_RSVP_TOPIC: 1})

# Retrieve all topics with RSVP Response YES
rsvp_yes_topics = rsvpStream.map(get_rsvp_yes_topics).filter(lambda x: x is not None)

# Find occurrence of each topic in each window duration
all_rsvp_yes_topics = rsvp_yes_topics.flatMap(lambda x: x)
all_topics_pairs = all_rsvp_yes_topics.map(lambda topic: (topic, 1))

#topicCounts = all_topics_pairs.reduceByKey(lambda x, y: x + y)

topicCounts = all_topics_pairs.reduceByKeyAndWindow(func=lambda x,y:x+y,
                                     invFunc=lambda x,y:x-y,
                                     windowDuration=WINDOW_DURATION,
                                     slideDuration=SLIDE_DURATION)

# Find TOP_N Trending topics
topN_trending_topics = topicCounts.transform(get_topN_trending_topics)
#topN_trending_topics.pprint()

# Save TOP_N Trending topics as a text file on local file system
#topN_trending_topics.saveAsTextFiles('file:///D://tmp//trending-topics')
topN_trending_topics.saveAsTextFiles(OUTPUT_PATH)

# Enable periodic checkpointing of RDDs of this DStream required by reduceByKeyAndWindow
ssc.checkpoint(RSVP_CHECKPOINT_PATH)

# start Spark Streaming
ssc.start()
ssc.awaitTermination()

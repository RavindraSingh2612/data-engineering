'''
Program : kafka-producer-rsvp.py
Description: Poll RSVP messages from meetup stream API and publish to kafka_meetup_rsvp_topic 
Created on Jun 6, 2019

@author: ravi

Input: 
Use KAFKA section of meetup-config.ini file to set desired input parameters as follows
COUNTRY_FILTER -> Provide geographic filtering using country code


Tasks: 
This KAFKA Producer performs following tasks:
1.Poll RSVP streaming data from Meetup Stream API
2.Validate the incoming JSON data for correct JSON format
3.Provide geographic filtering using country_filter
4.Publish the output JSON data to 'meetup-rsvp' kafka topic
'''

from kafka import KafkaClient, SimpleProducer
import json,requests
import ConfigParser

#Load parameters from meetup-config.ini configuration file
config = ConfigParser.RawConfigParser()
config.read('../../resources/meetup-config.ini')
MEETUP_RSVP_API_URL = config.get('MEETUP', 'meetup_rsvp_api_url')
KAFKA_URL = config.get('KAFKA', 'kafka_url')
KAFKA_MEETUP_RSVP_TOPIC = config.get('KAFKA', 'kafka_meetup_rsvp_topic')
COUNTRY_FILTER = config.get('KAFKA', 'country_filter')

# Creating Kafka client
kafka = KafkaClient(KAFKA_URL)

#Creating a Kafka producer instance
rsvp_producer = SimpleProducer(kafka)

r = requests.get(MEETUP_RSVP_API_URL,stream=True)

# Sending valid JSON and geographically filtered messages to kafka topic 'meetup-rsvp' .
for line in r.iter_lines():
    try:
        jsonline=json.loads(line.decode('utf-8'))
        #print(jsonline['group']['group_country'])
        if(jsonline['group']['group_country'] == COUNTRY_FILTER):
            rsvp_producer.send_messages(KAFKA_MEETUP_RSVP_TOPIC,line)
    except ValueError as e:
        pass
        #print('invalid json: %s' % e)
kafka.close()
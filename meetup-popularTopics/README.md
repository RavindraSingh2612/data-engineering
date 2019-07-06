meetup-popularTopics 
------------------------------------------------------------------------------------
Distributed and Scalable solution to find Top N Most Popular Topics per X Amount of Time from meetup RSVP Stream Data using Spark Streaming and Kafka.

Data Source
------------------------------------------------------------------------------------
Meetup streaming API for RSVP
https://stream.meetup.com/2/rsvps


Project Features
------------------------------------------------------------------------------------
1.Discover top N popular topic per X amount of time where both N and X are configurable
2.Geographic filtering by country
3.Parameter to get Top N rending topics is configurable
4.Used window function in Spark Streaming to get popular topics per X amount of time
3.Handling of invalid JSON messages
4.All variables used in Kafka and Spark Streaming programs are configurable using 'meetup-config.ini' file
5.Batch scripts for Kafka components for testing using sample meetup.json file


Tools & Technologies Used and Reason behind my choices 
------------------------------------------------------------------------------------
1.Python   (Python 2.7.15)
2.Kafka    (kafka_2.12-2.0.0)
3.Spark Streaming  (spark-2.2.0-bin-hadoop2.7)
4.Spark Streaming + Kafka Integration (spark-streaming-kafka-0-8_2.11:2.2.0)
5.Kafka Python API
6.PySpark

1.Implementation Language Python is easy to use & debug and fun to code.
2.Kafka and Spark Streaming both provides features like distributability and scalability for fast processing of large set of data other than having fault-tolerant and High Performance.
3.I have setup the and executed the solution in local mode in Eclipse IDE on my machine but this solution can be scaled up


Run Instructions
------------------------------------------------------------------------------------
1.Set following desired parameters in 'meetup-config.ini' configuration file under resource folder
country_filter -> Provide geographic filtering using country code
top_n -> Number of popular topics
window_duration -> Per X amount of time (in secs)
slide_duration -> same as window_duration
kafka_meetup_rsvp_topic -> Kafka topic into which you want to publish RSVP message streams received from Meetup streaming API
output_path -> To store the result (Top N popular Topics)
rsvps_checkpoint_path -> To store checkpoints for Spark Streaming

2.Exceute 'kafka-producer-rsvp.py' program to poll RSVP streaming data from Meetup Stream API
3.Execute 'spark-consumer-rsvp.py' To find Top N popular topics from RSVP messages Per X amount of time (in secs)
4.Check results in output_path (Top N popular Topics!!).


Future Improvements
------------------------------------------------------------------------------------
1.Provide geographic filtering by city
2.Include event_name and group_name to improve discovery of popular topics
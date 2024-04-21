from azure.eventhub import EventHubProducerClient, EventData

connectionStr = "Endpoint=sb://ccdeveventhub.servicebus.windows.net/;SharedAccessKeyName=cucumber;SharedAccessKey=dMCEGhaL5z/QMl2LZD7rAhdpccer1chIn+b6zRA8dlA=;EntityPath=cctest"
eventHubName = "cctest"

# Create a producer client to send messages to the event hub
producer = EventHubProducerClient.from_connection_string(conn_str=connectionStr, eventhub_name=eventHubName)

# Create a batch
event_data_batch = producer.create_batch()

# Add events to the batch
event_data_batch.add(EventData('First event '))
event_data_batch.add(EventData('Second event'))
event_data_batch.add(EventData('Third event'))

# Send the batch of events to the event hub
producer.send_batch(event_data_batch)

# Close the producer client
producer.close()


# create stream analytics job

# create input
# create output
# create query

# start the job
# stop the job
# delete the job
# get the job status

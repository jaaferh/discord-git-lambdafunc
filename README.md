# AWS Lambda Function code for Discord Webhook

Executed from Github Webhook post request with Json payload details on push.
The lambda function then uses a Discord Webhook to send an embedded message with details from the Github payload.

The code is slightly edited to allow for local testing - discord_wh_url added as param to allow personal webhook url to be used.

Discord Webhook pip package needs to be installed locally, cleaned then zipped to be uploaded to AWS Lambda as a Layer:

```
pip3 install -t . discord-webhook
rm -r *dist-info __pycache__
```

Packages must be in a folder 'Python'. So the file dir should be something like this zipped_packages.zip > Python > discord_webhook 


## Testing locally

Can build docker image to test locally.
Example event.json included to simulate the JSON body that would be sent from Github through the Webhook
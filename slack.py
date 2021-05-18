import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import datetime
import sentiment        #Code to clean and assign sentiment to message

#Function to send slack message on the channel
def send_message(client, channel_id, sentiment_analysis):
    try:
        blocks=[]
        if sentiment_analysis>0:
            message_header = {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":large_green_circle:`Good going team! There is a positive vibe in the channel here.`:large_green_circle:"}
                    }
            blocks.append(message_header)

        elif sentiment_analysis<0:
            message_header = {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": ":red_circle:`It seems as if the team is facing some difficulties. Let us bring up the morale!`:smile:"}
                    }
            blocks.append(message_header)
        result = client.chat_postMessage(
            channel=channel_id,
            blocks=blocks)

    except SlackApiError as e:
        print(f"Error: {e}")

#Function to fetch messages in a given channel as old as an hour ago 
def fetch_messages(client, channel_id):
    timestamp_1_hr_ago = datetime.date.today() - datetime.timedelta(hours=1)
    unix_timestamp_1_hr_ago = timestamp_1_hr_ago.strftime("%s") 
    # Store conversation history
    conversation_history = []
    try:
        result = client.conversations_history(channel=channel_id, oldest=unix_timestamp_1_hr_ago, limit=1000)
        conversation_history = result["messages"]
        return conversation_history

    except SlackApiError as e:
        print(f"Error: {e}")

#Function to fetch conversation ID given channel name
def fetch_conversation(client, channel_name):
    conversation_id = None
    try:
        result = client.conversations_list()
        for response in result:
            if conversation_id is not None:
                break
            for channel in result["channels"]:
                if channel["name"] == channel_name:
                    conversation_id = channel["id"]
                    #Print result
                    print(f"Found conversation ID: {conversation_id}")
                    return conversation_id

    except SlackApiError as e:
        print(f"Error: {e}")

#Main function which fetches sentiment and calls all functions
def main():
    client = WebClient(os.getenv("SLACK_TOKEN"))
    channel_name = os.getenv(os.getenv("CHANNEL_NAME"))
    channel_id = fetch_conversation(client, channel_name)
    conversation_history = fetch_messages(client, channel_id)
    sentiment_analysis=0
    for message in conversation_history:
        sentiment_analysis += sentiment.get_sentiment(message["text"])
    sentiment_analysis = sentiment_analysis/len(conversation_history)
    send_message(client, channel_id, sentiment_analysis)
    

# calling main function
if __name__ == "__main__":
    main()

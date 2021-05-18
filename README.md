# slack_police

Slack Police is a slack application that sends out a slack message every one hour with the hourly sentiment on the channel. The Slack App needs to be added to the channel and ```channel:read``` and ```channel:write``` scopes are to be given to the bot.

## Running

You can set up an hourly cronjob by running adding the below line in the crontab file:

```0 * * * * <path_to_file>/slack.py```

### Output

![Alt text](/slack_screenshot.png?raw=true "Slack Screenshot")




 

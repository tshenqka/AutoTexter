import random, schedule, time

from twilio.rest import Client

# here we set up user details
cellphone = ""
twilio_number = ""
twilio_account = ""
twilio_token = ""

GOOD_MORNING_QUOTES = [
    "Good morning!"
]

GOOD_EVENING_QUOTES = [
    "Good evening!"
]


def send_message(quotes_list=GOOD_MORNING_QUOTES):

    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    quote = quotes_list[random.randint(0, len(quotes_list)-1)]

    client.messages.create(to=cellphone,
                           from_=twilio_number,
                           body=quote
                           )


# send a message in the morning
schedule.every().day.at("10:58").do(send_message, GOOD_MORNING_QUOTES)

# send a message in the evening
schedule.every().day.at("20:00").do(send_message, GOOD_EVENING_QUOTES)

# testing
schedule.every().day.at("13:55").do(send_message, GOOD_EVENING_QUOTES)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)

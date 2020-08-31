from csv_parser import get_parsed_csv
from send_email import compose_and_send_email
import datetime

def get_date():
    current_time=datetime.datetime.now()
    date_today=current_time.strftime("%d-%m")
    return date_today

def send_email(email_address):
    compose_and_send_email(email_address)

def check_birthday():
    today=get_date()
    user_data=get_parsed_csv()
    for user in user_data:
        if(user.get("DOB")[:5]==today):
            send_email(user)

check_birthday()
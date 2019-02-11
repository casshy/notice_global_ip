# -*- coding: utf-8 -*-

from googleapiclient.discovery import build
from global_ip import get_global_ip
from send_mail_via_gmail_api import get_credentials, create_message, send_message

sender = 'example@gmail.com'
to = 'example@gmail.com'
def main():
    # Get current global ip.
    gip = get_global_ip()
    
    # Load old global ip from file.
    # If file isn't exist, create new file.
    try:
        with open('old_global_ip.txt', 'r') as f:
            old_gip = f.read()
    except FileNotFoundError:
        with open('old_global_ip.txt', 'w') as f:
            f.write(gip)
            old_gip = ""

    if old_gip == gip:
        print("Global ip haven't been changed. {}".format(gip))
        return

    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)

    # Send a message.
    subject = "Your global ip is {}".format(gip)
    message_text = """{}""".format(gip)
    
    message = create_message(sender=sender,
                             to=to,
                             subject=subject,
                             message_text=message_text)
    send_message(service, 'me', message)

if __name__ == "__main__":
    main()

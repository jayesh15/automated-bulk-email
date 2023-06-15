# Email Automation Project

Author: Jayesh Jain
Website: [jayesh15.github.io](https://jayesh15.github.io)
Instagram: [jayeshhhjain](https://www.instagram.com/jayeshhhjain)
Twitter: [jayeshjainsays](https://twitter.com/jayeshjainsays)

## Project Description
This project aims to automate the process of sending emails using Python. It provides a streamlined solution for sending bulk emails to multiple recipients with different content types, including text, images, and attachments.

## Files Used
- `testemails.csv`: CSV file containing the list of recipient email addresses.
- `emailbodytext.txt`: Text file containing the email body content.

## Required Packages
- `smtplib`: For establishing an SMTP connection and sending emails.
- `email.mime`: For constructing email messages with various content types.
- `os`: For handling file paths.
- `pandas`: For reading recipient email addresses from the CSV file.
- `pathlib`: For reading the email body text file.

## How It Works
1. The project reads recipient email addresses from the `testemails.csv` file using `pandas` and stores them in a list.
2. The email body content is read from the `emailbodytext.txt` file.
3. The `message` function is used to construct the email message, including subject, text content, images (if any), and attachments (if any).
4. An SMTP connection is established with the Gmail server using `smtplib`.
5. The email is sent to the recipients using the `send_email` function, which utilizes the SMTP connection and the constructed email message.

## Configuration
To enable the project to send emails through Gmail, please make sure to enable the "Less secure apps" option in your Gmail account's security settings. You can access the settings at [https://www.google.com/settings/security/lesssecureapps](https://www.google.com/settings/security/lesssecureapps).

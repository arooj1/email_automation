import streamlit as st
import pandas as pd
import smtplib
import pywhatkit as kit
from google.oauth2.service_account import Credentials
import gspread

# Google Sheets setup
SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service_account.json'  # Path to your Google service account credentials JSON file

# Function to connect to Google Sheets
def connect_google_sheet(sheet_url):
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_url(sheet_url)
    worksheet = sheet.sheet1
    return pd.DataFrame(worksheet.get_all_records())

# Function to send an email
def send_email(sender_email, sender_password, recipient_email, subject, body):
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, recipient_email, message)

# Function to send a WhatsApp message
def send_whatsapp(number, message):
    kit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)

# Streamlit App UI
st.title("Email & WhatsApp Automation")
st.sidebar.title("Options")

# Upload and preview Google Sheet
if st.sidebar.button("Upload Google Sheet"):
    sheet_url = st.text_input("Enter the Google Sheet URL:")
    if sheet_url:
        try:
            data = connect_google_sheet(sheet_url)
            st.write("Preview of the Google Sheet:")
            st.dataframe(data)
        except Exception as e:
            st.error(f"Failed to load sheet: {e}")

# Draft Email
if st.sidebar.button("Draft Email / Preview"):
    recipient_name = st.text_input("Recipient Name:")
    recipient_email = st.text_input("Recipient Email:")
    subject = st.text_input("Subject:")
    email_body = st.text_area("Email Body:")
    if st.button("Preview Email"):
        st.write(f"To: {recipient_email}")
        st.write(f"Subject: {subject}")
        st.write(email_body)

# Send Email
if st.sidebar.button("Send Email"):
    sender_email = st.text_input("Your Email:")
    sender_password = st.text_input("Your Password:", type="password")
    if st.button("Send"):
        for _, row in data.iterrows():
            try:
                send_email(
                    sender_email,
                    sender_password,
                    row['email'],
                    subject,
                    email_body.replace("{name}", row['name'])
                )
                st.success(f"Email sent to {row['name']} ({row['email']})")
            except Exception as e:
                st.error(f"Failed to send email to {row['name']}: {e}")

# Send WhatsApp
if st.sidebar.button("Send WhatsApp"):
    message_body = st.text_area("WhatsApp Message Body:")
    if st.button("Send WhatsApp"):
        for _, row in data.iterrows():
            try:
                send_whatsapp(row['cell'], message_body.replace("{name}", row['name']))
                st.success(f"WhatsApp message sent to {row['name']} ({row['cell']})")
            except Exception as e:
                st.error(f"Failed to send WhatsApp message to {row['name']}: {e}")

# Schedule Options
if st.sidebar.button("Schedule"):
    st.write("Scheduling feature will be implemented soon!")

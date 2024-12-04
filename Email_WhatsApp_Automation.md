
# Email and WhatsApp Automation Application

## Purpose
The purpose of this repository is to automate the process of sending emails and WhatsApp messages to prospective leads.

---

## Features
1. **Connect to Google Sheets**: Load data from a Google Sheet.
2. **Preview Data**: Display the uploaded sheet data.
3. **Extract Fields**: Automatically extract the following fields:
   - Name
   - Email
   - Country of Destination
   - Program
   - Cell
4. **Send Emails**: Draft and send personalized emails to leads.
5. **Send WhatsApp Messages**: Automate personalized WhatsApp messages.
6. **Scheduling**: Future feature for scheduling messages and emails.
7. **Streamlit Interface**: A user-friendly application interface.

---

## Application Process Flow
1. **Connect** to a Google Excel Sheet.
2. **Read** the data into the application.
3. **Extract** the necessary fields for communication.
4. **Draft and Preview** the email or WhatsApp message.
5. **Send Emails** or **WhatsApp Messages**.
6. **Schedule** for future communications.

---

## Streamlit Application Mockup

### Sidebar Options:
- Upload Google Sheet
- Draft Email / Preview
- Send Email
- Send WhatsApp
- Schedule

### Main Screen Sections:
1. **Upload Section**: 
   - Preview the uploaded Google Sheet.
2. **Draft Email / Preview**:
   - Draft and preview email templates.
3. **Send Email**:
   - Confirm and send emails.
4. **Send WhatsApp**:
   - Confirm and send WhatsApp messages.
5. **Schedule**:
   - Placeholder for scheduling options.

---

## How to Use
1. Upload your Google Sheet URL through the application.
2. Preview the uploaded data in the application interface.
3. Draft and preview your email or WhatsApp message.
4. Use the respective buttons to send emails or messages.
5. Utilize the scheduling feature for planned communication (coming soon).

---

## Technologies Used
- **Python**
- **Streamlit**: For the front-end interface.
- **Google Sheets API**: For data integration.
- **SMTP**: For email automation.
- **PyWhatKit**: For WhatsApp automation.

---

## Running the Application
1. Install the required dependencies (see `Virtual_Environment_Setup.md`).
2. Save the Streamlit app code in a file named `streamlit_app.py`.
3. Run the application:
   ```bash
   streamlit run streamlit_app.py
   ```

---

## Future Enhancements
1. Add scheduling functionality for emails and WhatsApp messages.
2. Enhance the interface with themes and analytics.
3. Add more communication channels like SMS or Slack.

---

## Disclaimer
This application is for educational purposes only. Ensure compliance with privacy laws and communication regulations before use.

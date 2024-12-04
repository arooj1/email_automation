# Email_automation
## Purpose
The purpose of this repository is to automate the process of sending `email` and `whatsapp` messages to the **prospective leads**. 

## Process Flow 
- `Connect` to Google Excel Sheet
- `Read` Google excel sheet in python

- `Extract`  following fields:
    - `name`
    - `email`
    - `country_of_destination`
    - `program`
    - `cell`

- `Send` email to each name 
- `Send` message to each name


## Mockup

`Software`: Streamlit
- Screen-1: 
    - GQ Consultancy Banner with logo
    - options on the side bar
        - upload `google sheet`
        - draft email / preview
        - send email 
        - send whatsapp 
        - schedule 

    - Main screen will show the following:
        - upload 
            - preview of the google sheet

        - draft email / preview
            - preview of the drafted email / template

        - send email 
            - confirmation 
        - send whatsapp 
            - confirmation 
        - schedule 
            - options 
        

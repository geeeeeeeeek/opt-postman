# OPT Postman

_📮 Get email notification of OPT status & statistics every * days._

![image](https://user-images.githubusercontent.com/7262715/48309461-5cec1700-e52f-11e8-8da5-235461227ccf.png)

## How to Run

1. Get a long-running server and set up the environment. Install Python 3, `pip`, `git` and other basic tools.

2. Clone this repo or download a ZIP:

   ```shell
   git clone git@github.com:geeeeeeeeek/opt-postman.git
   ```

3. Install dependencies:

   ```shell
   pip3 install -r requirements.txt
   ```

4. Replace the parameters with your Gmail username and password:

   ```python
   send_email("{REPLACE_WITH_YOUR_GMAIL}", "{REPLACE_WITH_YOUR_PASSWORD}")
   ```

5. Schedule the script execution. You may want to test it locally first.

   ```shell
   # Run once
   python3 main.py
   
   # Scheduled execution
   crontab -e
   ```

   Add a line in the opened editor. The example below runs the script and sends an email at 8 am PST every morning. 

   ```shell
   00 16 * * * /usr/bin/python3 /home/ubuntu/main.py
   ```

## Data Source

1. Case status: https://egov.uscis.gov/casestatus/mycasestatus.do
2. Statistics: http://www.checkuscis.com/
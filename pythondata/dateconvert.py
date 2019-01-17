from datetime import datetime

raw_date = "2017-01-11"
date_format = "%Y-%m-%d"

# READ DATE
parsed_date = datetime.strptime(raw_date, date_format)

# SAVE DATE AS STRING
date_str = parsed_date.strftime("%m/%d/%y") # 01/11/17

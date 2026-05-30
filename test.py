
from data.database import *

reports = fetch_reports()

for report in reports:
    print(report)


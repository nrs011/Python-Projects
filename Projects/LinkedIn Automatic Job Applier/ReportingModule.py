import datetime as dt
import os
import pandas as pd

def saveReportAsCSV(df):
    saved_df = pd.DataFrame(df)
    saved_df.columns = ["Company Name", "Job Title", "Location", "Easy Apply", "Application Successful"]

    path = os.path.join(os.path.expanduser("~"),"Desktop","LinkedIn Automated Applications")
    if not os.path.exists(path):
        os.makedirs(path)

    datestr = dt.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    x = 'LinkedIn Applications {}.csv'.format(datestr)

    saved_df.to_csv(os.path.join(path, x), index=False)

    return saved_df
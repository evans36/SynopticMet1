"""
Script that scrapes data from the IEM ASOS download service

Origanally created by Iowa State University

Modified by: Michael Vossen
University of Wisconsin Milwaukee

"""
from __future__ import print_function
import json
import time
import datetime
from io import StringIO
import pandas as pd

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

# Number of attempts to download data
MAX_ATTEMPTS = 6
# HTTPS here can be problematic for installs that don't have Lets Encrypt CA
SERVICE = "http://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?"


def download_data(uri):
    """Fetch the data from the IEM
    The IEM download service has some protections in place to keep the number
    of inbound requests in check.  This function implements an exponential
    backoff to keep individual downloads from erroring.
    Args:
      uri (string): URL to fetch
    Returns:
      string data
    """
    attempt = 0
    while attempt < MAX_ATTEMPTS:
        try:
            data = urlopen(uri, timeout=300).read().decode("utf-8")
            if data is not None and not data.startswith("ERROR"):
                return data
        except Exception as exp:
            print("download_data(%s) failed with %s" % (uri, exp))
            time.sleep(5)
        attempt += 1

    print("Exhausted attempts to download, returning empty data")
    return ""



def download_alldata(ob_time):
    """
    A method to download one hour of data for the entire United States
    """
    # timestamps in UTC to request data for
    startts = ob_time
 
    interval = datetime.timedelta(hours=1)

    service = SERVICE + "data=metar&format=onlycomma&latlon=no&"

    now = startts

    thisurl = service
    thisurl += now.strftime("year1=%Y&month1=%m&day1=%d&hour1=%H&")
    thisurl += (now + interval).strftime("year2=%Y&month2=%m&day2=%d&hour2=%H&")
    thisurl += "&direct=no&report_type=3"
    
    
    print("Downloading: %s" % (now,))
    data = StringIO(download_data(thisurl))
    df = pd.read_csv(data)
    final_data = df["metar"]
    for count, value in enumerate(final_data):
        if value.find("METAR ") != -1:
            
            final_data.iloc[count] = value.replace("METAR ", "")
    data_file = StringIO()
    final_data.to_csv(data_file, sep="\n", index=False, header=False)
    return data_file



def download_alldata_save(ob_time):
    """
    A method to download one hour of data for the entire United States
    """
    # timestamps in UTC to request data for
    startts = ob_time
 
    interval = datetime.timedelta(hours=1)

    service = SERVICE + "data=metar&format=onlycomma&latlon=no&"

    now = startts

    thisurl = service
    thisurl += now.strftime("year1=%Y&month1=%m&day1=%d&hour1=%H&")
    thisurl += (now + interval).strftime("year2=%Y&month2=%m&day2=%d&hour2=%H&")
    thisurl += "&direct=no&report_type=3"
    
    
    print("Downloading: %s" % (now,))
    data = StringIO(download_data(thisurl))
    df = pd.read_csv(data)
    final_data = df["metar"]
    for count, value in enumerate(final_data):
        if value.find("METAR ") != -1:
            
            final_data.iloc[count] = value.replace("METAR ", "")
    
    final_data.to_csv(f"{ob_time:%Y%m%d_%H}.txt", sep="\n", index=False, header=False)
    
    
   

if __name__ == "__main__":
    date = datetime.datetime(2022,9,14,0)
    download_alldata_save(date)

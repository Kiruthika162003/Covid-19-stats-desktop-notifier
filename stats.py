!pip install win10toast
import requests
from win10toast import ToastNotifier
import datetime

try:
    data = requests.get("https://api.covid19india.org/data.json")  # covid19india database
except:
    print("Check your internet connection")
    data = None

if data is not None:
    getData = data.json()
    covid_India = getData["cases_time_series"]  # national level data
    covid_India1 = getData["statewise"]
    title= """Kiruthika's COVID-19 India Live  {}""".format(datetime.date.today())
    n = len(covid_India)
    a = covid_India[n-1]  # yesterday data
    b = covid_India1[0] # current data
    l1 = list(b.values())
    l = list(a.values())
    tconf = l1[3]  # today's confirmed
    conf = l1[1]
    active = l1[0]
    deaths = l1[2]
    recov = l1[7]
    m1 = "Total cases: %s " % conf + "\n"
    m5 = "Active cases not yet recovered: %s " %active +" | "
    m2 = "Total Deaths in India: %s " % deaths + "\n"
    m3 = "Total Recovered: %s " % recov + "\n"
    m4 = "Today's confirmed cases: %s" % tconf
    message = m1 + m5 + m2 + m3 + m4
    toaster = ToastNotifier()
    toaster.show_toast(title, message, icon_path="corona.ico", duration=100)

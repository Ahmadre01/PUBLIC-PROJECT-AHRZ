from datetime import datetime
def show_time_now():
    """ This function returns the current date and time. """
    # Get the current date and time 
    time = datetime.now()
    # Display the year, month
    # day (1-31), hour (0-23), minute, and second
    print("Year: ", time.year)
    print("Month: ", time.month)
    print("Day: ", time.day)
    print("************************************")
    print("Hour: ", time.hour)
    print("Minute: ", time.minute)
    print("Seconds : ", time.second)
    FORMAT_DATE = "{:%Y-%m-%d , %H:%M:%S}".format(time)
    print("************************************")
    # show time of now  in "YYYY/MM/DD HH 
    return  "Full date = "+ FORMAT_DATE+" \n************************************"

print(show_time_now())

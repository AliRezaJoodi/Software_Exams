# https://github.com/AliRezaJoodi
def add_time(start_time, duration, start_day=""):

    #Separte the start into hours and minutes
    buffer = start_time.split()
    time_clock = buffer[0].split(":")
    time_format = buffer[1]

    #Convertor 12-hour clock format to 24-hour 
    if time_format == "PM" :
        hour = int(time_clock[0]) + 12
        time_clock[0] = str(hour)
    
    #Separate the duration to hours and minutes
    duration_time = duration.split(":")

    #Initial calculation of hours and minutes
    hour_new = int(time_clock[0]) + int(duration_time[0])
    minute_new = int(time_clock[1]) + int(duration_time[1])

    #Edit hour and minute value
    if minute_new >= 60 :
        hours_add = minute_new // 60
        minute_new = minute_new - (hours_add * 60)
        hour_new = hour_new + hours_add
    days_add = 0
    if hour_new > 24 :
        days_add = hour_new // 24
        hour_new = hour_new - (days_add * 24)
    
    #Detector of the clock format
    if 0 <= hour_new and hour_new < 12:
        time_format = "AM" 
    else:
        time_format = "PM" 
   
    #Convertor 24-hour clock format to 12-hour
    if hour_new > 12 :
        hour_new = hour_new - 12
    elif hour_new ==0 :
        hour_new = hour_new +12

    #Calculation new day
    if days_add == 0 :
        days_letter = ""
    elif days_add == 1 :
        days_letter = " (next day)"
    else :
        days_letter = " (" + str(days_add) + " days later)"

    #Calculate the day of the week
    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    if start_day :
        weeks_add = days_add // 7
        i = week_days.index(start_day.lower().capitalize()) + (days_add - (7 * weeks_add))
        if i > 6 : i = i- 7
        days_new = ", " + week_days[i]
    else :
        days_new = ""

    #Final pack
    if minute_new <= 9 :
        minute_new="0" + str(minute_new)
    else :
        minute_new=str(minute_new) 
    hour_new=str(hour_new)   
    new_time= hour_new + ":" + minute_new + " " + time_format + days_new + days_letter
    
    return new_time
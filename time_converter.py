miliseconds = 1000
seconds = 60
minute = 60
hour = 60
day = 24
try:
    sec = raw_input('Enter time to convert in seconds.\n> ')
    sec = float(sec) if sec else float(1)
    msec = sec * miliseconds
    min = sec / minute
    hr = min / hour
    dy = hr / day
    print msec, 'Miliseconds\n', sec, 'Seconds\n', min, 'Minutes\n', hr , 'Hours\n', dy, 'Days'
except TypeError:
    print 'Please enter a numeric Value.'
except ValueError:
    print 'Please enter a numeric Value.'

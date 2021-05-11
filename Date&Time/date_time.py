#Date Time

from datetime import datetime, timedelta
from time import strftime

def main():
    now = datetime.now()
    utc = datetime.utcnow()

    print(f'NOW: {now}')
    print(f'UTC: {utc}')
    print(f'Offset: {now.utcoffset()}')

    #Time
    print(f'Hour: {now.hour}')
    print(f'Minute: {now.minute}')
    print(f'Sec: {now.second}')
    print(f'uSec: {now.microsecond}')

    #Date
    print(f'Year: {now.year}')
    print(f'Month: {now.month}')
    print(f'Day: {now.day}')

    #Deltas
    print(f'Next Month: {now + timedelta(days=30)}')
    print(f'Last Week: {now + timedelta(weeks=-1)}')

    #ISO strings
    d = datetime.fromisoformat('2020-12-16')
    print(d)

    try:
        m = datetime.fromisoformat('20-20-20')
        print(m)
    except Exception as ex:
        print(ex.args)

    print(f'ISO: {now.isoformat()}')

    print(now.strftime('%y'))
    print(now.strftime('%Y'))
    print(now.strftime('%d'))
    print(now.strftime('%D'))
    print(now.strftime('%b'))
    print(now.strftime('Today is %B %d'))

if __name__ == '__main__':
    main()
    
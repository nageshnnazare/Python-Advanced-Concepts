# Dir Stats
# Simple app for scanning the drirectories recursively

#imports and globals
import os

stats = dict(path='', folders=0, files=0, links=0, size=0)

# get user input
def get_input():
    global stats
    ret = os.path.abspath(input('Enter the Folder Path : '))

    if not os.path.exists(ret):
        print(f'Sorry that path does not exist')
        exit(1)
    if not os.path.isdir(ret):
        print(f'Sorry that path is not a directory')
        exit(2)
    
    stats['path'] = ret

# Scan the path recursively
def scan(path):
    global stats
    print(f'Scanning: ' + path)

    #Millions of ways to do this
    for root, dirs, files in os.walk(path, onerror=None, followlinks=False):
        stats['folders'] += len(dirs)
        stats['files'] += len(files)

        for name in files:
            fullname = os.path.join(root, name)
            size = os.path.getsize(fullname)
            stats['size'] += size

# Display
def display():
    global stats
    print('Results')

    for k,v in stats.items():
        print(f'{k} : {v}')

# Main Function
def main():
    global stats
    get_input()
    scan(stats['path'])
    display()

if __name__ == "__main__":
    main()
import re
import datetime
import time
import eel




eel.init("web")

@eel.expose
def python(name):
    eel.callpython(name)

print("hello")
eel.start("Simple.html",mode="edge", block = False)
eel.sleep(1.0)
# Open the SRT file
with open('file.txt', 'r', encoding='utf-8') as f:
    subtitles = f.readlines()

# Initialize variables
current_sub = 0
start_time = None
end_time = None

# Compile a regular expression to extract the time components from the time stamp string
#time_regex = re.compile(r'(\d\d):(\d\d):(\d\d),(\d\d\d)')

# Iterate through the lines of the SRT file
while current_sub < len(subtitles):
    # Read the next line
    line = subtitles[current_sub].strip()

    # If the line is a time stamp, parse the start and end times
    if '-->' in line:
        start_time, end_time = map(str.strip,line.split('-->'))
        start_time = re.match(r'(\d\d):(\d\d):(\d\d).(\d\d\d)' ,start_time).groups()
        end_time = re.match(r'(\d\d):(\d\d):(\d\d).(\d\d\d)' ,end_time).groups()
        start_time = datetime.datetime(1, 1, 1, int(start_time[0]), int(start_time[1]), int(start_time[2]), int(start_time[3])*1000)
        end_time = datetime.datetime(1, 1, 1, int(end_time[0]), int(end_time[1]), int(end_time[2]), int(end_time[3])*1000)

    # If the line is not a time stamp and not empty, it is the text of the subtitle
    elif line:
        # Print the text of the subtitle
        
        eel.spk(line)

        # Set the start time of the subtitle
        start = time.perf_counter()

        # Wait until the end time of the subtitle
        while time.perf_counter() - start < (end_time - start_time).total_seconds():
            time.sleep(0.01)

    # Move to the next line in the SRT file
    current_sub += 1



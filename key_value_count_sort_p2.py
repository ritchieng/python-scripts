# Collate list of timings and counts, sort, and find most/least common timings in an email log
# This script uses mbox.txt to give you an example of how it might work

# 1. Prompt for file to load
fname = raw_input('Enter file name: ')

# 2. File handle to access file
fhandle = open(fname)

# 3a. Create counts dictionary
counts = dict()

# 3b. Create variable to determine which word you want to seek for the start of each sentence
x = 'From'

# 4. Loop through file
for line in fhandle:
    # 5. Split each line to have list of words
    words = line.split()

    # Guardian pattern to ensure blank lines are skipped
    if len(words) < 1:
        continue

    # You do not want any sentence not starting with x
    if words[0] != x:
        continue

    # print words
    # Will show you that [5] gives you time of email

    # 6. Seek the time
    time_all = words[5]

    # 7. Seek the hour
    time_all = time_all.split(':')
    time_hr = time_all[0]

    # print time_hr
    # Will show you that you have retrieved the hours

    # 8. Map key-value pairs to dictionary counts
    # i. If there is no count for the word, add 0
    # ii. If there is count for the word, add 1
    counts[time_hr] = counts.get(time_hr, 0) + 1

# 9. Convert dictionary to tuples
counts = counts.items()

# 10. Sort list of tuples in ascending order (earliest to latest)
counts_sorted = sorted(counts)

# 11. Print list of tuples using loop
for time, count in counts_sorted:
    print time, count




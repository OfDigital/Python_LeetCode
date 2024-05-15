def leastInterval(tasks: list[str], n: int) -> int:
    # Initialize a list to store frequencies of tasks (26 letters of the alphabet)
    freq = [0] * 26
    # Initialize variables to keep track of maximum frequency and count
    max_count = 0
    max_freq = 0
    
    # Iterate through the tasks list
    for task in tasks:
        # Update the frequency count of the current task
        freq[ord(task) - ord('A')] += 1
        
        # Update max_count and max_freq if necessary
        if max_freq == freq[ord(task) - ord('A')]:
            max_count += 1
        elif max_freq < freq[ord(task) - ord('A')]:
            max_freq = freq[ord(task) - ord('A')]
            max_count = 1

    # Calculate the number of gaps needed between tasks
    gap_count = max_freq - 1
    # Calculate the length of each gap
    gap_length = n - (max_count - 1)
    # Calculate the total number of empty slots between tasks
    empty = gap_count * gap_length
    # Calculate the number of available tasks to be scheduled
    available_tasks = len(tasks) - max_freq * max_count
    # Calculate the number of idle slots required
    idles = max(0, empty - available_tasks)

    # Return the total number of slots required
    return len(tasks) + idles

# Test the function
print(leastInterval(tasks=["A","A","A","B","B","B"], n=2))

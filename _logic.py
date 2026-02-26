print("Enter a large integer : ")
totalSeconds = int(input())
hours = totalSeconds // 3600


remainingAfterHours = totalSeconds % 3600

minutes = remainingAfterHours // 60

seconds = remainingAfterHours % 60

print(totalSeconds, "seconds is", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")
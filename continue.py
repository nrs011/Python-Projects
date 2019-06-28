numbersTaken = [2, 5, 12, 13, 17]

print("Here are the numbers that are still avaliable")

for n in range(1, 20):
    if n in numbersTaken:
        continue  # whenever you get to this point, the next line is skipped and the next iteration starts
    print(n)

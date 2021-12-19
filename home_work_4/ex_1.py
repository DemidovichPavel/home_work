from sys import argv


work_hours = int(argv[1])
hours_cost = int(argv[2])
prize = int(argv[3])
my_prize = prize / 100
earn = ((work_hours * hours_cost) + (work_hours * hours_cost) * my_prize)
print(earn)

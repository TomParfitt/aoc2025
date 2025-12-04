
def question1():
  password = 0

  with open('day03-2.txt') as file:

    for line in file:
      line = line.rstrip('\n')
      print(line)
      battery_1 = 0
      battery_2 = 0
      count = len(line)
      for idx in range(count):
        battery = int(line[idx])
        if idx != count-1 and battery > battery_1:
          battery_1 = battery
          battery_2 = int(line[idx+1])
        elif battery > battery_2:
          battery_2 = battery
      password += int(str(battery_1) + str(battery_2))

  return password


def question2():
  password = 0



  return password


print(f'Question 1 answer: {question1()}')
print(f'Question 2 answer: {question2()}') #25912654282

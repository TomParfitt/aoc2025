

def question1():
    position = 50
    password = 0

    with open('day01-2.txt') as file:
        for line in file:
            direction = line[0:1]
            count = int(line[1:])

            if direction == 'L':
                position -= count
            else:
                position += count

            if position % 100 == 0:
                password += 1

    print(password)
    # 992


def question2():
    position = 50
    password = 0

    with (open('day01-2.txt') as file):
        for line in file:
            direction = line[0:1]
            count = int(line[1:])

            full_turns = count // 100
            remainder = count % 100

            if remainder != 0:
                started_on_zero = position == 0
                partial_turns = 0

                if direction == 'L':
                    position -= remainder
                    if not started_on_zero and position <= 0:
                        partial_turns = 1
                else:
                    position += remainder
                    if not started_on_zero and position >= 100:
                        partial_turns = 1

                position = abs(100+position) % 100

            password = password + full_turns + partial_turns

    print(password)
    # 6133

question1()
question2()
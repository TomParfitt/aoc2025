

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

    return password


def question2():
    prev_position = 50
    password = 0

    with (open('day01-2.txt') as file):
        for line in file:
            direction = line[0:1]
            count = int(line[1:])

            full_turns, remainder = divmod(count, 100)

            if remainder != 0:
                new_position = prev_position - remainder if direction == 'L' else prev_position + remainder
                partial_turns = 0 if prev_position == 0 or 0 < new_position < 100 else 1
                prev_position = abs(100 + new_position) % 100

            password += full_turns + partial_turns

    return password


print(f'Question 1 answer: {question1()}')
print(f'Question 2 answer: {question2()}')

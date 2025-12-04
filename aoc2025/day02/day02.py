# Idea - create a map of tuple -> count. (assuming overlapping)
# key = start and end block
# value = how many product ranges have those ides
def question1():
  password = 0

  with open('day02-2.txt') as file:
    for line in file:
      product_ranges = line.split(',')

  for product_range in product_ranges:
    start, end = [int(s) for s in product_range.split('-')]

    for product_id in range(start, end + 1):
      product_id_str = str(product_id)
      if len(product_id_str) % 2 == 1:
        continue
      elif is_repeated(product_id_str):
        password += product_id

  return password


def is_repeated(product_id_str):
  if len(product_id_str) % 2 == 1:
    return False

  mid = len(product_id_str) // 2
  first_half = product_id_str[:mid]
  second_half = product_id_str[mid:]
  return first_half == second_half

# could change this to find out size
# ... get count divisor
# ... create string with first section * remaining
# ... check if equal
def question2():
  password = 0

  with open('day02-2.txt') as file:
    for line in file:
      product_ranges = line.split(',')

  for product_range in product_ranges:
    start, end = [int(s) for s in product_range.split('-')]

    for product_id in range(start, end + 1):
      product_id_str = str(product_id)
      if is_repeated(product_id_str):
        password += product_id
      else:
        # loop through half of the product_id
        for count_of_chars in range(1, len(product_id_str) // 2 + 1):

          repetitions, remainder = divmod(len(product_id_str), count_of_chars)

          if remainder != 0:
            # cant repeat if it doesn't divide cleanly
            continue
          pattern = product_id_str[0:count_of_chars]

          if (pattern * repetitions) == product_id_str:
            password += product_id

  return password


print(f'Question 1 answer: {question1()}')
print(f'Question 2 answer: {question2()}') #25912654282

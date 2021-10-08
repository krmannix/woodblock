from gutenberg.acquire import load_etext
from gutenberg._domain_model.exceptions import UnknownDownloadUriException

def ebook_exists(id):
  try:
    load_etext(id)
    return True
  except UnknownDownloadUriException:
    return False

def max_ebook_identifier(id, known_max, upper_limit):
  if abs(id - known_max) <= 1:
    return min(id, known_max) - 1

  if ebook_exists(id):
    known_max = max(id, known_max)

    if id >= upper_limit:
      next_id = id * 2
      upper_limit = id
    else:
      next_id = int((upper_limit - known_max) / 2) + known_max

    return max_ebook_identifier(next_id, known_max, upper_limit)
  else:
    next_id = int((id - known_max) / 2) + known_max
    return max_ebook_identifier(next_id, known_max, id)

print('calculating number of books')
result = max_ebook_identifier(30100, 1, 1)

print(f'there are {result} books')

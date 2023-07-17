import re

def match_12_hour_time(text):
    pattern = r"^(1[0-2]|0?[1-9]):[0-5][0-9]\s?(?:AM|PM|am|pm)$"
    match = re.match(pattern, text)
    return match is not None

# Test cases
print(match_12_hour_time("12:34 AM"))    # Output: True
print(match_12_hour_time("09:27 PM"))    # Output: True
print(match_12_hour_time("3:45am"))      # Output: True
print(match_12_hour_time("07:60 PM"))    # Output: False
print(match_12_hour_time("10:15 AM"))    # Output: True
print(match_12_hour_time("13:20 pm"))    # Output: False


def check_web_address(url):
  pattern = r"^(https?://)?(www\.)?[\w.-]+\.[a-zA-Z]{2,}(?:/[\w.-]*)*$"
  match = re.search(pattern, url)
  return match is not None


# Test cases
print(check_web_address("https://www.example.com"))  # Output: True
print(check_web_address("http://example.com"))  # Output: True
print(check_web_address("www.example.com"))  # Output: True
print(check_web_address("example.com"))  # Output: True
print(check_web_address("https://example.com/page"))  # Output: True
print(check_web_address("example"))  # Output: False
print(check_web_address("ftp://example.com"))  # Output: False
print(check_web_address("www.youtube.com"))  # Output: True
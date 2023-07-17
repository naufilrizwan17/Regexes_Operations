import re

ans1 = re.findall(r"[a-zA-Z]{3}", "The weather is fantastic, let us go and play outside.")
print(ans1)

ans2 = re.findall(r"\b[a-zA-Z]{2}","The tide is very high.")
print(ans2)

ans3 = re.findall(r"[0-9]", "I have slept for more than 3 hours.")
print(ans3)

ans4 = re.findall(r"\w{5,}", "How about some strawberries?")
print(ans4)

ans5 = re.findall(r"\d{4}", "There were 1000 mangoes and 2500 oranges filled in the carts.")
print(ans5)

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package update"
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex,log_line)
    if result is None:
        return ""
    return result[1]

print(extract_pid(log))
print(extract_pid("The mouse is in the [hole]"))

ans6 = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
print(ans6)

def validate_email(email):
    email_pattern = re.sub(r"[\w.-]+@[\w.-]+", "[REDACTED", email)
    return email_pattern

validate_email("naufil.rizwan17@gmail.com")

def validate_URL(URL):
    URL_pattern = re.search(r"(http:?)\.(www:?)\.([A-Za-z0-9_])\.(a-z)", URL)
    return URL_pattern

validate_URL("youtube.com")


def find_consecutive_vowels(text):
    pattern = r'\b\w*[aeiou]{3}\w*\b'  # Regex pattern to match words with 3 consecutive vowels
    matches = re.findall(pattern, text, re.IGNORECASE)

    for match in matches:
        print(match)


# Example usage:
text = "I have a beautiful day. The rain is pouring outside."
find_consecutive_vowels(text)


def convert_phone_number(phone):
    result = re.sub(r"(\d{3})-(\d{3})-(\d{4})", r"(\1) \2-\3", phone)
    if result == phone:
        return phone
    else:
        return result

print(convert_phone_number("My number is 212-345-9999."))  # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234"))  # Please call (888) 555-1234
print(convert_phone_number("123-123-12345"))  # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300"))  # Phone number of Buckingham Palace is +44 303 123 7300.

def convert_phone_number(phone):
    pattern = r"(\d{3})-(\d{3})-(\d{4})"
    match = re.search(pattern, phone)
    if match:
        return "({}) {}-{}".format(match.group(1), match.group(2), match.group(3))
    else:
        return phone

print(convert_phone_number("My number is 212-345-9999."))  # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234"))  # Please call (888) 555-1234
print(convert_phone_number("123-123-12345"))  # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300"))  # Phone number of Buckingham Palace is +44 303 123 7300.

def check_username(username):
    pattern = r"[A-Za-z0-9_]{10}"
    result = re.search(pattern,username)
    if result:
        ans = "The username: {} is valid".format(username)
        return ans
    else:
        ans = "The username: {} is invalid".format(username)
        return ans

print(check_username("topg_gamer"))
print(check_username("Rauf_pro45"))
print(check_username("Harry_w8"))
print(check_username("DadaG69"))
print(check_username("Salma-rocks"))
print(check_username("farhan74"))
print(check_username("Hot_girl27"))
print(check_username("rehanrules"))
print(check_username("money$mind"))
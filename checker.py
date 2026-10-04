import re
import hashlib
import requests
def strength_checker(password: str):
    password = re.sub(r"\s+", "", password)
    has_upper = bool(re.search(r"[A-Z]",password))
    has_lower = bool(re.search(r"[a-z]",password))
    has_numbers = bool(re.search(r"[0-9]",password))
    has_special = bool(re.search(r"[^\w\s]",password)) or ("_" in password)
    more_than_12 = len(password) >= 12
    checks = {
        "At least 12 characters": more_than_12,
        "Has upper case": has_upper,
        "Has lower case": has_lower,
        "Has numbers": has_numbers,
        "Has special characters": has_special,
    }
    # Validates password complexity and length requirements
    is_strong = all(checks.values())
    return is_strong, checks

def check_breach(password: str):
    sha1_pass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix,suffix = sha1_pass[:5],sha1_pass[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data: {response.status_code}")

    for line in response.text.splitlines():
        resp_suffix, count = line.split(':')
        if resp_suffix == suffix:
            return int(count)

    return 0

if __name__ == "__main__":
    password = str(input("Enter your password: "))
    strong, checks = strength_checker(password)
    pawned = check_breach(password)
    if strong:
        print("✅ Password is Strong.")
    else:
        print("⚠️⚠️ Password is NOT Strong.")
        print("Missing requirements:")
        for requirement, met in checks.items():
            if not met:
                print(f"  - {requirement}")

    if pawned == 0:
        print("✅ Password not found in any known data breaches.")
    else:
        print(f"⚠️⚠️ Password found in data breaches {pawned} times")








from collections import Counter

def validateMessage(message: str = None, chest: str = None) -> bool:
    
    message = message.replace(" ", "").lower()
    chest = chest.replace(" ", "").lower()

    required = Counter(message)
    found = Counter()    

    needed = sum(required.values())
    have = 0

    for char in chest:
        # Checks the correct character is found
        if char in required and found[char] < required[char]:
            found[char] += 1
            have += 1

            # Checks the total amount of characters is found
            if have == needed:
                return True

    return False
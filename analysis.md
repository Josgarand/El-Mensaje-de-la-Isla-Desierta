   # Technical Analysis
   ## Time Complexity (Big O)

   Let `m` be the length of the message and `c` the length of the chest.

   Here’s what the function does step by step:

   1. **Normalize text**
      - We remove spaces and make everything lowercase. Each string is scanned once.
      - Time: O(m + c)

   2. **Count characters**
      - We use `Counter` to count how many times each character appears in the message.
      - Time: O(m)

   3. **Sum needed characters**
      - We calculate how many total characters we need from the message.
      - Time: O(m)

   4. **Search in the chest**
      - We go through the chest one character at a time.
      - If a character is needed, we keep track of how many times we’ve seen it.
      - The loop stops early if we already found everything.
      - Worst case: we check the whole chest.
      - Time: O(c)

   ### Final Time Complexity

   **O(m + c)**

   ---

   ## Space Complexity (Memory)

   Two dictionaries (`Counter`) are used to keep track of character counts:

   - `required`: holds the character frequencies from the message.
   - `found`: keeps track of how many required characters have been found in the chest.

   The number of possible characters is limited (letters, digits, and accented characters), so the number of keys is bounded in practice.

   ### Final Space Complexity:

   **O(k)**, where `k` is the number of unique characters in the message (practically constant).  
   Effectively: **O(1)**

   ---

   ## Data Structures

   - The function uses `Counter` from the `collections` module to store the number of times each character appears in the message (`required`).
   - To track how many valid characters have been found so far (`found`).
   - A running counter (`have`) and a total needed count (`needed`) allow for early exit from the loop.

   ---

   ## Trade-offs

   - **Simplicity**: The code remains clean and readable while achieving better performance.
   - **Efficiency**: The function ends as soon as the message can be formed, which improves performance in many cases.
   - **Memory usage**: Uses two dictionaries `Counter` efficiently, without extra data structures.

   ---

   ## Edge Cases Considered

   - Ignores if the character is uppercase or lowercase
   - Handles accented characters
   - Efficient with large input like 1 million characters or more
   - Spaces are ignored
   - Works with numbers
   - Special characters like `#` are supported
   - Works with other character languages

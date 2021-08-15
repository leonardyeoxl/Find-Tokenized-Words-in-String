# Find Tokenized Words in String

## Problem

### What are Tokenized Words?

1. Words without space. For example, abc, def, a, b, c
2. Quoted words with or without space. For example, "qwerty asd zxcv", "abc", "a"

### Example Input and Output

#### Example 01

- Input: asd def qwe "qwerty asd zxcv" asf "tyuip dfhgdj fgh"
- Output: ['asd', 'def', 'qwe', '"qwerty asd zxcv"', 'asf', '"tyuip dfhgdj fgh"']

#### Example 02

- Input: "qwerty asd zxcv"
- Output: ['"qwerty asd zxcv"']

#### Example 03

- Input: asd def qwe
- Output: ['asd', 'def', 'qwe']

## Solution

See `solution.py`.

### Time and Space Complexity

- Time Complexity: O(N*N-1). Given N is the number of characters in the string
- Space Complexity: O(M). Given M is the number of valid word token in an array.
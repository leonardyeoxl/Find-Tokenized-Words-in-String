# Time Complexity: O(N*N-1). Given N is the number of characters in the string
# Space Complexity: O(M). Given M is the number of valid word token
def FindTokens(S):
    tokens = []
    if len(S) == 0:
        return tokens
    
    QUOTE_COUNT_MAX_IN_WORD_TOKEN = 2
    QUOTE = '"'
    WHITESPACE = ' '

    quote_count = 0
    left_ptr = 0
    right_ptr = 1
    while left_ptr < len(S) or right_ptr < len(S):
        # checking if word is a valid token. For example, abc
        if S[left_ptr] != WHITESPACE and S[left_ptr] != QUOTE:
            while right_ptr < len(S) and S[right_ptr] != WHITESPACE:
                right_ptr += 1
            tokens.append(S[left_ptr:right_ptr])
        
        # checking if word is a valid token with quotes. For example, "abc def xyz"
        elif S[left_ptr] == QUOTE and S[left_ptr] != WHITESPACE and quote_count == 0:
            quote_count += 1
            
            while right_ptr < len(S):
                if S[right_ptr] == QUOTE:
                    quote_count += 1
                    break
                right_ptr += 1
                
            if quote_count == QUOTE_COUNT_MAX_IN_WORD_TOKEN:
                tokens.append(S[left_ptr:right_ptr+1])
            
            quote_count = 0
            right_ptr += 1
        
        left_ptr = right_ptr
        right_ptr += 1
    
    return tokens

if __name__ == "__main__":
    S = 'asd def qwe "qwerty asd zxcv" asf "tyuip dfhgdj fgh"'
    arr = FindTokens(S)
    assert arr == ['asd', 'def', 'qwe', '"qwerty asd zxcv"', 'asf', '"tyuip dfhgdj fgh"'], "solution invalid for {}".format(S)

    S = '"qwerty asd zxcv"'
    arr = FindTokens(S)
    assert arr == ['"qwerty asd zxcv"'], "solution invalid for {}".format(S)

    S = 'asd def qwe'
    arr = FindTokens(S)
    assert arr == ['asd', 'def', 'qwe'], "solution invalid for {}".format(S)
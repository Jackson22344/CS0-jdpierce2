def solution(s: str):

    if 'ss' in s:
        return "hiss"
    else:
        return "no hiss"

input_string = input()

print(solution(input_string))

# Assert statements to test solution function
assert(solution("hiss") == "hiss")        
assert(solution("kattis") == "no hiss")   
assert(solution("kiss") == "hiss") 
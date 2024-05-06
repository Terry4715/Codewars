#%%
print("Hello, World!")
# %%

#kata #1 - https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python

def make_negative(number):
    return 0 - abs(int(number))

# number = input("Enter any number to make it negative: ")
# print(make_negative(number))

#kata #2 - https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

boolean = True
print(bool_to_word(boolean))

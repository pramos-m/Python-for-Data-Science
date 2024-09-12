# None: Represents the absence of value.
# NaN (Not a Number): Represents an undefined number.
# 0: Can be considered "null" or empty.
# Empty string "": Can also be considered as "null".
# False: Boolean value that can be considered as "null".

import math

def NULL_not_found(obj: any) -> int:
    if obj is None:
        print(f"Nothing: {obj} {type(obj)}")
    elif isinstance(obj, float) and math.isnan(obj):
        print(f"Cheese: {obj} {type(obj)}")
    elif obj == 0:
        print(f"Zero: {obj} {type(obj)}")
    elif obj == "":
        print(f"Empty: {obj} {type(obj)}")
    elif obj is False:
        print(f"Fake: {obj} {type(obj)}")
    else:
        print("Type not found")
        return 1
    return 0

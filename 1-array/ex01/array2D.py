import numpy as np

def slice_me(family: list, start: int, end: int) -> list:

    try:
        arr = np.array(family, dtype='f')
        print(f'My shape is : {np.asarray(family).shape}')
        res = arr[start:end]
        print(f'My new shape is : {np.asarray(res).shape}')
        return (res)
    except Exception as err:
        print("Error:", err)

# Just as we can use square brackets to access individual array elements, we can also use them to access subarrays with the slice notation, marked by the colon (:) character. The NumPy slicing syntax follows that of the standard Python list; to access a slice of an array x, use this:

# x[start:stop:step]
# If any of these are unspecified, they default to the values start=0, stop=size of dimension, step=1.

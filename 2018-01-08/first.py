print('Hello World')

def add(num1,num2):
    return(num1+num2)

print(add(2,3))


# compute the volume of a cube

def cube_volume(length, width, height):
    return (length*width*height)

def mean(numbers):
    return(sum(numbers)/len(numbers))

def median(numbers):
    """Compputes the medain of a list of numbers

    arguments:  list of numbers
    return: the median

    >>> median([2,1,6])
    2
    >>> median([3,5,4,9])
    4.5

    """
    len_num = len(numbers)
    x=sorted(numbers)
    mid = len_num //2
    if len_num%2 == 1:
        return(x[mid])
    else:
        return(sum(x[mid-1:mid+1])/2)


def mode(numbers):
    """Find the most common value in a list

    argument:  list of numbers
    returns: the mode

    >>> mode([1,2,2,2,3,3,4])
    2

    """
    from collections import defaultdict

    d = defaultdict(int)

    for n in numbers:
        d[n] += 1

    return sorted(d, key=lambda key: d[key])[-1]

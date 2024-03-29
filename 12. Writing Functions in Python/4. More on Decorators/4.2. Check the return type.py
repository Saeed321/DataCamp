
#	Start by completing the returns_dict() decorator so that it raises an AssertionError if the return type of the decorated function is not a dictionary.

Hint

#	Make sure wrapper() is flexible enough to take any arguments that the function it is decorating might take.
#	wrapper() must call the function being decorated.
#	Don't forget to return the newly decorated function.

def returns_dict(func):
  # Complete the returns_dict() decorator
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    assert(type(result) == dict)
    return result
  return wrapper

@returns_dict
def foo(value):
  return value

try:
  print(foo([1,2,3]))
except AssertionError:
  print('foo() did not return a dict!')

#	Now complete the returns() decorator, which takes the expected return type as an argument.

Hint

#	You want to return a new decorator that looks a lot like the returns_dict() decorator you just wrote.
#	wrapper() should call the function being decorated.
#	Don't forget to return the decorated function.
#	Don't forget to return the decorator.

def returns(return_type):
  # Write a decorator that raises an AssertionError if the
  # decorated function returns a value that is not return_type
  def decorator(func):
    def wrapper(*args, **kwargs):
      result = func(*args, **kwargs)
      assert(type(result) == return_type)
      return result
    return wrapper
  return decorator
  
@returns(dict)
def foo(value):
  return value


try:
  print(foo([1,2,3]))
except AssertionError:
  print('foo() did not return a dict!')


#	Define a new decorator, named decorator(), to return.
#	Ensure the decorated function keeps its metadata.
#	Call the function being decorated and return the result.
#	Return the new decorator.

Hint

#	Remember: decorators like tag() that take arguments are actually decorator factories. tag() should create a new decorator and return it.
#	Use a decorator from the functools module to attach the metadata from func() to the wrapper() function.
#	wrapper() is the decorated function that decorator() returns. Its only job is to call the function being decorated.

def tag(*tags):
  # Define a new decorator, named "decorator", to return
  def decorator(func):
    # Ensure the decorated function keeps its metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
      # Call the function being decorated and return the result
      return func(*args, **kwargs)
    wrapper.tags = tags
    return wrapper
  # Return the new decorator
  return decorator

@tag('test', 'this is a tag')
def foo():
  pass

print(foo.tags)

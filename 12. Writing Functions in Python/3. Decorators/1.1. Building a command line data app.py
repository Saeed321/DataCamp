
#	Add the functions std(), minimum(), and maximum() to the function_map dictionary, like we did with mean().
#	The name of the function the user wants to call is stored in func_name. Use the dictionary of functions, function_map, to call the chosen function and pass data as an argument.

# Add the missing function references to the function map
function_map = {
  'mean': mean,
  'std': std,
  'minimum': minimum,
  'maximum': maximum
}

data = load_data()
print(data)

func_name = get_user_input()

# Call the chosen function and pass "data" as an argument
function_map['std'](data)

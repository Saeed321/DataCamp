
#	First of all, import Template from string module.

# Import Template
from string import Template

#	Complete the template using $tool and $description identifiers.
# Import Template
from string import Template

# Create a template
wikipedia = Template("$tool is a $description")

#	Substitute identifiers with the correct tool and description variables in the template and print out the results.

Hint

#	To substitute the identifier1 and identifier2 in the template string created, use string.substitute(). Don't forget to specify identifier1=name and identifier2=description inside each call.

# Import Template
from string import Template

# Create a template
wikipedia = Template("$tool is a $description")

# Substitute variables in template
print(wikipedia.substitute(tool=tool1, description=description1))
print(wikipedia.substitute(tool=tool2, description=description2))
print(wikipedia.substitute(tool=tool3, description=description3))

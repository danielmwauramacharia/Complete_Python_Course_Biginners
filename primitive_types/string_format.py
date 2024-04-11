from string import Template
# format () method
# @youtube by simplilearn

# use of Keyword argument
print("daniel {} learning {}".format('is', 'python'))

# use of index or positional argument
print("learn {0} programming with {1}".format('python', 'hamedani'))

# default indexing
print("{} called {} to inform that {} will be absent".format('John', 'Jane', 'Diana'))

# specified index
print("{2} called {1} to inform that {0} will be absent".format(
    'John', 'Jane', 'Diana'))

# use of Keyword Arguments
print("we {a}, {b} and {c} via  practice".format(
    a='learn', b='upskill', c='grow'))

# use of string template class
# Example 1
a1 = "python"
a2 = "programming"
n = Template("Hello, welcome to $n1 $n2")
print(n.substitute(n1=a1, n2=a2))

# Example 2
stu_name = "Daniel"
s = Template("Hey, $name!, How are you")
print(s.substitute(name=stu_name))

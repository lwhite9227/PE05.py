# Tasks from the exercise

# 1) make_shirt function
#    accepts a size and the text of a message, then prints a summary

def make_shirt(size, message):
    """Print a summary of the shirt size and the message printed on it."""
    print(f"Shirt size: {size}, message: '{message}'")

# Initial calls with positional and keyword arguments
make_shirt('L', 'Hello, world!')              # positional
make_shirt(size='M', message='Python is fun')  # keywords

# 2) modify make_shirt with defaults

def make_shirt(size='L', message='I love Python'):
    """Print a summary of the shirt size and the message.

    Defaults: size is large, message is 'I love Python'.
    """
    print(f"Shirt size: {size}, message: '{message}'")

# Using the default values
make_shirt()             # large shirt with default message
make_shirt(size='M')     # medium shirt with default message
make_shirt(size='S', message='Code all day')

# 3) describe_city function

def describe_city(city, country='Asia'):
    """Print a sentence stating the city and its country."""
    print(f"{city.title()} is in {country.title()}.")

# Three calls
describe_city('Tokyo')              # default country
describe_city('Toronto', country='Canada')
describe_city('Shreveport', country='united states')

# 4) show_messages function

def show_messages(messages):
    """Print each message from the list of short text messages."""
    for msg in messages:
        print(msg)

sample_msgs = [
    'Hello there!',
    'Stay curious.',
    'Keep learning.'
]

show_messages(sample_msgs)

# 5) function to count upper and lower case letters

def count_case(s):
    """Return the number of uppercase and lowercase letters in the string."""
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    print(f"No. of Upper case characters : {upper}")
    print(f"No. of Lower case Characters : {lower}")

# Sample execution
count_case('The quick Brow Fox')

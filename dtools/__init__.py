#!/usr/bin/env python
# coding: utf-8

# <div style="float:left">
#     <h1 style="width:450px">Practical 4: Object-Oriented Programming</h1>
#     <h2 style="width:450px">Getting to grips with Functions &amp; Packages</h2>
# </div>
# <div style="float:right"><img width="100" src="https://github.com/jreades/i2p/raw/master/img/casa_logo.jpg" /></div>

# <div style="border: dotted 1px rgb(156,121,26); padding: 10px; margin: 5px; background-color: rgb(255,236,184); color: rgb(156,121,26)"><i>Note</i>: You should download this notebook from GitHub and then save it to your own copy of the repository. I'd suggest adding it (<tt>git add ...</tt>) right away and then committing (<tt>git commit -m "Some message"</tt>). Do this again at the end of the class and you'll have a record of everything you did, then you can <tt>git push</tt> it to GitHub.</div>

# ## Revisiting Task 4. Why 'Obvious' is Not Always 'Right'
# 
# Task 4 in Practical 3 is hard, especially coming at the end of an already challenging practical. So I want to provide _another_ chance for the concepts to bed in before we use them as part of our exploratory work with the InsideAirbnb sample.
# 
# ##### A Dictionary of Lists to the Rescue
# 
# Remember, if we don't really care about column order (and why would we, on one level?), then a dictionary of lists would be a nice way to handle things. And why should we care about column order? With our CSV files above we already saw what a pain it was to fix things when the layout of the columns changed from one data set to the next. If, instead, we can just reference the 'Description' column in the data set then it doesn't matter where that column actually is. Why is that? 
# 
# Well, here are four rows of 'data' for city sizes organised by _row_:

# In[ ]:


myData = [
    ['id', 'Name', 'Rank', 'Longitude', 'Latitude', 'Population'], 
    ['1', 'Greater London', '1', '-18162.92767', '6711153.709', '9787426'], 
    ['2', 'Greater Manchester', '2', '-251761.802', '7073067.458', '2553379'], 
    ['3', 'West Midlands', '3', '-210635.2396', '6878950.083', '2440986']
]

# What cities are in the data set?
col = myData[0].index('Name')
cities = []
for i in range(1,len(myData)):
    cities.append(myData[i][col])
print(", ".join(cities))


# Compare that code to how it works as a dictionary of lists organised by _column_:

# In[ ]:


myData = {
    'id'         : [0, 1, 2, 3, 4, 5],
    'Name'       : ['Greater London', 'Greater Manchester', 'Birmingham','Edinburgh','Inverness','Lerwick'],
    'Rank'       : [1, 2, 3, 4, 5, 6],
    'Longitude'  : [-0.128, -2.245, -1.903, -3.189, -4.223, -1.145],
    'Latitude'   : [51.507, 53.479, 52.480, 55.953, 57.478, 60.155],
    'Population' : [9787426, 2705000, 1141816, 901455, 70000, 6958],
}

# What cities are in the data set?
print(", ".join(myData['Name']))


# See how even basic questions like "Is Edinburgh in our list of data?" are suddenly easy to answer? We no longer need to loop over the entire data set in order to find one data point. In addition, we know that everything in the 'Name' column will be a string, and that everything in the 'Longitude' column is a float, while the 'Population' column contains integers. So that's made life easier already. But let's test this out and see how it works.

# Now let's look at what you can do with this... but first we need to import one _more_ package that you're going to see a _lot_ over the rest of term: `numpy` (Numerical Python), which is used _so_ much that most people simply refer to it as `np`. This is a _huge_ package in terms of features, but right now we're interested only in the basic arithmatic functions: `mean`, `max`, and `min`.

# There's a _lot_ of content to process in the code below, so do _not_ rush blindly on if it is confusing. 
# 
# <div style="border: dotted 1px rgb(156,121,26); padding: 10px; margin: 5px; background-color: rgb(255,236,184)"><i>Stop!</i>: Look closely at what is going on. Try pulling it apart into pieces and then reassembling it. Start with the bits that you understand and then <i>add</i> complexity.</div>
# 
# We'll go through each one in turn, but they nearly all work in the same way and the really key thing is that you'll notice that we no longer have any loops (which are slow) just `index` or `np.<function>` (which is _very_ fast). 

# #### The Population of Manchester
# 
# The code can look pretty daunting, so let's break it down into parts:

# In[ ]:


pop = myData['Population'][ myData['Name'].index('Manchester') ]
print(f"Manchester's population is {pop}") # Notice how 'f-strings' work!


# Remember that this is a dictionary-of-lists (DoL). So:
# ```python
# myData['Population']    # Returns a list of population values
# myData['Population'][0] # Returns the first element of that list
# ```
# Does **that part** make sense?
# 
# ---
# 
# Now, to the second part, we know that Manchester is at index position 1 in the list, but we don't want to hard-code this for every city, so we need to replace `0` with code that will look up the index of a city, and we can only get that my looking in `myData['Name']`:
# ```python
# myData['Name'].index('Manchester')
# ```
# 
# Here we look in the dictionary for the key `Name` and find that that's _also_ a list (`['London','Manchester',...]`). All we're doing here is ask Python to find the index of 'Manchester' for us in that list. 
# 
# And `myData['Name'].index('Manchester')` gives us back a `1`, so _instead_ of just writing in a `1` into `myData['Population'][1]` we can replace `1` with `myData['Name'].index('Manchester')`! Notice the complete _absence_ of a for loop?

# #### The Easternmost City
# 
# Because we are dealing with numeric values now we can also do useful things much more quickly like finding the first part of, say, a _bounding box_ (the East value).

# In[ ]:


city = myData['Name'][ myData['Longitude'].index( max(myData['Longitude']) ) ]
print(f"The easternmost city is: {city}")


# Again, we need to break this down into parts in order to understand it:
# 1. We need to find the maximum _value_ of the longitude in the data set.
# 2. We need to find the _index_ of this value.
# 3. We use that index value to look up the name of the city.
# 
# So, the pieces in code... 
# ```python
# myData['Longitude']      # The longitude data values
# myData['Longitude'][0]   # The first element of the list
# max(myData['Longitude']) # The maximum value in the list
# myData['Longitude'].index(...) # Search for a value in the list
# ```
# Does **that part** make sense?
# 
# ---
# We can then think our way through this as we might with a maths equation and substitution:
# ```python
# myData['Longitude'].index( max(myData['Longitude']) ) # The index of the maximum value of the list
# myData['Name'][0] # The first element in the city list
# 
# # You can use whitespace to make this more legible
# myData['Name'][
#     myData['Longitude'].index( 
#         max(myData['Longitude']) 
#     )
# ]
# 
# # Or, once you're more comfortable with code:
# city = myData['Name'][ myData['Longitude'].index( max(myData['Longitude']) ) ]
# ```
# Does **that part** make sense?
# 
# ---
# 
# So to explain this in three steps, what we're doing is:
# * Finding the maximum value in the Longitude column (we know there must be one, but we don't know what it is!),
# * Finding the index (position) of that maximum value in the Longitude column (now that we know what the value is!),
# * Using that index to read a value out of the Name column.
# 
# I _am_ a geek, but that's pretty cool, right? In one line of code we managed to quickly find out where the data we needed was even though it involved three discrete steps. Think about how much work you'd have to do if you were still thinking in _rows_, not _columns_!

# #### The Location of Lerwick
# 
# This is 'just' variations on a theme since we're still using the same concepts of `index` and lists, what makes it hard is that there looks to be a _lot_ of code on one line:

# In[ ]:


city = "Lerwick"
print(f"The town of {city} can be found at " + 
      f"{abs(myData['Longitude'][myData['Name'].index(city)])}ºW, {myData['Latitude'][myData['Name'].index(city)]}ºN")


# But always remember that you can rewrite this using whitespace and concatentation to make it easier for a human to read:

# In[ ]:


city = "Lerwick"
print(f"The town of {city} can be found at " + 
      f"{abs(myData['Longitude'][myData['Name'].index(city)])}ºW, " +
      f"{myData['Latitude'][myData['Name'].index(city)]}ºN")


# Or, you could even work it out this way first and _then_ combine the code as above:

# In[ ]:


city = "Lerwick"
lat  = abs(
    myData['Longitude'][
        myData['Name'].index(city)
    ]
)
lon  = myData['Latitude'][
    myData['Name'].index(city)
]

print(f"The town of {city} can be found at " + 
      f"{lat}ºW, " +
      f"{lon}ºN")


# Notice that have a `+` at the *end of the line* tells Python that it should carry on reading to the next line as part of the same command. That's a handy way to make your code a little easier to read! Same goes withg formatting a list: if it's getting a little long then you can *also* continue a line using a `,`!
# 
# ##### Recap of f-Strings
# 
# In case you're rusty on how f-strings (`f"<some text here>"`) work, the first one will help you to make sense of the second: f-strings allow you to 'interpolate' code directly into a string rather than having to have lots of `str(x) + " some text " + str(y)`. You can write `f"{x} some text {y}"` and Python will automatically replace `{x}` with the _value of `x`_ and `{y}` with the _value of `y`_. 
# 
# So `f"The town of {city} can be found at "` becomes `f"The town of Lerwick can be found at "` because `{city}` is replaced by the value of the variable `city`. This makes for code that is easier for humans to read and so I'd consider that a good thing.
# 
# ##### Breaking it Down (Again)
# 
# The second f-string _looks_ hard because there's a _lot_ of code there. But, again, if we start with what we recognise that it gets just a little bit more manageable... Also, it stands to reason that the only difference between the two outputs is that one asks for the 'Longitude' and the other for the 'Latitude'. So if you can make sense of one you have _automatically_ made sense of the other and don't need to work it all out.
# 
# Let's start with a part that you might recognise:
# ```python
# myData['Name'].index(city)
# ```
# Does **that part** make sense?
# 
# ---
# 
# You've _got_ this. This is just asking Python to work out the index of Lerwick (because `city = 'Lerwick'`). So it's a number. 5 in this case. And we can then think, 'OK so what does this return:
# ```python 
# myData['Longitude'][5]
# ```
# And the answer is `-1.145`. That's the Longitude of Lerwick! There's just _one_ last thing: notice that we're talking about degrees West here. So the answer isn't a negative (because negative West degrees would be _East_!), it's the _absolute_ value. And that is the final piece of the puzzle: `abs(...)` gives us the absolute value of a number!
# 
# Does **that part** make sense?
# 
# ---
# 
# You could have [found `abs` yourself using Google](https://lmgtfy.app/?q=absolute+value+python).

# #### The Average City Size
# 
# Here we're going to 'cheat' a little bit: rather than writing our own function, we're going to import a package and use someone _else's_ function. The `numpy` package contains a _lot_ of useful functions that we can call on (if you don't believe me, add "`dir(np)`" on a new line after the `import` statement), and one of them calculates the average of a list or array of data.

# In[ ]:


import numpy as np

mean = np.mean(myData['Population'])
print(f"The mean population is: {mean}")


# You _could_ also write this like:
# ```python
# print(f"The mean population is: {np.mean(myData['Population']}")
# ```
# There's no 'right' way here to write your code: putting it all on one line and not saving it to a temporary variable called 'mean' is slightly faster, but if you were going to use the mean to do other things (e.g. standardise the data) then it is a bit more clear what you're doing.

# #### Standardising City Sizes
# 
# To give you a sense of how scaleable this approach to data is, check out this neat little trick for working out z-scores for cities sizes:

# In[ ]:


# Use numpy functions to calculate mean and standard deviation
mean = np.mean(myData['Population'])
std  = np.std(myData['Population'])
print(f"City distribution has sample mean {mean} and sample standard deviation of {std:7.2f}.")


# `numpy` gives us a way to calculate the mean and standard deviation _quickly_ and without having to reinvent the wheel. The other potentially new thing here is `{std:7.2f}`. This is about [string formatting](https://www.w3schools.com/python/ref_string_format.asp) and the main thing to recognise is that this means 'format this float with 7 digits to the left of the left of the decmial and 2 digits to the right'. The link I've provided uses the slightly older approach of `<str>.format()` but the formatting approach is the same.
# 
# Does **that part** make sense?
# 
# ---
# 
# Now we're going to see how the code `[x for x in list]` gives us a way to apply an operation (converting to string, subtracting a value, etc.) to every item in a list without writing out a full for loop. This basically gives us a one-line way to avoid writing:
# ```python
# rs = []
# for x in myData['Population']:
#     rs.append((x-mean)/std)
# ```
# So here code in the `for` loop is applied and the result automatically added to the output list.

# In[ ]:


rs = [(x - mean)/std for x in myData['Population']]
myData['Std. Population'] = rs
print(myData['Std. Population'])


# In[ ]:


print("City name: " + ", ".join( myData['Name'] ))
print("Raw population: " + ", ".join( [str(x) for x in myData['Population']] ))
print("Standardised population: " + ", ".join( [f"{x:4.3f}" for x in myData['Std. Population']] ))


# This is where our new approach really comes into its own: because all of the population data is in one place (a.k.a. a _series_ or column), we can just throw the whole list into the `np.mean` function rather than having to use all of those convoluted loops and counters. Simples, right? 
# 
# No, not _simple_ at all conceptually, but we've come up with a way to _make_ it simple _as code_.

# #### Brain Teaser
# 
# Why not have a stab at writing the code to print out the _4th most populous_ city? This can _still_ be done on one line, though you might want to start by breaking the problem down:
# 1. How do I find the _4th_ largest value in a list?
# 2. How do I find the _index_ of the 4th largest value in a list?
# 3. How do I use that to look up the name associated with that index?
# 
# You've already done \#2 and \#3 above so you've _solved_ that problem. If you can solve \#1 then the rest should fall into place.
# 
# <div style="border: dotted 1px green; padding: 10px; margin: 5px; background-color: rgb(249,255,249);"><i>Hint</i>: you don't want to use <tt>&lt;list&gt;.sort()</tt> because that will sort your data <i>in place</i> and break the link between the indexes across the 'columns'; you want to research the function <tt>sorted(&lt;list&gt;)</tt> where <tt>&lt;list&gt;</tt> is the variable that holds your data and `sorted(...)` just returns whatever you pass it in a sorted order <i>without</i> changing the original list. You'll see why this matters if you get the answer... otherwise, wait a few days for the answers to post.</div>

# In[ ]:


sorted(myData['Population'], reverse=True)


# In[ ]:


# Print out the name of the 4th most populous city-region

# Find the fourth largest value
fourth = sorted(myData['Population'], reverse=True)[3]
print(fourth)

# Find the index of the fourth largest value
idx = myData['Population'].index(fourth)
print(idx)

# Find the city associated with that value
city = myData['Name'][idx]

# And output
print("The fourth most populous city is: " + str(city))


# The answer is Edinburgh.

# #### Recap!
# 
# So the _really_ clever bit in all of this isn't switching from a list-of-lists to a dictionary-of-lists, it's recognising that the dictionary-of-lists is a _better_ way to work _with_ the data that we're trying to analyse and that that there are useful functions that we can exploit to do the heavy lifting for us. Simply by changing the way that we stored the data in a 'data structure' (i.e. complex arrangement of lists, dictionaries, and variables) we were able to do away with lots of for loops and counters and conditions, and reduce many difficult operations to something that could be done on one line! 

# ## Task 1. Creating a Set of Functions

# Let's start trying to put this all together by creating a a set of functions that will help us to:
# 
# 1. Download a file from a URL (checking if it has already _been_ downloaded to save bandwidth).
# 2. Parse it as a CSV file and...
# 3. Convert it to a Dictionary-of-Lists
# 4.Perform some simple calculations using the resulting data.
# 
# To be honest, there's not going to be much about writing our _own_ objects here, but we will be making use of them and, conceptually, an understanding of objects and classes is going to be super-useful for understanding what we're doing in the remainder of the term!

# #### Task 1.1: Start from Existing Code
# 
# First, let's be sensibly lazy--we've already written code to read a file ([2020-08-24-sample-listings.csv](https://github.com/jreades/i2p/raw/master/data/2020-08-24-sample-listings.csv)) from the Internet and turn it into a list of lists. So I've copy+pasted that into the code block below since we're going to start from this point; however, just to help you check your own understanding, I've removed a few bits and replacement with `??`. Sorry. 😈

# In[ ]:


from urllib.request import urlopen
import csv

url = "https://github.com/jreades/i2p/raw/master/data/2020-08-24-sample-listings.csv"

urlData = [] # Somewhere to store the data

response = urlopen(url) # Get the data using the urlopen function
csvfile  = csv.reader(response.read().decode('utf-8').splitlines()) # Pass it over to the reader

for row in csvfile:
    urlData.append(row)

print("urlData has " + str(len(urlData)) + " rows and " + str(len(urlData[0])) + " columns.")
print(urlData[-1][:2]) # Check it worked!


# You should get `urlData has 101 rows and 26 columns.` and a row that looks like this: `['40373464', 'Modern, Small Double Private Room']`.

# #### Task 1.2: Getting Organised
# 
# Let's take the code above and modify it so that it is:
# 
# 1. A function that takes two arguments: a URL; and a destination filename.
# 2. Implemented as a function that checks if a file exists already before downloading it again.
# 
# You will find that the `os` module helps here because of the `path` function. And you will [need to Google](https://lmgtfy.app/?q=check+if+file+exists+python) how to test if a file exists. I would normally select a StackOverflow link in the results list over anything else because there will normally be an _explanation_ included of why a particular answer is a 'good one'. I also look at which answers got the most votes (not always the same as the one that was the 'accepted answer'). In this particular case, I also found [this answer](https://careerkarma.com/blog/python-check-if-file-exists/) useful.
# 
# --- 
# 
# I would start by setting my inputs:

# In[ ]:


import os
url = "https://github.com/jreades/i2p/raw/master/data/2020-08-24-sample-listings.csv"
out = os.path.join('data','2020-08-24-sample-listings.csv')


# #### Task 1.3: Sketching Out a Function
# 
# Then I would sketch out how my function will work using comments. And the simplest thing to start with is checking whether the file has already been downloaded:

# In[ ]:


from urllib.request import urlopen

def get_url(src, dest):
    
    # Check if dest does *not* exist -- that
    # would mean we had to download it!
    if not os.path.isfile(dest):
        print(f"{dest} not found!")
    else:
        print(f"Found {dest}!")
        
get_url(url, out)


# #### Task 1.4: Fleshing Out a Function 
# 
# I would then flesh out the code that checks if the data has been downloaded and ensure that both my if and else 'branches' return a list that I could then read using the CSV library:

# In[ ]:


def get_url(src, dest):
    
    # Check if dest does *not* exist -- that
    # would mean we had to download it!
    if not os.path.isfile(dest):
        print(f"{dest} not found, downloading!")
        
        # Get the data using the urlopen function
        response = urlopen(src) 
        filedata = response.read().decode('utf-8')
        
        # Extract the part of the dest(ination) that is *not*
        # the actual filename--have a look at how 
        # os.path.split works using `help(os.path.split)`
        path = list(os.path.split(dest)[:-1])
        
        # Create any missing directories in dest(ination) path
        # -- os.path.join is the reverse of split (as you saw above)
        # but it doesn't work with lists... so I had to google how 
        # to use the 'splat' operator! os.makedirs creates missing 
        # directories in a path automatically.
        if len(path) >= 1 and path[0] != '':
            os.makedirs(os.path.join(*path), exist_ok=True)
        
        with open(dest, 'w') as f:
            f.write(filedata)
            
    else:
        print(f"Found {dest} locally!")
    
    with open(dest, 'r') as f:
        return f.read().splitlines()
        
# Using the `return contents` line we make it easy to 
# see what our function is up to.
c = get_url(url, out)


# <div style="border: dotted 1px rgb(156,121,26); padding: 10px; margin: 5px; background-color: rgb(255,236,184)"><i>Stop!</i> Notice that we don't try to check if the data file contains any useful data! So if you download or create an empty file while testing, you won't necessarily get an error until you try to turn it into data afterwards!</div>

# #### Task 1.5: Read a CSV file into a LoL

# Now we've taken care of whether or not the file has already been downloaded, we can focus on the next part of the problem! This will also use code from Task 2.1 in the Live Session.

# In[ ]:


import csv

# Notice that it doesn't make sense to use `dest` as the 
# parameter name here because we always read *from* a data
# source. Your names can be whatever you want, but they 
# should be logical wherever possible!
def to_lol(lst):
    
    # Rest of code to read file and convert it goes here
    csvdata = []
    
    # This is the same code that you used last week, but 
    # you'll have to rename some vars to get things to
    # work for you here.
    csvfile  = csv.reader(lst)
    for row in csvfile:              
        csvdata.append( row )
    
    # Return list of lists
    return csvdata
        
# Save the CSV-LoL to a new variable
clol = to_lol(c)


# In[ ]:


print(f"LoL has {len(clol)} rows and {len(clol[0])} columns.")
print(clol[0][:2])
print(clol[-1][:2])


# You should get: 
# ```
# LoL has 101 rows and 26 columns.
# ['id', 'name']
# ['40373464', 'Modern, Small Double Private Room']
# ```

# #### Task 1.6: Convert a LoL to a DoL
# 
# We're going to assume that the first row of our LoL is always a _header_ (i.e. list of column names). If it's not then this code is going to have problems. A _robust_ function would allow us to specify column names when we create the data structure, but let's not get caught up in that level of detail just yet.
# 
# Have a look at Task 2.3 from the Live Coding session to see how to fill this in... Notice that I've also, for the first time used the docstring support offered by Python. Once this function is working you'll be able to use `help(to_dol)` and get back the docstring help!

# In[ ]:


def to_dol(lol):
    """
    Converts a list-of-lists (LoL) to a dict-of-lists (dol)
    using the first element in the LoL to create column names.
    
    :param lol: a list-of-lists where each element of the list represents a row of data
    :returns: a dict-of-lists
    """
    # Create empty dict-of-lists
    ds = {}

    # I had a version of this code that used
    # lol.pop(0) since it made the for loop
    # easier to read. But I changed my mind...
    #
    # Can you think why?
    col_names = lol[0]
    for c in col_names:
        ds[c] = []

    # Then values into a list attached to each key
    for row in lol[1:]:
        for c in range(0,len(col_names)):
            ds[ col_names[c] ].append( row[c] )
            
    return ds

ds = to_dol(clol)


# In[ ]:


print(", ".join(ds.keys()))
print(ds['id'][:2])
print(ds['name'][:2])
print(ds['room_type'][:2])


# The answer should look like:
# ```
# id, name, description, host_id, host_name, host_since, latitude, longitude, property_type, room_type, accommodates, bathrooms, bedrooms, beds, price, minimum_nights, maximum_nights, availability_30, availability_60, availability_90, availability_365, number_of_reviews, first_review, last_review, review_scores_rating, calculated_host_listings_count
# ['25339003', '40259218']
# ['An Amazing 4Bedroom Home, Central London, Sleeps12', 'Large Double Room - Maida Vale']
# ['Entire home/apt', 'Private room']
# ```

# #### Task 1.7: Convert Data Types on DoL
# 
# You can just take the code we saw in the Live Coding session (Task 4.1), but you'll need to investigate the columns yourself in order to see what the appropraite values should be. I would suggest taking the _full_ version of the function where we check what `cdata` is so that we have one function that works for both strings and lists.
# 
# Just to help get you started, here are the column names and you can create a `dtype` list to hold the _data type_ for each column. I'm also going to introduce you the `zip` function here as it has many uses with geographic data (especially converting lat/long to points).

# In[ ]:


cols  = ['id', 'name', 'description', 'host_id', 'host_name', 
        'host_since', 'latitude', 'longitude', 'property_type', 
        'room_type', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 
        'price', 'minimum_nights', 'maximum_nights', 'availability_30', 
        'availability_60', 'availability_90', 'availability_365', 'number_of_reviews', 
        'first_review', 'last_review', 'review_scores_rating', 'calculated_host_listings_count']
dtype = [int, str, str, int, str, 
         str, float, float, str, 
         str, int, bool, float, float, 
         str, int, int, int, int, 
         int, int, int, int,
         str, str, float, int]

# 'Zips up' these two lists into an iterator list of tuples!
# Note than you cannot save the output of zip directly because
# you can only iterate through it once.
for d in zip(cols, dtype):
    # Notice the more advanced formatting here:
    # - `>20` means right-align with up to 20 characters of whitespace; notice the last line!
    # - `d[1].__name__` gives us the name of the data type, rather than a '<class...>' output.
    print(f"Column ({d[0]:>20}) is type: \t{d[1].__name__}")


# In[ ]:


# Convert the raw data to data of the appropriate
# type: 'column data' (cdata) -> 'column type' (ctype)
def to_type(cdata, ctype):
    # If a string
    if isinstance(cdata, str):
        try:
            if ctype==bool:
                return cdata==True
            else:
                return ctype(cdata)
        except TypeError:
            return cdata
    
    # Not a string (assume list)
    else: 
        fdata = []
        for c in cdata:
            try:
                if ctype==bool:
                    fdata.append( c=='True' )
                else:
                    fdata.append( ctype(c) )
            except:
                fdata.append( c )
        return fdata


# In[ ]:


# Now apply this! We'll copy the data to 
# new data structure only so that we know
# we're not overwriting `ds` until we're sure
# that the code works.
ds2 = {}
for d in zip(cols, dtype):
    ds2[ d[0] ] = to_type(ds[d[0]], d[1])


# In[ ]:


print(ds2['id'][:3])
print(ds2['host_name'][:3])
print(ds2['beds'][:3])
print(ds2['availability_365'][:3])
print(ds2['last_review'][:3])


# You should get the followg:
# ```
# [25339003, 40259218, 20097666]
# ['Emily', 'Mantas', 'Thanyawan']
# [9.0, 1.0, 1.0]
# [23, 365, 0]
# ['2020-03-01', '2020-02-08', '']
# ```

# #### Task 1.8: Checking Basic Functionality
# 
# Let's see if our new data structure broadly works by testing out some of our previous operations:

# In[ ]:


import numpy as np # We'll need this


# In[ ]:


print(f"Average availability over 365 days is {np.mean(ds2['availability_365'])}")
print(f"Standard deviation on minimum nights is {np.std(ds2['minimum_nights'])}")
print(f"Median maximum nights is {np.median(ds2['maximum_nights'])}")


# But...

# In[ ]:


print(f"Median price per night is {np.median(ds2['price'])}")


# Why is this happening? Write some code below to check:

# In[ ]:


ds2['price'][:3]


# #### Task 1.9: Putting It All Together
# 
# Here's a clue for how to solve the 'price' data problem; you will need to combine it with something we've seen earlier that allows you to iterate over a list and apply the solution to every `x` in the 'price' column. If you are nearing the end of the 2-hour practical, then may skip this task for now and work on converting the functions to a package (next task below).

# In[ ]:


#float(ds2['price'][0].replace('$',''))
ds2['price'] = to_type([ x.replace('$','') for x in ds2['price']],float)


# In[ ]:


print(f"Median price per night is ${np.median(ds2['price']):0.2f}")


# ## Task 2. Creating a Package from Functions
# 
# Using or adapting as necessary the approach that we saw in the Live Coding session (Task 2 from Part 1) create a package called `dtools` by exporting the functions you've created above (only the final version of each, so don't export the one form Task 1.3 for instance) into a file called `__init__.py` that sits in the `dtools` directory.

# In[ ]:


get_ipython().system("mkdir -p 'dtools'")


# In[ ]:


# Commented out so don't automatically re-run this code every time
#!jupyter nbconvert --ClearOutputPreprocessor.enabled=True \
#    --to python --output=dtools/__init__.py \
#    Practical-04-Objects.ipynb


# Once you have tidied up the content of `dtools/__init__.py` you should be able to run the code below. You can actually edit the `init` file directly in Jupyter as a text file. You can compare this to the file I've created on GitHub.

# In[ ]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# In[ ]:


import dtools
help(to_dol)


# In[ ]:


url = 'https://github.com/jreades/i2p/raw/master/data/src/2019-sample-Crime.csv'
out = os.path.join('data','crime-sample.csv')

dlol = dtools.get_url(url, out)
dlol = dtools.to_lol(dlol)
ddol = dtools.to_dol(dlol)

print(len(ddol.keys()))
print(len(ddol['ID']))


# In[ ]:


print(ddol.keys())


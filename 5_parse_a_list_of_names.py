# In this bite you will work with a list of names.
#
# First you will write a function to take out duplicates and title case them.
#
# Then you will sort the list in alphabetical descending order by surname and lastly
# determine what the shortest first name is. For this exercise you can assume there is
# always one name and one surname.
#
# With some handy Python builtins you can write this in a pretty concise way. Get it
# sorted :)

NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
    each name appears only once"""
    names_set = [name.title() for name in set(names)]
    return names_set


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names_surname_sort = sorted(names, key=lambda name: name.split()[1], reverse=True)
    return names_surname_sort


def shortest_first_name(names):
    """Returns the shortest first name (str).
    You can assume there is only one shortest name.
    """
    names_firstname_sort = sorted(names, key=lambda name: len(name.split()[0]))
    return names_firstname_sort[0].split()[0]


title_cased_set = dedup_and_title_case_names(NAMES)
surname_sort = sort_by_surname_desc(title_cased_set)
first_length_sort = shortest_first_name(title_cased_set)

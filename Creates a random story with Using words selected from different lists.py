import random
nouns = [ "sun" , "water" , "fish" , "cat" , "grass" ]
adjectives = [ "pretty" , "ugly" , "red" , "smelly" , "fun" ]
verbs = [ "reads" , "eats" , "smells" , "drinks" , "grabs" ]
print ( "\n  SENTENCE ==> The" ,random.choice(adjectives),random.choice(nouns),
       random.choice(verbs), ", the" ,
       random.choice(adjectives),random.choice(nouns),"\n")
#############################################################

#some OUTPUT  from this program ==>
# The smelly grass smells the fun water
# The red cat grabs the fun sun

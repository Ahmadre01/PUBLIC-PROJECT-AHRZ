import random
nouns = [ "sun" , "water" , "fish" , "cat" , "grass" ]
adjectives = [ "pretty" , "ugly" , "red" , "smelly" , "fun" ]
verbs = [ "reads" , "eats" , "smells" , "drinks" , "grabs" ]
print ( "\n  SENTENCE ==> The" ,random.choice(adjectives),random.choice(nouns),
       random.choice(verbs), ", the" ,
       random.choice(adjectives),random.choice(nouns),"\n")
# یک داستان تصادفی ایجاد می‌کند با استفاده از کلمات انتخابی از لیست‌های مختلف
# ابتدا سه لیست از کلمات تعریف شده‌اند: 
# اسم‌ها (nouns)، صفت‌ها (adjectives) و فعل‌ها (verbs). 
# random.choice()با استفاده از تابع 
# در پایتون استفاده میکندrandom که از کتابخانه 
# یک عنصر تصادفی از هر یک از این لیست‌ها انتخاب شده و در داستان نهایی استفاده می‌شود
#############################################################

#some OUTPUT  from this program ==>
# The smelly grass smells the fun water
# The red cat grabs the fun sun

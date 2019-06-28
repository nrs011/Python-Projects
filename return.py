def allowed_dated_age(my_age):
    girls_age = my_age / 2 + 7
    return girls_age

nimeshs_limit = allowed_dated_age(21)
joes_limit = allowed_dated_age(49)
print("Nimesh can date girls", nimeshs_limit, "or older.")
print("Joe can date girls", joes_limit, "or older.")
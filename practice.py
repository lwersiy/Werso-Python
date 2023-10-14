user_dict = {
    "louis": {"has_license": True, "valid": True, "age": 31, "person_is_insured": True},
    "Giddy": {"has_license": True, "valid": True, "age": 16, "person_is_insured": True}
}

# User to consider
user = "louis"

# Get age and license information for the user
age = user_dict.get(user, {}).get("age", None)
has_license = user_dict.get(user, {}).get("has_license", False)
is_valid = user_dict.get(user, {}).get("valid", False)
is_insured = user_dict.get(user, {}).get("person_is_insured", False)

# Determine which type of car to give based on age and license information
if age is not None:
    if 18 <= age <= 70:
        print("Give car")
        if 25 <= age <= 35:
            print("Give sport car")
        if age > 30:
            print("Give SUV")
    else:
        print("Do not give car")
else:
    print("Age information not available for user '{}'.".format(user))

# Check if a sport car should be given based on age
if age is not None and 25 <= age <= 35:
    print("Give sport car")
else:
    print("Do not give sport car")

# Check if a car should be given based on license information
if has_license and is_valid and is_insured:
    print("Give car")
else:
    print("Do not give car")


################################################################################


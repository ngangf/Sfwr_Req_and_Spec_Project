from Project.userlogin import UserLogin

# verify username and password against the database
def test_user_login():
    database_usernames = [
        "Tom"
        "Peter"
        "John"
        "Paul"
    ]

    database_passwords = [
        "Tommy2020"
        "Pete01"
        "Joe77"
        "P1202"
    ]

    userlogin = UserLogin()

    for username in database_usernames:
        assert userlogin.verify_login(username) == True, "Please verify the username"

    for password in database_passwords:
        assert userlogin.verify_login(password) == True, "Please verify the password"
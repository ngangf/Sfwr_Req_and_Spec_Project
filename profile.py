class Profile:
    def __init__(self):
        self.profile = []

    def __len__(self):
        return len(self.profile)

    def add_email(self, email):
        if email.valid:
            self.profile.append(email)
        else:
            return "this email address is invalid!"
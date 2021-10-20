from django.contrib.auth.models import User


def normalize(name: str) -> str:
    return name.lower().translate({ord(c): None for c in "-_ "})


class CustomUser:
    @property
    def display_name(self: User) -> str:
        full_name = self.get_full_name()
        if full_name and normalize(full_name) != normalize(self.username):
            return f"{self.username} ({full_name})"
        return self.username

    @property
    def profile_name(self: User) -> str:
        return self.get_full_name() or self.username

    @property
    def short_name(self: User) -> str:
        return self.first_name or self.username

    @property
    def is_trackable(self: User) -> bool:
        return (
            self.is_authenticated
            and "@example.com" not in self.email
            and "admin" not in self.username
        )


for _name in dir(CustomUser):
    if not _name.startswith("_"):
        method = getattr(CustomUser, _name)
        User.add_to_class(_name, method)

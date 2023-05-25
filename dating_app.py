class Profile:
    profile_count = 0

    def __init__(self, gender, age, looking_for):
        self.id = Profile.profile_count + 1
        Profile.profile_count += 1
        self.gender = gender
        self.age = age
        self.looking_for = looking_for

    def __str__(self):
        return f"{self.age} year old {self.gender}, looking for a {self.looking_for}. (id: {self.id})"


class FreeProfile(Profile):
    like_limit = 1

    def __init__(self, gender, age, looking_for):
        super().__init__(gender, age, looking_for)
        self.likes_given = 0

    def likes(self, profile):
        if profile.id == self.id:
            print("You can't like your own profile.")
        elif self.likes_given >= FreeProfile.like_limit:
            print("You can't like more, you've reached your like limit.")
        elif profile.id in self.likes_given:
            print("You already liked this profile.")
        else:
            self.likes_given += 1
            profile.likes_received.append(self)
            if self in profile.likes_received:
                print("It's a match!")


class ProProfile(Profile):
    like_limit = 1000

    def __init__(self, name, gender, age, looking_for):
        super().__init__(gender, age, looking_for)
        self.name = name
        self.likes_given = []

    def likes(self, profile):
        if profile.id == self.id:
            print("You can't like your own profile.")
        elif profile.id in self.likes_given:
            print("You already liked this profile.")
        elif len(self.likes_given) >= ProProfile.like_limit:
            print("You can't like more, you've reached your like limit.")
        else:
            self.likes_given.append(profile)
            profile.likes_received.append(self)
            if self in profile.likes_received:
                print("It's a match!")

    def send_message(self, profile, message):
        if isinstance(profile, FreeProfile):
            print("Unable to send message, upgrade your profile to Pro.")
        else:
            print(f"Message is sent to profile #{profile.id}.")
            

class DatingApp:
    def __init__(self, name):
        self.name = name
        self.profiles = []

    def register(self, *profiles):
        for profile in profiles:
            self.profiles.append(profile)

    def new_day(self):
        for profile in self.profiles:
            if isinstance(profile, FreeProfile):
                profile.likes_given = []

    def recommend_profiles(self, target):
        recommendations = []
        for profile in self.profiles:
            if (
                profile.id != target.id and
                profile.id not in [like.id for like in target.likes_given] and
                profile.gender == target.looking_for and
                target.gender == profile.looking_for
            ):
                recommendations.append(profile.id)
        return recommendations

    def advanced_recommend_profiles(self, target):
        recommendations = self.recommend_profiles(target)
        liked_profiles = [like.id for like in target.likes_received]
        return sorted(recommendations, key=lambda profile_id: profile_id in liked_profiles, reverse=True)

    def who_liked_profile(self, profile):
        return [like.id for like in profile.likes_received]


ibsnder = DatingApp('IBSnder')
john = ProProfile('John', 'male', 30, 'female')  # should have profile id 1
jane = FreeProfile('female', 28, 'male')  # should have profile id 2
kate = ProProfile('Kate', 'female', 34, 'female')  # should have profile id 3
jack = FreeProfile('male', 23, 'male')  # should have profile id 4
jill = ProProfile('Jill', 'female', 28, 'male')  # should have profile id 5
bob = ProProfile('Bob', 'male', 42, 'female')  # should have profile id 6
david = FreeProfile('male', 37, 'female')  # should have profile id 7
ibsnder.register(john, jane, kate, jack, jill, bob, david)
print(john)  # should print: John is a 30 year old male, looking for a female. (id: 1)
print(jane)  # should print: 28 year old female, looking for a male. (id: 2)
john.likes(jane)
jane.likes(john)  # should print: It's a match!
jane.likes(bob)  # should print: You can't like more, you've reached your like limit.
john.likes(john)  # should print: You can't like your own profile.
john.likes(kate)
jill.likes(john)
david.likes(jill)
print(ibsnder.recommend_profiles(jill))  # since Jill already liked John, it should print only: [6, 7]
print(ibsnder.advanced_recommend_profiles(jill))  # since David liked Jill, it should print only: [7, 6]
print(ibsnder.who_liked_profile(john))  # should print [2, 5]
ibsnder.new_day()
jane.likes(john)  # should print: You already liked this profile.
jane.likes(bob)  # no error, because Jane again has a free like
john.send_message(jane, 'hello')  # should print: Message is sent to profile #2.
jane.send_message(john, 'hi')  # Unable to send message, upgrade your profile to Pro.

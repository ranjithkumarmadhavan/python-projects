import instaloader

ig = instaloader.Instaloader()

user = input("Enter the Instagram username: ")

ig.download_profile(user, profile_pic_only=True)

import instaloader
ig = instaloader.Instaloader()

username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
ig.login(username, password)

post_url = input("enter the instagram post url: ")
post = instaloader.Post.from_shortcode(ig.context, post_url.rsplit('/', 1)[-1])
ig.download_post(post, target="video")

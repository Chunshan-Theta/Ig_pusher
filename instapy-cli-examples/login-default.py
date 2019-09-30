from instapy_cli import client

username = 'just.test.pusher'
password = '00000000'

with client(username, password) as cli:
    # do stuffs with cli
    ig = cli.api()
    print(ig.current_user())

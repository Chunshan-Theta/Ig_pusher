from instapy_cli import client

username = 'just.test.pusher'
password = '00000000'
image = 'https://images.unsplash.com/photo-1460518451285-97b6aa326961?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjEyMDd9'
text = 'This will be the caption of your photo.' + '\r\n' + 'You can also use hashtags! #hash #tag #now'

with client(username, password) as cli:
    cli.upload(image, text)

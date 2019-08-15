from instapy_cli import client

username = 'just.test.pusher'
password = '00000000'
image = './test.png'
text = 'This will be the caption of your photo.' + '\r\n' + 'You can also use hashtags! #hash #tag #now'

with client(username, password) as cli:
    cli.upload(image, text)

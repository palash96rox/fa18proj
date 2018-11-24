import builder
import pprint

books_data = dict()
library = {
    'eng': ['pride.txt',],
    'hin': ['hindi.txt',]
}
for lang in library.keys():
    for book in library[lang]:
        books_data = builder.build(book,books_data,lang)
pprint.pprint(books_data)




users_data = dict()
users = {
    'user00': ['28-Nov.txt',],
    'user01': ['testing.txt',],
}
for user in users.keys():
    for script in users[user]:
        users_data = builder.build(script,books_data,user)
pprint.pprint(users_data)
from random import choice
from flask import Flask

import json

app=Flask(__name__)

class Developer():
    def __init__(self, name, last_n, language):
        self.first_name = name
        self.last_name = last_n
        self.programming_language = language


    def __str__(self):
        return '%s %s - %s' % (self.first_name, self.last_name, self.programming_language)

    def __call__(self):
        return str('%s %s - %s' % (self.first_name, self.last_name, self.programming_language))

p1=Developer('Jack', 'Denials', 'Python')
p2=Developer('Bond', '007', 'C++')
p3=Developer('Alex', 'S', 'Ryby')

developers = [p1,p2,p3]

@app.route('/')
def developer_controller():

    return str(list(map(lambda dev: str(dev), developers)))

@app.route('/remove_developer/')
def remove_developer():
    if len(developers)==0:
        return "There is no programmers"
    else:
        developers.remove(choice(developers))
        return str(list(map(lambda dev: str(dev), developers)))
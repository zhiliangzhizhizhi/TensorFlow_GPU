# import tensorflow as tf
# zero_tsr = tf.zeros([2,4])
from random import choice

class Person:
    def __init__(self, name):
        self.greeting = "<div>Hello {name}</div>"
        self.name = name

    def __abs__(self):
        return self.make_greeting()

    def make_greeting(self):
        return self.greeting.format(name=self.name)


def main():
    people = [Person('Jane'),
              Person('Jill'),
              Person('Bob')
              ]

    person = choice(people)
    print(person)

# if __name__ == '__main__':
#    main()

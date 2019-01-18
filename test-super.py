class Person:
    def __init__(self, name, surname, number,**kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        super().__init__(**kwargs)#have to add a super statement here,or a error message:Tutor has no
        #attribute classes will display.The reason is that super find the next class in the
        #Method resolution order.after we add this super here,it will go next to call the init
        # of LearnerMixin which is right behind Person in the MRO.


class LearnerMixin:
    def __init__(self,classes,**kwargs):
        self.classes = classes
        super().__init__(**kwargs)

    def enrol(self, course):
        self.classes.append(course)


class TeacherMixin:
    def __init__(self,course_taught,**kwargs):
        self.courses_taught = course_taught
        super().__init__(**kwargs)

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Tutor(Person, LearnerMixin, TeacherMixin):
    def __init__(self, *args, **kwargs):#compare to test-mixins.py,the caller and the callee
        #need to have a matching argument signture,
        # see https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
        # super(Tutor, self).__init__(*args, **kwargs)
        print(self.__class__)
        super().__init__(*args,**kwargs)

jane=Tutor('Jane','Smith','SMTJNX045',classes='a_postgrad_course',
           course_taught='an_undergrad_course')
# jane = Tutor("Jane", "Smith", "SMTJNX045")
# print(jane.__dict__)
# jane.enrol('a_postgrad_course')
# jane.assign_teaching('an_undergrad_course')
print(jane.__dict__)
# print(Tutor.mro())
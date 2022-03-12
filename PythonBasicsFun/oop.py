# class: a collection of state (attributes) and
# behavior (methods) that completely describes something
# object: an instance of a class

class Subject:
    """Represents a subject in a research study.
    
    Attributes:
        sid(int): a unique identifier for the subject
        name(str): the subject's name
        measurements(dict of str:float): represents the subject's timestamped
            measurements throughout the study

        num_subjects(int): class-level attribute
            represents the total number of subjects in the study
    """
    num_subjects = 0 # class-level attribute
    # meaning thre is only one num_subjects variables
    # shared across all Subject objects
    # do not declare instance-level attributes here

    # __init__() is a special method
    # for initializing an object like a constructor
    def __init__(self, name, measurements=None):
        # self is like the "this" keyword
        # self refers to the "current" AKA "invoking" object
        self.sid = Subject.num_subjects
        Subject.num_subjects += 1
        self.name = name
        if measurements is None:
            measurements = {}
        self.measurements = measurements

    # __str__() special method
    # invoked implicilt whenever a string representation of an object is needed
    def __str__(self):
        return "SID: " + str(self.sid) + " NAME: " + self.name +\
            " MEASUREMENTS: " + str(self.measurements)

    # non-special instance-level method
    def record_measurement(self, timestamp, value):
        # TODO: should do error checking....
        self.measurements[timestamp] = value

    # non-special class level method
    def display_number_of_subjects():
        print("Number of subjects:", Subject.num_subjects)


sub1 = Subject("bob")
print(sub1) # implicit invocation of __str__()
# self refers to the same object that sub1 refers
print(sub1.__str__()) # explicit invocation
# method invocation syntax: <object ref>.<name of method>()
print(sub1.measurements) # access instance-level attribute
print(Subject.num_subjects) # access class-level attribute

sub2 = Subject("mary")
print(sub2)
print(Subject.num_subjects) # access class-level attribute
# sub2.measurements["1-1-2000 12:00:00"] = 1.5
sub2.record_measurement("1-1-2000 12:00:00", 1.5) # self will refer to sub2

print(sub2)
print(sub1)

Subject.display_number_of_subjects()
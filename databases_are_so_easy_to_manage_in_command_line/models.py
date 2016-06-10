from peewee import *

# create a my_models.db database which will be modified from python script
# as my_models_db
my_models_db = SqliteDatabase('my_models.db', pragmas = (('foreign_keys', True), ))

class BaseModel(Model):
    # is this subclass really a metaclass? below:
    class Meta:
        database = my_models_db
        order_by = ('id', )

class School(BaseModel):
    # CLASS ATTRIBUTES
    # id maps to a column expecting unique ID values
    # name maps to a column expecting char128 non-null values
    id = PrimaryKeyField(unique=True)
    name = CharField(128, null=False) 

    # invoking instance name will return "School: <name> (<id>)"
    def __str__(self):
        return "School: " + self.name + " (" + self.id + ")"

class Batch(BaseModel):
    # CLASS ATTRIBUTES
    # id maps to a column expecting unique ID values
    # school maps to a column expecting ID values from school
    # name maps to a column expecting char 128 non-null values
    id = PrimaryKeyField(unique=True)
    school = ForeignKeyField(School, related_name="batches", on_delete='CASCADE')
    name = CharField(128, null=False)

    # invoking instance name will return "Batch: <name> (<id>)"
    def __str__(self):
        return "Batch: " + self.name + " (" + self.id + ")"

class User(BaseModel):
    # CLASS ATTRIBUTES
    # id maps to a column expecting unique ID values
    # first_name maps to a column expecting char128 values, initialized as empty strings
    # last_name maps to a column expecting char128 non-null values
    # age maps to a column expecting non-null integer values
    id = PrimaryKeyField(unique=True)
    first_name = CharField(128, default="")
    last_name = CharField(128, null=False)
    age = IntegerField(null=False)
    
    # invoking instance name will return "User: <first_name> <last_name> (<id>)"
    def __str__(self):
        return "User: " + self.first_name + " " + self.last_name + " (" + self.id + ")"

class Student(User):
    # CLASS ATTRIBUTE - batch maps to a column expecting ID values from Batch
    batch = ForeignKeyField(Batch, related_name="students", on_delete='CASCADE')

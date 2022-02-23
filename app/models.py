from flask import Markup, url_for, g
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Float, Text
from sqlalchemy.orm import relationship
from flask_appbuilder.models.decorators import renders
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction
from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField, IntField, ObjectIdField


# 学院
class College(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


# 部门
class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


# 专业
class Major(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


# 班级
class MClass(Model):
    __tablename__ = 'mclass'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


# 教师
class Teacher(Model):
    id = Column(Integer, primary_key=True)
    work_num = Column(String(30), unique=True, nullable=False)  # 工号
    name = Column(String(50), nullable=False)
    college_id = Column(Integer, ForeignKey('college.id'), nullable=False)  # 学院
    college = relationship("College")
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)  # 部门
    department = relationship("Department")
    tel_num = Column(String(30), unique=True, nullable=False)  # 电话号
    birthday = Column(Date)

    def __repr__(self):
        return self.name


assoc_teacher_student = Table('teacher_student', Model.metadata,
                              Column('id', Integer, primary_key=True),
                              Column('teacher_id', Integer, ForeignKey('teacher.id')),
                              Column('student_id', Integer, ForeignKey('student.id'))
                              )


# 学生
class Student(Model):
    id = Column(Integer, primary_key=True)
    stu_num = Column(String(30), unique=True, nullable=False)  # 学号
    name = Column(String(50), nullable=False)
    college_id = Column(Integer, ForeignKey('college.id'), nullable=False)
    college = relationship("College")
    major_id = Column(Integer, ForeignKey('major.id'), nullable=False)
    major = relationship("Major")
    mclass_id = Column(Integer, ForeignKey('mclass.id'), nullable=False)
    mclass = relationship("MClass")
    teachers = relationship('Teacher', secondary=assoc_teacher_student, backref='student')
    tel_num = Column(String(30), unique=True, nullable=False)  # 电话号
    birthday = Column(Date)

    def __repr__(self):
        return self.name

# 女生
class Gerl(Model):
    __bind_key__ = 'my_sql'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name
# 用户
class User(Model):
    __bind_key__ = 'my_sql2'
    id = Column(Integer, primary_key=True)
    en = Column(Integer, unique=True, nullable=False)
    user = Column(String(50), unique=True, nullable=False)
    address = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.user

# 测试
class Users(Document):
    # _id = ObjectIdField(primary_key=True)
    name_id = StringField(max_length=20, unique=True, required=True)
    age = IntField(unique=True, required=True)
    name = StringField(max_length=60, required=True, unique=True)
    gender = StringField(max_length=60, required=True)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name

# 回旋测试脚本数据modeo
class Test_Data(Document):
    name = StringField(max_length=20, unique=True, required=True)
    yid = StringField(max_length=50, required=True)
    game_count = IntField(required=True)
    is_test = IntField(required=True)
    cpm = StringField(max_length=50, required=True)
    version_name = StringField(max_length=60, required=True)
    channel_name = StringField(max_length=60, required=True)
    game_version = StringField(max_length=60, required=True)
    device_id = StringField(max_length=60, required=True)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name

from flask import render_template, flash
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, MultipleView, MasterDetailView
from app import appbuilder, db
from flask_appbuilder import AppBuilder, expose, BaseView, has_access, SimpleFormView
from flask_babel import lazy_gettext as _
from flask_appbuilder.charts.views import DirectByChartView

from wtforms import Form, StringField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm

from flask_appbuilder.widgets import ListThumbnail
from .models import College, Department, Major, MClass, Teacher, Student, Gerl, User
from flask_appbuilder.actions import action
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, Select2Widget


# 这里定义了学院、部门、专业、班级、教师和学生的相关视图。
# 代码比较简单，直接关联我们定义好的模型就可以了，代码如下：

class CollegeView(ModelView):
    datamodel = SQLAInterface(College)


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)


class MajorView(ModelView):
    datamodel = SQLAInterface(Major)


class MClassView(ModelView):
    datamodel = SQLAInterface(MClass)


class TeacherView(ModelView):
    datamodel = SQLAInterface(Teacher)


class StudentView(ModelView):
    datamodel = SQLAInterface(Student)

class GerlView(ModelView):
    datamodel = SQLAInterface(Gerl)

class UserView(ModelView):
    datamodel = SQLAInterface(User)
    label_columns = {'user': '用户名','address':'地址'}
    list_columns = ['id', 'en', 'user', 'address']
    related_views = [GerlView]
    chart_title = 'Grouped Birth contacts'
    chart_type = 'AreaChart'
    group_by_columns = ['birthday']

    show_template = 'appbuilder/general/model/show_cascade.html'
    edit_template = 'appbuilder/general/model/edit_cascade.html'

    order_columns = ['address', 'user']
    search_columns = ['user', 'address']    #过滤添加

db.create_all()

# 这里将6个视图作为子菜单添加到了`School Manage`菜单中：

appbuilder.add_view(CollegeView, "College", icon="fa-folder-open-o", category_icon = "fa-envelope", category='学校管理', )
appbuilder.add_view(DepartmentView, "Department", icon="gear", category='学校管理')
appbuilder.add_view(MajorView, "Major", icon="gear", category='学校管理')
appbuilder.add_view(MClassView, "班级", icon="gear", category='学校管理')
appbuilder.add_view(TeacherView, "Teacher", icon="gear", category='学校管理')
# appbuilder.add_view(StudentView, "Student", icon="gear", category='学校管理')
appbuilder.add_view(StudentView, "Student", icon="fa-folder-open-o", category_icon = "fa-envelope", category='清理专家')
appbuilder.add_view(GerlView, "Gerl", category='清理专家')
appbuilder.add_view(UserView, "用户", icon = "fa-folder-open-o", category_icon = "fa-envelope", category='用户管理')
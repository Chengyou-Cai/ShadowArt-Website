from django.forms import ModelForm #引入所用Django表单类的基类
from app.models import Moment #引入本应用models.py中定义的Moment类，以便在后面的表单类中关联

class MomentForm(ModelForm):
    class Meta: #定义子类，在Meta中声明与本表单关联的模型类及其字段
        model=Moment
        fields='__all__' #或用列表形式声明所要导入信息 fields=('content','user_name','kind')
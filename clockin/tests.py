from django.test import TestCase

# Create your tests here.
from enum import Enum

DefaultType = Enum('DefaultType', ('阅读写作','教育教养','学习考试','语言学习',
                '健康锻炼','生活习惯','艺术创作','职场训练','其他'))


for name, member in DefaultType.__members__.items():
    print(name, '=>', member, ',', member.value)


INSERT INTO defaulttype  (name)  VALUES  ('阅读写作'),('教育教养'),('学习考试');
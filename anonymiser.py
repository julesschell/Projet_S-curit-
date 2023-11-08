from insanonym_utils import models
from insanonym_utils import utils
from insanonym_utils import runner

#utils.sample()

# model1 = models.FileConfigModel.parse_file('parser1.cfg')
# r1 = runner.Runner(model1)
# df1=r1.dataframe
# print(df1)
# r1.execute()
# print(df1)

# model2 = models.FileConfigModel.parse_file('parser2.cfg')
# r2 = runner.Runner(model2)
# df2=r2.dataframe
# print(df2)
# r2.execute()
# print(df2)

# model3 = models.FileConfigModel.parse_file('parser3.cfg')
# r3 = runner.Runner(model3)
# df3=r3.dataframe
# print(df3)
# r3.execute()
# print(df3)

model4 = models.FileConfigModel.parse_file('parser4.cfg')
r4 = runner.Runner(model4)
df4=r4.dataframe
print(df4)
r4.execute()
print(df4)




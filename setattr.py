class SetAtt:
    name = 'rukesh'
    caste = 'shrestha'


S = SetAtt()
setattr(S,'name','shristi')
print(getattr(S,'caste'))
# print(S.name)
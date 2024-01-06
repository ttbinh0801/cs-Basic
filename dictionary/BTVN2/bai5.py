names = {
    'students': [
        {'firstName': 'Nikki', 'lastName': 'Roysden'},
        {'firstName': 'Mervin', 'lastName': 'Friedland'},
        {'firstName': 'Aron', 'lastName': 'Wilkins'}
    ],
    'teachers': [
        {'firstName': 'Amberly', 'lastName': 'Calico'},
        {'firstName': 'Regine', 'lastName': 'Agtarap'}
    ]
}
print('LIST OF STUDENT')
for i in names['students'] :
    print ('- '+i['firstName']+ ' '+ i['lastName'])
print('LIST OF TEACHER')
for j in names['teachers']:
    print ('- '+j['firstName'] + ' ' + j['lastName']) 
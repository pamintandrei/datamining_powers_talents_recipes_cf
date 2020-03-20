import os

files=os.listdir('D:\\getting recipes\\powers\\MonoBehaviour')
dirr='D:\\getting recipes\\powers\\MonoBehaviour\\'
power_list=open('powers.txt','w')

for each_file in files:
    name_dirr=dirr+each_file
    name=each_file[:each_file.find('.Power.PowerDescriptionComponent(Clone).txt')]
    power_list.write(name.rstrip('\n'))
    power_list.write(',')
    with open(name_dirr) as fisier:
        for line in fisier:
            
            
            if(line.find('string StringId')!=-1):
                name=line[line.find('"'):]
                power_list.write(name.rstrip('\n'))
                power_list.write(',')
            
            
            if(line.find('string StringContent')!=-1):
                name=line[line.find('"'):]
                power_list.write(name.rstrip('\n'))
                power_list.write(',')
    
    power_list.write('\n')
power_list.close()
recipe_list=open('talents.txt','w')
i=0
with open('talent_definitions.txt') as file:
    while i < 57291:
        line=file.readline()

        if(line.find('string tree = ')!=-1):
            tree=line[line.find('"'):]
            recipe_list.write(tree.rstrip('\n'))
            recipe_list.write(',')
        if(line.find('int totalPips')!=-1):
            
            total_pips=line[line.find('= '):]
            total_pips=total_pips[1:]
            recipe_list.write(total_pips.rstrip('\n'))
            recipe_list.write(',')
        if(line.find('int pipCost')!=-1):
            
            pip_cost=line[line.find('= '):]
            pip_cost=pip_cost[1:]         
            recipe_list.write(pip_cost.rstrip('\n'))
            recipe_list.write(',')
        if(line.find('TalentGrantEntry talentGrantEntries')!=-1):
            
            auxfile=open('talent_definitions.txt','r')
            number_entries=auxfile.readlines()[i+2]
            
            auxfile.close()
            
            number=number_entries[number_entries.find('= '):]
            number=number[2:]
            
            recipe_list.write(number.rstrip('\n'))
            recipe_list.write(',')
            if(int(number)==1):
                auxfile=open('talent_definitions.txt','r')
                number_entries=auxfile.readlines()[i+8]
            
                auxfile.close()
            
                number=number_entries[number_entries.find('= '):]
                number=number[2:]
            for entires in range(0,int(number)):
                line=file.readline()
                i+=1
                data1=line.find('string data = ')
                statnmae=line.find('string statName = ')
                while(data1==-1 and statnmae==-1):
                    
                    line=file.readline()
                    i+=1     
                    data1=line.find('string data = ')
                    statnmae=line.find('string statName = ')
                power=line[line.find('"'):]
                recipe_list.write(power.rstrip('\n'))
                recipe_list.write(',')
                auxfile=open('talent_definitions.txt','r')
                base=auxfile.readlines()[i+2]
                
                auxfile.close()
                
                if(base.find('float _baseValue =')!=-1):
                    quant=base[base.find('= '):]
                    quant=quant[1:]
                else:
                    quant=1
                try:
                    recipe_list.write(quant.rstrip('\n'))
                except:
                    recipe_list.write(str(quant))

                recipe_list.write(',')
            i+=1
            line=file.readline()
            if(line.find('TStat statList')!=-1):
                auxfile=open('talent_definitions.txt','r')
                number_entries=auxfile.readlines()[i+2]
                auxfile.close()
                number=number_entries[number_entries.find('= '):]
                number=number[2:]
                if(int(number)!=0):
                    for entires in range(0,int(number)):
                        line=file.readline()
                        i+=1

                        statnmae=line.find('string statName = ')
                        while(statnmae==-1):
                            
                            line=file.readline()
                            i+=1     
                            statnmae=line.find('string statName = ')
                        power=line[line.find('"'):]
                        recipe_list.write(power.rstrip('\n'))
                        recipe_list.write(',')
                        auxfile=open('talent_definitions.txt','r')  
                        base=auxfile.readlines()[i+2]
                        
                        auxfile.close()
                        
                        if(base.find('float _baseValue =')!=-1):
                            quant=base[base.find('= '):]
                            quant=quant[1:]
                        else:
                            quant=1
                        try:
                            recipe_list.write(quant.rstrip('\n'))
                        except:
                            recipe_list.write(str(quant))
        
                        recipe_list.write(',')
                    recipe_list.write('talentpath-end-begining,')
            recipe_list.write('\n')
            
        i+=1         
recipe_list.close()
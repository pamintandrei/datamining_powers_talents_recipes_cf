

recipe_list=open('recipes.txt','w')
i=0
with open('crafting_recipes_5.10.txt') as file:
    while i < 73970:
        line=file.readline()

        if(line.find('string _templateName = ')!=-1):
            name=line[line.find('"'):]

            recipe_list.write(name.rstrip('\n'))
            recipe_list.write(',')
        if(line.find('int OutputQuantity')!=-1):
            
            quant=line[line.find('= '):]
            quant=quant[1:]
            recipe_list.write(quant.rstrip('\n'))
            recipe_list.write(',')
            
        if(line.find('CraftingIngredient Ingredients')!=-1):
            
            auxfile=open('crafting_recipes_5.10.txt','r')
            number_ingredients=auxfile.readlines()[i+2]
            
            auxfile.close()
            
            number=number_ingredients[number_ingredients.find('= '):]
            number=number[2:]
            
            recipe_list.write(number.rstrip('\n'))
            recipe_list.write(',')

            for ingrediente in range(0,int(number)):
                line=file.readline()
                i+=1
                while(line.find('string DisplayName = ')==-1):
                    line=file.readline()
                    i+=1
                ingredient=line[line.find('"'):]
                recipe_list.write(ingredient.rstrip('\n'))
                recipe_list.write(',')
                while(line.find('int Quantity')==-1):
                    line=file.readline()
                    i+=1
                quant=line[line.find('= '):]
                quant=quant[1:]
                recipe_list.write(quant.rstrip('\n'))
                recipe_list.write(',')
            recipe_list.write('\n')
        i+=1         
recipe_list.close()
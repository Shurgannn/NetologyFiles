with open('list_of_recipes.txt', encoding='utf-8') as f:
  def get_cook_book():
    global cook_book
    cook_book = {}
    for line in f:
      name_of_dish = line.strip()
      ingridient_count = f.readline()
      cook_book.setdefault(name_of_dish, list())
      for i in range(int(ingridient_count)):
        rec = f.readline().strip().split('|')
        ingredients = {'ingridient_name': rec[0], 'quantity': rec[1], 'measure': rec[2]}
        cook_book[name_of_dish].append(ingredients)
      f.readline()
    return cook_book


  def get_shop_list_by_dishes(dishes, person_count):
    dict_with_ingredients = {}
    for dish in dishes:
      if dish in cook_book:
        for ingridient in cook_book[dish]:
          ingridient_name = ingridient['ingridient_name']
          measure = ingridient['measure']
          quantity1 = int(ingridient['quantity'])
          if ingridient_name not in dict_with_ingredients:
            dict_with_ingredients[ingridient_name] = {'mesure': measure, 'quantity': quantity1 * person_count}
          else:
            dict_with_ingredients[ingridient_name]['measure'] += quantity1 * person_count
      else:
        print("Блюда нет в списке рецептов!")
    return dict_with_ingredients

  get_cook_book()
  print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView,TemplateView


from .models import Ingredients,FoodRecipes
from  .forms import IngForm
# Create your views here.


class HomeView(TemplateView):
    template_name="food/home.html"

class IngredientsListView(ListView):

    model =Ingredients
    # ingredients_list.html

class FoodRecipesListView(ListView):
    model=FoodRecipes
    # foodrecipes_list.html

def edit_ing(request):
    if request.method == 'POST':
        form=IngForm(request.POST)
        if form.is_valid():
            # save data and return user to the home page
            try:
                ingredient=Ingredients.objects.get(name=form.cleaned_data['name'].lower())
                ingredient.quantity=form.cleaned_data['quantity']
                ingredient.save()
                return redirect(reverse('show-ings'))
            except:
                form.save()   
                return redirect(reverse('show-ings'))
    

    else:
        form = IngForm()
    context={
        'form':form
    }
    return render(request, 'food/edit-ing.html',context)



class FoodRecipesCreateView(CreateView):
    model=FoodRecipes
    fields="__all__"
    success_url= reverse_lazy('show-recipes')
    #foodrecipes_form.html



def suggest(request):
    suggested_food=[]
    recipes= FoodRecipes.objects.all()
    ingredients=Ingredients.objects.all()
    for food in recipes:
        existing_ingrdients=0
        required_ingredients=food.recipe.all()
        for req_ing in required_ingredients:
            for ex_ing in ingredients:
                if ex_ing==req_ing:
                    if ex_ing.quantity>0:
                        existing_ingrdients+=1
        if existing_ingrdients== food.needed_ings:
            suggested_food.append(food.name)   
     

    context={
        'suggested_food':suggested_food
        
    }
    return render(request, 'food/suggested-food.html',context)



def weekly_plan(request):
    foods=FoodRecipes.objects.all()
    

    buy_list=[]
    week_program=[]
    while len(week_program)<=21:
        for food in foods:
            week_program.append(food.name)
            buy_ing=food.recipe.all()
            for item in buy_ing:
                buy_list.append(item.name)

            
    


    buy_list=set(buy_list)
    while len(week_program)>21:
        week_program.pop()
    
    context={
        'week_program':week_program,
        'buy_list':buy_list
    }

    return render(request,'food/week-program.html',context)
            


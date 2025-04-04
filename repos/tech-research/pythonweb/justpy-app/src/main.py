import justpy as jp

# Define the function for the route
def test(request):
    wp = jp.WebPage()
    jp.Div(text='Hello, World!', classes='text-3xl m-2', a=wp)
    return wp

# Use JustPy's app function directly to associate the route
jp.justpy(test)
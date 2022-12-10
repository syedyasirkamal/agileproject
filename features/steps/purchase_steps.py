from behave import given, when, then


@given(u'I navigate to purchase page')
def step_impl(context):
    """
        Navigate to login page and as the web server will run in local when we run
        end to end tests using behave, the url will be http://127.0.0.1:5000/login
    """
    context.browser.get('http://127.0.0.1:5000/purchase')

@then(u'I see the Order Now text on the page')
def step_impl(context):
    """
        If the login is successful we will be redirected to http://127.0.0.1:5000/index
        and also see the message "Login successful !!" on that page
    """
    assert context.browser.current_url == 'http://127.0.0.1:5000/purchase'
    assert 'Order Now!' in context.browser.page_source


@then(u'I see an Order Now button')
def step_impl(context):
    """
        Find the Order Now button on the html page with the relevant value
    """
    assert context.browser.find_element("xpath", f"//input[@type='submit' and @value='Order Now!']")




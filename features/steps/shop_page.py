from behave import when, then


@when('Click on sort by')
def click_sort_by(context):
    context.app.shop_page.click_sort_by_option()


@when('User can select the option to sort by selling')
def verify_sort_by_selling(context):
    context.app.shop_page.click_sort_by_selling()


@then('User can click on layaout for three products')
def verify_layout_three_btn(context):
    context.app.shop_page.click_layout_three_btn()


@then('Veirfy the url contains the text "{query}"')
def verify_url_contains_query(context, query):
    context.app.shop_page.verify_url_contains_sort_query(query)

from behave import when, then


@when('Click on sort by')
def click_sort_by(context):
    context.app.shop_page.click_sort_by_option()


@when('Select the option to sort by selling')
def verify_sort_by_selling(context):
    context.app.shop_page.click_sort_by_selling()


@when('Select the option to sort alphabetically A-Z')
def verify_sort_by_alphabetically(context):
    context.app.shop_page.click_sort_by_alphabetically()


@when('Select the option to sort alphabetically Z-A')
def verify_sort_by_alphabetically(context):
    context.app.shop_page.click_sort_by_alphabetically_descending()


@when('Click the option to sort by date from old to new')
def verify_sort_by_date_old_to_new(context):
    context.app.shop_page.click_sort_by_date_old_to_new_option()


@when('Click the option to sort by date from new to old')
def verify_sort_by_date_new_to_old(context):
    context.app.shop_page.click_sort_by_date_new_to_old_option()


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.shop_header.click_cart_icon()


@then('Click on layaout for three products')
def verify_layout_three_btn(context):
    context.app.shop_page.click_layout_three_btn()


@then('Verify the url contains the text "{query}"')
def verify_url_contains_query(context, query):
    context.app.shop_page.verify_url_contains_sort_query(query)


@then('Verify the text "{query}" is displayed')
def verify_text_is_displayed(context, query):
    context.app.shop_page.verify_text_is_displayed(query)

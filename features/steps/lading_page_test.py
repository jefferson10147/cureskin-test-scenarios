from behave import given, when, then

@given('Open landing page')
def open_landing_page(context):
    context.app.landing_page.open_page()


@when('Click on Download option')
def click_download_btn(context):
    context.app.landing_page.click_download_btn()


@when('Switch to the new window')
def switch_to_new_window(context):
    context.app.landing_page.switch_to_new_window()


@then('UI components are visible')
def verify_ui_components(context):
    context.app.header.verify_presence_of_logo()
    context.app.header.verify_presence_of_menu_elements()


@then('User is redirected to the right page')
def verify_redirection(context):
    context.app.header.verify_redirection_to_right_page()

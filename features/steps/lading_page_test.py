from behave import given, when, then

@given('Open landing page')
def open_landing_page(context):
    context.app.landing_page.open_page()


@given('Open shop page')
def open_shop_page(context):
    context.app.shop_page.open_page()


@when('Click on Download option')
def click_download_btn(context):
    context.app.landing_page.click_download_btn()


@when('Switch to the new window')
def switch_to_new_window(context):
    context.app.landing_page.switch_to_new_window()


@when('Click on About Us option')
def click_about_us(context):
    context.app.header.click_about_us()


@when('Click on Testimonials option')
def click_testimonials(context):
    context.app.header.click_testimonials()


@when('Click on Expertise option')
def click_expertise(context):
    context.app.header.click_expertise()


@when('Click on Shop option')
def click_shop(context):
    context.app.header.click_shop()


@when('Click on Contact Us option')
def click_contact_us(context):
    context.app.header.click_contact_us()


@when('Verify title is shown')
def verify_page_contains_title(context):
    context.app.contact_us_page.verify_page_title()


@then('UI components are visible')
def verify_ui_components(context):
    context.app.header.verify_presence_of_logo()
    context.app.header.verify_presence_of_menu_elements()


@then('User is redirected to the right page')
def verify_redirection(context):
    context.app.header.verify_redirection_to_right_page()


@then('User is redirected to About Us page')
def verify_redirection_to_about_us(context):
    context.app.about_us_page.verify_page_is_opened()


@then('User is redirected to Testimonials page')
def verify_redirection_to_testimonials(context):
    context.app.testimonials_page.verify_page_is_opened()


@then('User is redirected to Expertise page')
def verify_redirection_to_expertise(context):
    context.app.expertise_page.verify_page_is_opened()


@then('User is redirected to Shop page')
def verify_redirection_to_shop(context):
    context.app.shop_page.verify_page_is_opened()


@then('User is redirected to Contact Us pages')
def verify_redirection_to_contact_us(context):
    context.app.contact_us_page.verify_page_is_opened()


@then('User can click on each footer links')
def verify_footer_links(context):
    context.app.footer.verify_each_link_is_clickable()

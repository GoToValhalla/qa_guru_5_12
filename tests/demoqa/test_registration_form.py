import os

import allure
from selene import have, by

from utils import attach


@allure.title("Successful fill form")
def test_successful(setup_browser):
    browser = setup_browser
    # first_name = "Alex"
    # last_name = "Egorov"
    #
    # with allure.step("Open registrations form"):
    #     browser.open("https://demoqa.com/automation-practice-form")
    #     browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
    #     browser.driver.execute_script("$('footer').remove()")
    #     browser.driver.execute_script("$('#fixedban').remove()")
    #
    # with allure.step("Fill form"):
    #     browser.element("#firstName").set_value(first_name)
    #     browser.element("#lastName").set_value(last_name)
    #     browser.element("#userEmail").set_value("alex@egorov.com")
    #     browser.element("#genterWrapper").element(by.text("Other")).click()
    #     browser.element("#userNumber").set_value("1231231230")
    #     # browser.element("#dateOfBirthInput").click()
    #     # browser.element(".react-datepicker__month-select").s("July")
    #     # browser.element(".react-datepicker__year-select").selectOption("2008")
    #     # browser.element(".react-datepicker__day--030:not(.react-datepicker__day--outside-month)").click()
    #     browser.element("#subjectsInput").send_keys("Maths")
    #     browser.element("#subjectsInput").press_enter()
    #     browser.element("#hobbiesWrapper").element(by.text("Sports")).click()
    #     # browser.element("#uploadPicture").uploadFromClasspath("img/1.png")
    #     browser.element("#currentAddress").set_value("Some street 1")
    #     browser.element("#state").click()
    #     browser.element("#stateCity-wrapper").element(by.text("NCR")).click()
    #     browser.element("#city").click()
    #     browser.element("#stateCity-wrapper").element(by.text("Delhi")).click()
    #     browser.element("#submit").click()
    #
    # with allure.step("Check form results"):
    #     browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))

    with allure.step("Open registrations form"):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Fill form"):
        browser.element('[id="firstName"]').send_keys('Ivan')
        browser.element('[id="lastName"]').send_keys('Ivanov')
        browser.element('[id="userEmail"]').send_keys('r@ya.com')
        browser.element('[name="gender"][value=Male]').double_click()
        browser.element('[id="userNumber"]').send_keys('7777777777')

        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__year-select').click().element('[value="1990"]').click()
        browser.element('.react-datepicker__month-select').click().element('[value="2"]').click()
        browser.element('.react-datepicker__day--022').click()

        browser.element('#subjectsInput').click().send_keys('Maths').press_enter()

        browser.element('label[for="hobbies-checkbox-1"]').click()

        browser.element('#uploadPicture').send_keys(os.getcwd() + '/test.png')

        browser.element('[id="currentAddress"]').send_keys('Test-city, test street, test house 2')

        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
        browser.element('#react-select-4-input').type('Delhi').press_enter()

        browser.element('#submit').press_enter()
    with allure.step("Check form results"):
        browser.all('tbody tr').should(have.exact_texts(
            'Student Name Ivan Ivanov', 'Student Email r@ya.com', 'Gender Male', 'Mobile 7777777777',
            'Date of Birth 22 March,1990', 'Subjects Maths', 'Hobbies Sports',
            'Picture test.png', 'Address Test-city, test street, test house 2',
            'State and City NCR Delhi'))

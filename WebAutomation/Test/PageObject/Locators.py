

_author_ = 'Subhra Thota'

# youtube site details - https://www.youtube.com/watch?v=rH_agjNXpmw

class Locator(object):


#home page locator

    logo = "//img[@alt='Mercury Tours']"
    singon = "//a[contains(text(),'SIGN-ON')]"
    register = "//a[contains(text(),'REGISTER')]"
    support = "//a[contains(text(),'SUPPORT')]"
    contact = "//a[contains(text(),'CONTACT')]"

# registration page locator

    regis_text = "//*[contains(text(),'basic information')]"
    firstname = "//input[@name='firstName']"
    lastname = "//input[@name='lastName']"
    phone = "//input[@name='phone']"
    email= "//input[@name='userName']"
    address1 = "//input[@name='address1']"
    address2 = "//input[@name='address2']"
    city = "//input[@name='city']"
    state = "//input[@name='state']"
    postalcode ="//input[@name='postalCode']"
    country = "//select[@name='country']"
    username ="//input[@name='email']"
    password = "//input[@name='password']"
    confirmpassword = "//input[@name='confirmPassword']"
    submit = "//input[@name='register']"

# post registration locator

    thank_you = "//*[contains(text(),'Thank you for registering')]"
    username_is = "//*[contains(text(),'Your user name is')]"


# signon page locators

    signon_username = "//input[@name='userName']"
    signon_password = "//input[@name='password']"
    submitlogin = "//input[@name='login']"
    signon_txt = "//*[contains(text(),'Enter your user')]"
    regis_form = "//a[@href='mercuryregister.php']"







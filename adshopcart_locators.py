from faker import Faker

fake = Faker(locale='en_CA')
asc_url = 'https://advantageonlineshopping.com/#/'
asc_create_url = 'https://advantageonlineshopping.com/#/register'
asc_account_url = 'https://advantageonlineshopping.com/#/'
asc_username = 'Shopaos9'
asc_password = 'Myaos9'
asc_email = 'fd9@gmail.com'
username = fake.user_name()
password = fake.password()
email = fake.email()
new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
phone_number = fake.phone_number()
subject = "Great products, excellent online shopping app!"
country = fake.country()
city = fake.city()
address = fake.city()
province = fake.province_abbr()
postalcode = fake.postalcode()

##########################################################_END_OF_LOCATORS_############################################

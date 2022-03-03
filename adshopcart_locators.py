from faker import Faker

fake = Faker(locale='en_CA')
asc_url = 'https://advantageonlineshopping.com/#/'
asc_create_url = 'https://advantageonlineshopping.com/#/register'
asc_account_url = 'https://advantageonlineshopping.com/#/'
asc_username = 'Shopaos8'
asc_password = 'Myaos8'
asc_email = 'fd8@gmail.com'
username = fake.user_name()
password = fake.password()
email = fake.email()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
phone_number = fake.phone_number()
country = fake.country()
city = fake.city()
address = fake.city()
province = fake.province_abbr()
postalcode = fake.postalcode



from api import PetFriends
from settings import valid_email, valid_password,invalid_auth_key
import os

pf = PetFriends()



def test_add_new_pet_with_valid_data_simple(name='пёсель', animal_type='двортерьер',age='4'):
    # Позитивный тест кейс
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name

def test_add_photo_of_pet_with_valid(pet_photo='images/P1040103.jpg'):
    # Позитивный тест кейс

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

        assert status == 200
    else:
        raise Exception("There is no my pets")

def test_get_api_key_for_invalid_user(email=valid_email):
    # Негативный тест кейс
    invalid_password ='0000000'

    status, _ = pf.get_api_key(email, invalid_password)
    assert status == 403


def test_add_new_pet_with_invalid_data(name='', animal_type='',age= "52", pet_photo='images/cat1.txt'):
    # Негативный тест кейс

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, _ = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400


def test_successful_update_self_pet_invalid_info(name='Мурзик', animal_type='Котэ', age='sto'):
   #Негативный тест кейс
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, _ = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 400

    else:
        _= pf.create_pet_simple(auth_key, 'name', 'animal_type', '5')

        status, _ = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 400

def test_get_all_pets_with_invalid_key(filter=''):
    # Негативный тест кейс

    status, _ = pf.get_list_of_pets(invalid_auth_key, filter)
    assert status == 403

def test_add_new_pet_with_invalid_key(name='Барбоскин', animal_type='двортерьер',age='4', pet_photo='images/cat1.jpg'):
    # Негативный тест кейс
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)



    status, _ = pf.add_new_pet(invalid_auth_key, name, animal_type, age, pet_photo)


    assert status == 403

def test_successful_update_self_pet_info_invalid_key(name='Мурзик', animal_type='Котэ', age=5):
    # Негативный тест кейс

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:

        status, _ = pf.update_pet_info(invalid_auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 403

    else:
        _ = pf.create_pet_simple(auth_key, 'name', 'animal_type', '5')
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
        status, _ = pf.update_pet_info(invalid_auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 403
def test_successful_delete_self_pet_invalid_key():
    # Негативный тест кейс

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']

    status, _ = pf.delete_pet(invalid_auth_key, pet_id)

    assert status == 403

def test_create_pet_simple_invalid_key(name='Барбоскин', animal_type='двортерьер', age='4'):
    # Негативный тест кейс

    status, _ = pf.create_pet_simple(invalid_auth_key, name, animal_type, age)

    assert status == 403




from app.models.category import CategoryModel
from app.models.item import ItemModel
from app.models.user import UserModel


def insert_test_data():
    for data in user_data:
        UserModel(**data).save()

    for data in category_data:
        CategoryModel(**data).save()

    for data in item_data:
        ItemModel(**data).save()


user_data = [
    {
        'name': 'Duong Le',
        'email': 'duong@gmail.com',
        'password': '123456'
    },
    {
        'name': 'Minh Phan',
        'email': 'minhp@gmail.com',
        'password': '123456'
    }
]

category_data = [
    {
        'name': 'Spring',
        'description': 'Warm',
        'image_url': 'https://vn.got-it.ai/'
    },
    {
        'name': 'Summer',
        'description': 'Hot',
        'image_url': 'https://vn.got-it.ai/'
    },
    {
        'name': 'Fall',
        'description': 'Cool',
        'image_url': 'https://vn.got-it.ai/'
    },
    {
        'name': 'Winter',
        'description': 'Cold',
        'image_url': 'https://vn.got-it.ai/'
    }
]

item_data = [
    {
        'description': 'Plant',
        'image_url': 'https://vn.got-it.ai/',
        'user_id': 1,
        'category_id': 1
    },
    {
        'description': 'Water',
        'image_url': 'https://vn.got-it.ai/',
        'user_id': 1,
        'category_id': 1
    },
    {
        'description': 'Ground',
        'image_url': 'https://vn.got-it.ai/',
        'user_id': 2,
        'category_id': 1
    },
    {
        'description': 'Sky',
        'image_url': 'https://vn.got-it.ai/',
        'user_id': 1,
        'category_id': 1
    }
]

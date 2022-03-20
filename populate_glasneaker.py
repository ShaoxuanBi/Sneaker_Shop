

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'Sneaker_Shop.settings')

import django 
django.setup()
from Glasneaker.models import Brand, Product




def populate():
# populate data of products and brands


    # data of products

    air_jordans = [
        {

            'name':'Air Jordan1 Retro Sp',
            'description':'Court Purple',
            'picture':'/static/images/11.jpg',
            'price':1100.00,
            'quantity':10,
            'size':'38'
        },
        {

            'name':'Air Jordan1 Retro Sp',
            'description':'Court Purple',
            'picture':'/static/images/11.jpg',
            'price':1100.00,
            'quantity':10,
            'size':'39'
        },
        {

            'name':'Air Jordan1 Retro Sp',
            'description':'Court Purple',
            'picture':'/static/images/11.jpg',
            'price':1100.00,
            'quantity':10,
            'size':'40'
        },
        {

            'name':'Air Jordan1 Retro Sp',
            'description':'Court Purple',
            'picture':'/static/images/11.jpg',
            'price':1100.00,
            'quantity':10,
            'size':'41'
        },
        {

            'name':'Air Jordan1 Retro Sp',
            'description':'Court Purple',
            'picture':'/static/images/11.jpg',
            'price':1100.00,
            'quantity':10,
            'size':'42'
        },
        {

            'name':'Air Jordan1 Retro Sp',
            'description':'Court Purple',
            'picture':'/static/images/11.jpg',
            'price':1100.00,
            'quantity':10,
            'size':'43'
        },
        {

            'name':'Air Jordan1 Retri Sp',
            'description':'TUROBO GREEN',
            'picture':'/static/images/10.jpg',
            'price':565.00,
            'quantity':10,
            'size':'38'
        },
        {

            'name':'Air Jordan1 Retri Sp',
            'description':'TUROBO GREEN',
            'picture':'/static/images/10.jpg',
            'price':565.00,
            'quantity':10,
            'size':'39'
        },
        {

            'name':'Air Jordan1 Retri Sp',
            'description':'TUROBO GREEN',
            'picture':'/static/images/10.jpg',
            'price':565.00,
            'quantity':10,
            'size':'40'
        },
        {

            'name':'Air Jordan1 Retri Sp',
            'description':'TUROBO GREEN',
            'picture':'/static/images/10.jpg',
            'price':565.00,
            'quantity':10,
            'size':'41'
        },
        {

            'name':'Air Jordan1 Retri Sp',
            'description':'TUROBO GREEN',
            'picture':'/static/images/10.jpg',
            'price':565.00,
            'quantity':10,
            'size':'42'
        },
        {

            'name':'Air Jordan1 Retri Sp',
            'description':'TUROBO GREEN',
            'picture':'/static/images/10.jpg',
            'price':565.00,
            'quantity':10,
            'size':'43'
        },
        {

            'name':'Air Jordan1 Retro High OG',
            'description':'CRIMSON',
            'picture':'/static/images/08.jpg',
            'price':290.00,
            'quantity':10,
            'size':'38'
        },
        {

            'name':'Air Jordan1 Retro High OG',
            'description':'CRIMSON',
            'picture':'/static/images/08.jpg',
            'price':290.00,
            'quantity':10,
            'size':'39'
        },
        {

            'name':'Air Jordan1 Retro High OG',
            'description':'CRIMSON',
            'picture':'/static/images/08.jpg',
            'price':290.00,
            'quantity':10,
            'size':'40'
        },
        {

            'name':'Air Jordan1 Retro High OG',
            'description':'CRIMSON',
            'picture':'/static/images/08.jpg',
            'price':290.00,
            'quantity':10,
            'size':'41'
        },
        {

            'name':'Air Jordan1 Retro High OG',
            'description':'CRIMSON',
            'picture':'/static/images/08.jpg',
            'price':290.00,
            'quantity':10,
            'size':'42'
        },
        {

            'name':'Air Jordan1 Retro High OG',
            'description':'CRIMSON',
            'picture':'/static/images/08.jpg',
            'price':290.00,
            'quantity':10,
            'size':'43'
        },
        {

            'name':'Air Jordan1 Retro Sp',
            'description':'Black Toe',
            'picture':'/static/images/aj04.jpeg',
            'price':450.00,
            'quantity':10,
            'size':'38'
        },
        {

            'name':'Air Jordan1 Retro Sp',
            'description':'Black Toe',
            'picture':'/static/images/aj04.jpeg',
            'price':450.00,
            'quantity':10,
            'size':'39'
        },
        {

            'name':'Air Jordan1 Retro Sp',
            'description':'Black Toe',
            'picture':'/static/images/aj04.jpeg',
            'price':450.00,
            'quantity':10,
            'size':'40'
        },
        {

            'name':'Air Jordan1 Retro Sp',
            'description':'Black Toe',
            'picture':'/static/images/aj04.jpeg',
            'price':450.00,
            'quantity':10,
            'size':'41'
        },
        {

            'name':'Air Jordan1 Retro Sp',
            'description':'Black Toe',
            'picture':'/static/images/aj04.jpeg',
            'price':450.00,
            'quantity':10,
            'size':'42'
        },
        {

            'name':'Air Jordan1 Retro Sp',
            'description':'Black Toe',
            'picture':'/static/images/aj04.jpeg',
            'price':450.00,
            'quantity':10,
            'size':'43'
        },
    ]

    yeezy = [

        {

            'name':'Yezzy Boost 350V2',
            'description':'Clay',
            'picture':'/static/images/28.jpg',
            'price':560.00,
            'quantity':20,
            'size':'38'
        },
        {

            'name':'Yezzy Boost 350V2',
            'description':'Clay',
            'picture':'/static/images/28.jpg',
            'price':560.00,
            'quantity':20,
            'size':'39'
        },
        {

            'name':'Yezzy Boost 350V2',
            'description':'Clay',
            'picture':'/static/images/28.jpg',
            'price':560.00,
            'quantity':20,
            'size':'40'
        },
        {

            'name':'Yezzy Boost 350V2',
            'description':'Clay',
            'picture':'/static/images/28.jpg',
            'price':560.00,
            'quantity':20,
            'size':'41'
        },
        {

            'name':'Yezzy Boost 350V2',
            'description':'Clay',
            'picture':'/static/images/28.jpg',
            'price':560.00,
            'quantity':20,
            'size':'42'
        },
        {

            'name':'Yezzy Boost 350V2',
            'description':'Clay',
            'picture':'/static/images/28.jpg',
            'price':560.00,
            'quantity':20,
            'size':'43'
        },
        {

            'name':'Yeezy Boost 350V2',
            'description':'Cream',
            'picture':'/static/images/25.jpg',
            'price':480.00,
            'quantity':20,
            'size':'38'
        },
        {

            'name':'Yeezy Boost 350V2',
            'description':'Cream',
            'picture':'/static/images/25.jpg',
            'price':480.00,
            'quantity':20,
            'size':'39'
        },
         {

            'name':'Yeezy Boost 350V2',
            'description':'Cream',
            'picture':'/static/images/25.jpg',
            'price':480.00,
            'quantity':20,
            'size':'40'
        },
         {

            'name':'Yeezy Boost 350V2',
            'description':'Cream',
            'picture':'/static/images/25.jpg',
            'price':480.00,
            'quantity':20,
            'size':'41'
        },
         {

            'name':'Yeezy Boost 350V2',
            'description':'Cream',
            'picture':'/static/images/25.jpg',
            'price':480.00,
            'quantity':20,
            'size':'42'
        },
         {

            'name':'Yeezy Boost 350V2',
            'description':'Cream',
            'picture':'/static/images/25.jpg',
            'price':480.00,
            'quantity':20,
            'size':'43'
        },
        {

            'name':'Yeezy Boost 700',
            'description':'Wave Runner',
            'picture':'/static/images/31.jpg',
            'price':590.00,
            'quantity':30,
            'size':'38'
        },
        {

            'name':'Yeezy Boost 700',
            'description':'Wave Runner',
            'picture':'/static/images/31.jpg',
            'price':590.00,
            'quantity':30,
            'size':'39'
        },
        {

            'name':'Yeezy Boost 700',
            'description':'Wave Runner',
            'picture':'/static/images/31.jpg',
            'price':590.00,
            'quantity':30,
            'size':'40'
        },
        {

            'name':'Yeezy Boost 700',
            'description':'Wave Runner',
            'picture':'/static/images/31.jpg',
            'price':590.00,
            'quantity':30,
            'size':'41'
        },
        {

            'name':'Yeezy Boost 700',
            'description':'Wave Runner',
            'picture':'/static/images/31.jpg',
            'price':590.00,
            'quantity':30,
            'size':'42'
        },
        {

            'name':'Yeezy Boost 700',
            'description':'Wave Runner',
            'picture':'/static/images/31.jpg',
            'price':590.00,
            'quantity':30,
            'size':'43'
        },
        {

            'name':'Yeezy Boost 700',
            'description':'Mauve',
            'picture':'/static/images/yeezy04.jpeg',
            'price':350.00,
            'quantity':40,
            'size':'38'
        },
        {

            'name':'Yeezy Boost 700',
            'description':'Mauve',
            'picture':'/static/images/yeezy04.jpeg',
            'price':350.00,
            'quantity':40,
            'size':'39'
        },
        {

            'name':'Yeezy Boost 700',
            'description':'Mauve',
            'picture':'/static/images/yeezy04.jpeg',
            'price':350.00,
            'quantity':40,
            'size':'40'
        },
        {

            'name':'Yeezy Boost 700',
            'description':'Mauve',
            'picture':'/static/images/yeezy04.jpeg',
            'price':350.00,
            'quantity':40,
            'size':'41'
        },
        {

            'name':'Yeezy Boost 700',
            'description':'Mauve',
            'picture':'/static/images/yeezy04.jpeg',
            'price':350.00,
            'quantity':40,
            'size':'42'
        },
        {

            'name':'Yeezy Boost 700',
            'description':'Mauve',
            'picture':'/static/images/yeezy04.jpeg',
            'price':350.00,
            'quantity':40,
            'size':'43'
        },
    ]    

# 测试数据
#Test ONLY
    nike = [  
       {

            'name':'Air Jordan1 Retro Sp',
            'description':'Shadow',
            'picture':'/static/images/aj12.jpeg',
            'price':315.00,
            'quantity':5,
            'size':'38'
        },
       {

            'name':'Air Jordan1 Retro Sp',
            'description':'Shadow',
            'picture':'/static/images/aj12.jpeg',
            'price':315.00,
            'quantity':5,
            'size':'39'
        },
       {

            'name':'Air Jordan1 Retro Sp',
            'description':'Shadow',
            'picture':'/static/images/aj12.jpeg',
            'price':315.00,
            'quantity':5,
            'size':'40'
        },
       {

            'name':'Air Jordan1 Retro Sp',
            'description':'Shadow',
            'picture':'/static/images/aj12.jpeg',
            'price':315.00,
            'quantity':5,
            'size':'41'
        },
       {

            'name':'Air Jordan1 Retro Sp',
            'description':'Shadow',
            'picture':'images/aj12.jpeg',
            'price':315.00,
            'quantity':5,
            'size':'42'
        },
       {

            'name':'Air Jordan1 Retro Sp',
            'description':'Shadow',
            'picture':'/static/images/aj12.jpeg',
            'price':315.00,
            'quantity':5,
            'size':'43'
        },

   ]

    adidas = [
       {

            'name':'Yezzy Boost 750',
            'description':'OG',
            'picture':'/static/images/yeezy02.jpeg',
            'price':580.00,
            'quantity':2,
            'size':'43'
        },
       {

            'name':'Yezzy Boost 750',
            'description':'OG',
            'picture':'/static/images/yeezy02.jpeg',
            'price':580.00,
            'quantity':2,
            'size':'42'
        },
       {

            'name':'Yezzy Boost 750',
            'description':'OG',
            'picture':'/static/images/yeezy02.jpeg',
            'price':580.00,
            'quantity':2,
            'size':'41'
        },
       {

            'name':'Yezzy Boost 750',
            'description':'OG',
            'picture':'/static/images/yeezy02.jpeg',
            'price':580.00,
            'quantity':2,
            'size':'40'
        },
       {

            'name':'Yezzy Boost 750',
            'description':'OG',
            'picture':'/static/images/yeezy02.jpeg',
            'price':580.00,
            'quantity':2,
            'size':'39'
        },
       {

            'name':'Yezzy Boost 750',
            'description':'OG',
            'picture':'/static/images/yeezy02.jpeg',
            'price':580.00,
            'quantity':2,
            'size':'38'
        },

   ]
   
   

    # data of brands

    brands = {
        'AirJordans':{'products': air_jordans,'views':0,'likes':0},
        'Yeezy':{'products': yeezy,'views':0,'likes':0},
        'Nike':{'products': nike,'views':0,'likes':0},
        'Adidas':{'products': adidas,'views':0,'likes':0},

    }

    # add brands and products
    for brand, brand_data in brands.items():
        b = add_brand(brand,brand_data['views'],brand_data['likes'])
        for p in brand_data['products']:
            add_product(b,p['name'],p['description'],p['picture'],p['price'],p['quantity'],p['size'])

    # print out the data after population
    # for b in Brand.objects.all():
    #     for p in Product.filter(brand=b):
    #         print(f'-{b}: {p}')


def add_product(b, name, description, picture, price, quantity, size):
    product = Product.objects.get_or_create(brand=b, productname=name)[0]

    product.description = description
    product.picture = picture
    product.price = price
    product.quantity = quantity
    product.size = size

    product.save()

    return product


def add_brand(name, views=0, likes=0):
    brand = Brand.objects.get_or_create(name=name)[0]

    brand.views = views
    brand.likes = likes

    brand.save()
    return brand


# Start execution here
if __name__ == '__main__':
    print('Starting Glasneaker data population...')
    populate()

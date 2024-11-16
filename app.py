from flask import Flask, render_template

app = Flask(__name__)


# TODO: Restaurant List of Dictionaries
# image_url, restaurant_name, status, location, id
restaurants = [
    {
        "id": 1,
        "location": "Makati",
        "restaurant_name": "Restaurant One",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/67468/pexels-photo-67468.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },
    {
        "id": 2,
        "location": "Pasig",
        "restaurant_name": "Restaurant Two",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/25858122/pexels-photo-25858122/free-photo-of-patio-of-cafe.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 3,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Three",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/16550341/pexels-photo-16550341/free-photo-of-facade-of-urban-building.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 4,
        "location": "Quezon CIty",
        "restaurant_name": "Restaurant Four",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/12935080/pexels-photo-12935080.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 5,
        "location": "Alabang",
        "restaurant_name": "Restaurant Five",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/8921562/pexels-photo-8921562.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 6,
        "location": "Pasig",
        "restaurant_name": "Restaurant Six",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/14646764/pexels-photo-14646764.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
    },{
        "id": 7,
        "location": "Barcelona,Spain",
        "restaurant_name": "Restaurant Seven",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.HiCJtT_7bkTvJmsP_rCmtAHaDq?rs=1&pid=ImgDetMain"
    },{
        "id": 8,
        "location": "Paris",
        "restaurant_name": "Restaurant Eight",
        "status": "Open",
        "image_url": "https://d3h1lg3ksw6i6b.cloudfront.net/guide/fr/2020/xlarge/407110_int3_1.jpg"
    },{
        "id": 9,
        "location": "Manila",
        "restaurant_name": "Restaurant Nine",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.h2hoxVzGCtdUMpWijOUrcwAAAA?w=450&h=246&rs=1&pid=ImgDetMain"
    },{
        "id": 10,
        "location": "New York, USA",
        "restaurant_name": "Restaurant Ten",
        "status": "Closed",
        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/16/79/ab/61/tasting-menu.jpg"
    },{
        "id": 11,
        "location": "Caloocan",
        "restaurant_name": "Restaurant Eleven",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.Adn8XOZDbHw8v8OT0-BqIwAAAA?rs=1&pid=ImgDetMain"
    },{
        "id": 12,
        "location": "Quezon City",
        "restaurant_name": "Restaurant Twelve",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.L-swDBSaikwVWWft7shiUQHaEK?rs=1&pid=ImgDetMain"
    },{
        "id": 13,
        "location": "Hong Kong",
        "restaurant_name": "Restaurant Thirteen",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.spjxIz_Mkg07qtMP8toK5wHaHa?rs=1&pid=ImgDetMain"
    },{
        "id": 14,
        "location": "Seoul, South Korea",
        "restaurant_name": "Restaurant Fourteen",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.-xlQUR7Yeym5OdALyvMGDAHaFc?rs=1&pid=ImgDetMain"
    },{
        "id": 15,
        "location": "Davao",
        "restaurant_name": "Restaurant Fifteen",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/R.c2af55399f74b2df989a0a8c3eaac22c?rik=pLuDZoAHS58vgw&riu=http%3a%2f%2fwww.godairyfree.org%2fwp-content%2fuploads%2f2017%2f04%2fthe-butchers-daughter.jpg&ehk=HQOGpfvApyU3E9c%2bwEsP%2bnORukmNZFX05uKzETTCahM%3d&risl=&pid=ImgRaw&r=0"
    },{
        "id": 16,
        "location": "Taguig",
        "restaurant_name": "Restaurant Sixteen",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.zke3uid2fZzC28Dr1KMa8QHaFj?rs=1&pid=ImgDetMain"
    },{
        "id": 17,
        "location": "Madrid, Spain",
        "restaurant_name": "Restaurant Seventeen",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.G6z_mwnIs9t-t3LUCoZ0QwHaFj?rs=1&pid=ImgDetMain"
    },{
        "id": 18,
        "location": "Antipolo",
        "restaurant_name": "Restaurant Eighteen",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.jzbpC7BxVSPp_ixRJQln3QHaFj?rs=1&pid=ImgDetMain"
    },{
        "id": 19,
        "location": "Pampanga",
        "restaurant_name": "Restaurant Nineteen",
        "status": "Open",
        "image_url": "https://cdn.tasteatlas.com/Images/Restaurants/46f1e7f83a7846bd9824e459a4d8eb6d.jpg?mw=1300"
    },{
        "id": 20,
        "location": "Thailand",
        "restaurant_name": "Restaurant Twenty",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.TbOC4riLtL-q51USl_8cRQHaFc?rs=1&pid=ImgDetMain"
    },{
        "id": 21,
        "location": "Mexico City, Mexico",
        "restaurant_name": "Restaurant Twenty-One",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.mqMXao4KDGxfkWU5p-znfQHaE7?rs=1&pid=ImgDetMain"
    },{
        "id": 22,
        "location": "Tagaytay",
        "restaurant_name": "Restaurant Twenty-Two",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.WM3AHD1dZuUSEYLQZehlCAHaFT?rs=1&pid=ImgDetMain"
    },{
        "id": 23,
        "location": "Lima, Peru",
        "restaurant_name": "Restaurant Twenty-Three",
        "status": "Closed",
        "image_url": "https://freight.cargo.site/t/original/i/af4c2cb40aa902d4c4d6613d727507a7f85a456aeffaa39cf9129114b6d01215/9.jpg"
    },{
        "id": 24,
        "location": "Paris, France",
        "restaurant_name": "Restaurant Twenty-Four",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.GQ4dsI-xbDs_k1ZSGZM9yAHaFj?rs=1&pid=ImgDetMain"
    },{
        "id": 25,
        "location": "Atxondo, Spain",
        "restaurant_name": "Restaurant Twenty-Five",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/R.043a8f0e1e4d535fb4bfd4ba4c4b7353?rik=Y%2bjtXWIKI7wAEA&riu=http%3a%2f%2flondoneater.com%2fwp-content%2fuploads%2f2017%2f02%2fExtebarri-4.jpg&ehk=7KRCqk5Jj5fDlJIF3PRaz1f8fxI99qExf7J0YF5duvg%3d&risl=&pid=ImgRaw&r=0"
    },{
        "id": 26,
        "location": "Copenhagen, Denmark",
        "restaurant_name": "Restaurant Twenty-Six",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.vos9T3qrtYTHX8nAUKy3mgHaE8?rs=1&pid=ImgDetMain"
    },{
        "id": 27,
        "location": "Buenos Aires, Argentina",
        "restaurant_name": "Restaurant Twenty-Seven",
        "status": "Open",
        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/12/d8/c1/1c/entrada-al-restaurante.jpg"
    },{
        "id": 28,
        "location": "Davao",
        "restaurant_name": "Restaurant Twenty-Eight",
        "status": "Closed",
        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/1b/03/18/13/benjarong-bar-and-restaurant.jpg"
    },{
        "id": 29,
        "location": "Paranaque",
        "restaurant_name": "Restaurant Twenty-Nine",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.JaKqCh2yZaPLHSzpIFOaAwAAAA?rs=1&pid=ImgDetMain"
    },{
        "id": 30,
        "location": "Tarlac",
        "restaurant_name": "Restaurant Thirty",
        "status": "Closed",
        "image_url": "https://lh3.googleusercontent.com/qAm1QoUrA4iSYXCxKP0Gi_qGsLdpCjT1qP3cybijFMuAieelC2tWLDQzqIn1CHfqraU-WJFhnPRSthN8BtjWAEOvpaA8_gQvjuIgodbBAko4Lr-OAXpXWWLcm_TPwyw8She0LD9av506gqBMajgBmMr9u03jMh2OA-DraTT86uIrgSzMLAeTJV18Efnyjg"
    },{
        "id": 31,
        "location": "Pasay City",
        "restaurant_name": "Restaurant Thirty-One",
        "status": "Closed",
        "image_url": "https://images.squarespace-cdn.com/content/v1/5682b6f957eb8d0dbae2c4b2/1487920956463-UMVAMGML74EWGFV1AJS2/image-asset.jpeg"
    }, {
        "id": 32,
        "location": "Cebu City",
        "restaurant_name": "Restaurant Thirty-Two",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.H9pMKHNvCiNfhPjwdz_g6QHaE7?rs=1&pid=ImgDetMain"
    }, {
        "id": 33,
        "location": "BGC, Philippines",
        "restaurant_name": "Restaurant Thirty-Three",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.2Y3WeV1gXxiGuPrVbi9ySgAAAA?rs=1&pid=ImgDetMain"
    }, {
        "id": 34,
        "location": "Venice, Italy",
        "restaurant_name": "Restaurant Thirty-Four",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.X7rBxoPIdpNdzs1BHkr9YQHaE7?rs=1&pid=ImgDetMain"
    },{
        "id": 35,
        "location": "California, USA",
        "restaurant_name": "Restaurant Thirty-Five",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.bLirOx8-dQ-T12F_NcepnAHaEJ?rs=1&pid=ImgDetMain"
    },{
        "id": 36,
        "location": "Quezon City",
        "restaurant_name": "Restaurant Thirty-Six",
        "status": "Closed",
        "image_url": "https://www.rappler.com/tachyon/r3-assets/BCAD2C3D21A6468BBEC6A1960FA5CD21/img/951C7892759942DAAE924BE67CD91860/9.jpg"
    },{
        "id": 37,
        "location": "Manila",
        "restaurant_name": "Restaurant Thirty-Seven",
        "status": "Open",
        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/0b/a5/22/aa/photo4jpg.jpg"
    },{
        "id": 38,
        "location": "Melbourne, Australia",
        "restaurant_name": "Restaurant Thirty-Eight",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.0YjCWitAow5ZLhPXuKaR5gHaE8?rs=1&pid=ImgDetMain"
    },{
        "id": 39,
        "location": "Tokyo, Japan",
        "restaurant_name": "Restaurant Thirty-Nine",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/R.0c8579ace743a252ecb94c089d420ab7?rik=YvVQT4L8qLYOkg&riu=http%3a%2f%2fc8.alamy.com%2fcomp%2fA58P8P%2fjapan-tokyo-ginza-traditional-japanese-restaurant-A58P8P.jpg&ehk=8Z7wXmeMBl0rerkK%2fRb15LNig9UfcF1Dmv0iTMV40jQ%3d&risl=&pid=ImgRaw&r=0"
    },{
        "id": 40,
        "location": "San Francisco, USA",
        "restaurant_name": "Restaurant Forty",
        "status": "Open",
        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/07/34/19/c8/waterfront-restaurant.jpg"
    },{
        "id": 41,
        "location": "BGC, Philippines",
        "restaurant_name": "Restaurant Forty-One",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.PLqb0HRdyGIbOSGcRFJjXQHaE7?rs=1&pid=ImgDetMain"
    },{
        "id": 42,
        "location": "Hong Kong",
        "restaurant_name": "Restaurant Forty-Two",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.YUcL765mNPc567Z0yBgxlAHaE7?rs=1&pid=ImgDetMain"
    },{
        "id": 43,
        "location": "London",
        "restaurant_name": "Restaurant Forty-Three",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.50bSn9SJY6oilCdAdsx11QHaFS?rs=1&pid=ImgDetMain"
    },{
        "id": 44,
        "location": "Moscow, Russia",
        "restaurant_name": "Restaurant Forty-Four",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.3mmW0c1vePaGjwFyTnVgwAHaEK?rs=1&pid=ImgDetMain"
    },{
        "id": 45,
        "location": "Singapore",
        "restaurant_name": "Restaurant Forty-Five",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/R.e4c1c85ad61004f4d537560f27ea020c?rik=cBsh97VEcrKY2g&riu=http%3a%2f%2fsuper-thai.com%2fwp-content%2fuploads%2f2020%2f10%2fcontact-banner-e1603863951148-900x644.jpg&ehk=TNJ8Rsx%2fACrA5sWgt%2bAtAPKTuYAkDAyi8h64tpclGoQ%3d&risl=&pid=ImgRaw&r=0"
    },{
        "id": 46,
        "location": "Beijing, China",
        "restaurant_name": "Restaurant Forty-Six",
        "status": "Closed",
        "image_url": "https://www.thatsmags.com/image/view/201712/f-bistronome-beijing-6.jpg"
    },{
        "id": 47,
        "location": "New York, USA",
        "restaurant_name": "Restaurant Forty-Seven",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.Rc8HGprX6AmxHNhxzdXzUwHaD4?rs=1&pid=ImgDetMain"
    },{
        "id": 48,
        "location": "Vienna, Austria",
        "restaurant_name": "Restaurant Forty-Eight",
        "status": "Open",
        "image_url": "https://media.cntraveler.com/photos/53da8b10dcd5888e145bb464/master/w_1200,c_limit/cafe-central-vienna-austria-alamy.jpg"
    },{
        "id": 49,
        "location": "Berlin, Germany",
        "restaurant_name": "Restaurant Forty-Nine",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/R.aca34c29c16cea31ee6d57e71e51c550?rik=xxpD52412C92XA&riu=http%3a%2f%2fimg1.10bestmedia.com%2fImages%2fPhotos%2f309423%2fp-Restaurant-Le-Faubourg_54_990x660.jpg&ehk=Qc%2bXiuNOlZmAFB8dUkfxFPxFeU%2fZXskim6wN0GDevNw%3d&risl=&pid=ImgRaw&r=0"
    },{
        "id": 50,
        "location": "Los Angeles, USA",
        "restaurant_name": "Restaurant Fifty",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.Boi0r_Q47n-sERa6uC9UkQHaFj?rs=1&pid=ImgDetMain"
    },                
]      



@app.route('/')
def hello_world():
    print(restaurants);
    return render_template('index.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    past_listings = [{
        'url': 'https://www.zillow.com/homedetails/204-N-Timber-Ct-Harrisburg-PA-17110/86473736_zpid/',  # :contentReference[oaicite:0]{index=0}
        'image_url': 'https://photos.zillowstatic.com/fp/ee9c0d53a83046805ea04d2addb7df11-cc_ft_960.jpg',  # :contentReference[oaicite:1]{index=1}
        'address': '204 N Timber Ct, Harrisburg, PA 17110',  # :contentReference[oaicite:2]{index=2}
        'beds': 2, 'baths': 2, 'sqft': 1232, 'price': 200000, 'date': 'May 5, 2025'  # :contentReference[oaicite:3]{index=3}
    },
    {
        'url': 'https://www.zillow.com/homedetails/991-Ethan-Ct-Harrisburg-PA-17112/86441943_zpid/',  # :contentReference[oaicite:4]{index=4}
        'image_url': 'https://photos.zillowstatic.com/fp/edeb44281352b99523a03e35bcbbbbf9-cc_ft_960.jpg',  # :contentReference[oaicite:5]{index=5}
        'address': '991 Ethan Ct, Harrisburg, PA 17112',  # :contentReference[oaicite:6]{index=6}
        'beds': 3, 'baths': 3, 'sqft': 2131, 'price': 379900, 'date': 'January 3, 2025'  # :contentReference[oaicite:7]{index=7}
    },
    {
        'url': 'https://www.zillow.com/homedetails/6360-Huntingdon-St-Harrisburg-PA-17111/86475234_zpid/',  # :contentReference[oaicite:8]{index=8}
        'image_url': 'https://photos.zillowstatic.com/fp/11be6ca8214625b68a4e5454154e0630-cc_ft_960.jpg',  # :contentReference[oaicite:9]{index=9}
        'address': '6360 Huntingdon St, Harrisburg, PA 17111',  # :contentReference[oaicite:10]{index=10}
        'beds': 2, 'baths': 1, 'sqft': 1168, 'price': 206000, 'date': 'December 30, 2024'  # :contentReference[oaicite:11]{index=11}
    },
    {
        'url': 'https://www.zillow.com/homedetails/3992-Secretariat-St-Harrisburg-PA-17112/303860563_zpid/',  # :contentReference[oaicite:12]{index=12}
        'image_url': 'https://photos.zillowstatic.com/fp/1fa5a45c85ddd0d731e03e10178bfd4f-cc_ft_960.jpg',  # :contentReference[oaicite:13]{index=13}
        'address': '3992 Secretariat St, Harrisburg, PA 17112',  # :contentReference[oaicite:14]{index=14}
        'beds': 5, 'baths': 3, 'sqft': 3688, 'price': 600000, 'date': 'December 6, 2024'  # :contentReference[oaicite:15]{index=15}
    },
    {
        'url': 'https://www.zillow.com/homedetails/4208-Prosperous-Dr-Harrisburg-PA-17112/86436994_zpid/',  # :contentReference[oaicite:16]{index=16}
        'image_url': 'https://photos.zillowstatic.com/fp/e26f325ea2399d2bdae167cfb15d3d96-cc_ft_960.jpg',  # :contentReference[oaicite:17]{index=17}
        'address': '4208 Prosperous Dr, Harrisburg, PA 17112',  # :contentReference[oaicite:18]{index=18}
        'beds': 3, 'baths': 3, 'sqft': 3558, 'price': 599900, 'date': 'December 2, 2024'  # :contentReference[oaicite:19]{index=19}
    }
    ]
    return render_template('index.html', listings=past_listings)

@app.route('/robots.txt')
def robots():
    return send_from_directory('.', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml')

if __name__ == '__main__':
    app.run(debug=True)

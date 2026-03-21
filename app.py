from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ── Home page ──────────────────────────────────────
@app.route('/')
def home():
    return render_template('index.html')

# ── Rooms page ─────────────────────────────────────
@app.route('/rooms')
def rooms():
    room_list = [
        {'name': 'Deluxe Suite',    'price': 4999, 'img': 'deluxe.jpg',   'beds': 2, 'desc': 'Spacious suite with city view and private balcony.'},
        {'name': 'Standard Room',   'price': 1999, 'img': 'standard.jpg', 'beds': 1, 'desc': 'Comfortable room with modern amenities.'},
        {'name': 'Family Room',     'price': 6999, 'img': 'family.jpg',   'beds': 3, 'desc': 'Perfect for families, with extra space and bunk beds.'},
        {'name': 'Presidential Suite', 'price': 14999, 'img': 'pres.jpg', 'beds': 2, 'desc': 'Top-floor luxury with panoramic views.'},
    ]
    return render_template('rooms.html', rooms=room_list)

# ── Booking page ───────────────────────────────────
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name        = request.form.get('name')
        email       = request.form.get('email')
        checkin     = request.form.get('checkin')
        checkout    = request.form.get('checkout')
        room_type   = request.form.get('room_type')
        guests      = request.form.get('guests')
        return render_template('booking_confirm.html',
                               name=name, email=email,
                               checkin=checkin, checkout=checkout,
                               room_type=room_type, guests=guests)
    return render_template('booking.html')

# ── Contact / About page ───────────────────────────
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

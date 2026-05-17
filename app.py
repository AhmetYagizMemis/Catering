from flask import Flask, render_template, request

app = Flask(__name__)

# Ana sayfamızı açan kısım
@app.route('/')
def ana_sayfa():
    return render_template('index.html')

# Hakkımızda sayfasını açan kısım
@app.route('/hakkimizda')
def hakkimizda():
    return render_template('hakkimizda.html')

# Belgelerimiz sayfasını açan kısım
@app.route('/belgelerimiz')
def belgelerimiz():
    return render_template('belgelerimiz.html')

@app.route('/galeri')
def galeri():
    return render_template('galeri.html')

@app.route('/menu')
def menu_sayfasi():
    return render_template('menu.html')
# İletişim formundan gelen bilgileri yakalayan kısım
@app.route('/mesaj-gonder', methods=['POST'])
def mesaj_gonder():
    isim = request.form.get('isim')
    email = request.form.get('email')
    mesaj = request.form.get('mesaj')
    
    # Şimdilik gelen mesajı ekrana yazdırıyoruz (Mail atma kodunu buraya ekleyeceğiz)
    print(f"YENİ MESAJ VAR! \nKimden: {isim} \nE-posta: {email} \nMesaj: {mesaj}")
    
    return "Mesajınız başarıyla alındı! En kısa sürede dönüş yapacağız."

if __name__ == '__main__':
    app.run(debug=True)
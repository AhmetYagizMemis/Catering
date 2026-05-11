from flask import Flask, render_template, request

app = Flask(__name__)

# Ana sayfamızı açan kısım
@app.route('/')
def ana_sayfa():
    return render_template('index.html')

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
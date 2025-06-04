<div align="center">
  <img src="https://img.shields.io/github/languages/count/gizemkizilay/YayinciAviProjesi?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/gizemkizilay/YayinciAviProjesi?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/gizemkizilay/YayinciAviProjesi?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/gizemkizilay/YayinciAviProjesi?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>


Publisher Hunt Project
Yayıncı Avı Projesi

The Broadcaster Hunt Project is a network security research that aims to analyze connections to online broadcast platforms at the network level and identify the IP addresses, servers, and port numbers used. This project aims to analyze broadcast traffic to popular broadcast and meeting platforms, especially Twitch, YouTube Live, Zoom, Microsoft Teams, and Google Meet. Capturing this traffic with network analysis tools such as Wireshark and obtaining meaningful data provides valuable insights into network security, privacy, and protocol behavior.  

Yayıncı Avı Projesi, çevrimiçi yayın platformlarına yapılan bağlantıları ağ düzeyinde analiz ederek, kullanılan IP adreslerini, sunucuları ve port numaralarını tespit etmeyi amaçlayan bir ağ güvenliği araştırmasıdır. Bu proje, özellikle Twitch, YouTube Live, Zoom, Microsoft Teams, Google Meet gibi popüler yayın ve toplantı platformlarına yapılan yayın trafiğini analiz etmeyi hedefler. Wireshark gibi ağ analiz araçlarıyla bu trafiği yakalayıp anlamlı veriler elde etmek, ağ güvenliği, gizlilik ve protokol davranışı konularında değerli içgörüler sağlar.

---

## Features / *Özellikler*

- Basic traffic capture with Wireshark: Network traffic from live streaming platforms was captured using Wireshark.
  Wireshark ile temel trafik kaydı: Canlı yayın platformlarına ait ağ trafiği Wireshark kullanılarak kaydedildi.
- Basic IP and server analysis: IP addresses and servers connected during streaming were identified.  
  *Temel IP ve sunucu analizi: Yayın sırasında bağlanılan IP adresleri ve sunucular tespit edildi.
- Simple Wireshark filters applied: TCP and IP filters were used to make network traffic easier to analyze  
  Basit Wireshark filtreleri uygulandı: TCP ve IP filtreleriyle ağ trafiği daha okunabilir hale getirildi.
-  Cross-platform traffic comparison performed: raffic volumes from platforms like Twitch, YouTube, and Zoom were compared.
  Platformlar arası trafik karşılaştırması yapıldı: Twitch, YouTube ve Zoom gibi platformlarda oluşan trafik hacimleri karşılaştırıldı.

---

## Team / *Ekip*

- 2420191015 - Gizem Kızılay: Proje Sahibi / Project Owner  
 
---

## Roadmap / *Yol Haritası*

See our plans in [ROADMAP.md](ROADMAP.md).  
*Yolculuğu görmek için [ROADMAP.md](ROADMAP.md) dosyasına göz atın.*

---

## Research / *Araştırmalar*

| Topic / *Başlık*        | Link                                    | Description / *Açıklama*                        |
|-------------------------|-----------------------------------------|------------------------------------------------|
| Aircrack Deep Dive      | [researchs/aircrack.md](researchs/aircrack.md) | In-depth analysis of Aircrack-ng suite. / *Aircrack-ng paketinin derinlemesine analizi.* |
| Example Research Topic  | [researchs/your-research-file.md](researchs/your-research-file.md) | Brief overview of this research. / *Bu araştırmanın kısa bir özeti.* |
| Add More Research       | *Link to your other research files*     | *Description of the research*                  |

---

## Installation / *Kurulum*

1. **Clone the Repository / *Depoyu Klonlayın***:  
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```

2. **Set Up Virtual Environment / *Sanal Ortam Kurulumu*** (Recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies / *Bağımlılıkları Yükleyin***:  
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage / *Kullanım*

Run the project:  
*Projeyi çalıştırın:*

```bash
python main.py --input your_file.pcap --output results.txt
```

**Steps**:  
1. Prepare input data (*explain data needed*).  
2. Run the script with arguments (*explain key arguments*).  
3. Check output (*explain where to find results*).  

*Adımlar*:  
1. Giriş verilerini hazırlayın (*ne tür verilere ihtiyaç duyulduğunu açıklayın*).  
2. Betiği argümanlarla çalıştırın (*önemli argümanları açıklayın*).  
3. Çıktıyı kontrol edin (*sonuçları nerede bulacağınızı açıklayın*).

---

## Contributing / *Katkıda Bulunma*

We welcome contributions! To help:  
1. Fork the repository.  
2. Clone your fork (`git clone git@github.com:YOUR_USERNAME/YOUR_REPO.git`).  
3. Create a branch (`git checkout -b feature/your-feature`).  
4. Commit changes with clear messages.  
5. Push to your fork (`git push origin feature/your-feature`).  
6. Open a Pull Request.  

Follow our coding standards (see [CONTRIBUTING.md](CONTRIBUTING.md)).  

*Topluluk katkilerini memnuniyetle karşılıyoruz! Katkıda bulunmak için yukarıdaki adımları izleyin ve kodlama standartlarımıza uyun.*

---

## License / *Lisans*

Licensed under the [MIT License](LICENSE.md).  
*MIT Lisansı altında lisanslanmıştır.*

---

## Acknowledgements / *Teşekkürler* (Optional)

Thanks to:  
- Gizem Kızılay (kizilaygzm@gmail.com)
- Istinye University

*Teşekkürler: Harika kütüphaneler ve ilham kaynakları için.*

---

## Contact / *İletişim* (Optional)

Project Maintainer: [Gizem Kızılay/Istinye University] - [kizilaygzm@gmail.com]  
Found a bug? Open an issue.  

*Proje Sorumlusu: [Gizem Kızılay/Istinye University] - [kizilaygzm@gmail.com]. Hata bulursanız bir sorun bildirin.*

---

*Replace placeholders (e.g., YOUR_USERNAME/YOUR_REPO) with your project details.*

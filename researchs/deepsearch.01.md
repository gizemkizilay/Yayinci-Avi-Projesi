**Proje ve Hedefler ve Ozellikler:** 


Yayıncı Avı Projesi, çevrimiçi yayın ve iletişim platformlarına (Twitch, YouTube Stream, Microsoft Teams, Google Meet, Zoom vb.) bağlanıldığında kullanılan IP adreslerini, sunucuları ve port numaralarını tespit etmeyi amaçlayan bir ağ analiz projesidir. Proje kapsamında, bu platformlara yayın yaparken veya yayın izlerken oluşan ağ trafiği incelenerek hangi sunucularla iletişim kurulduğu belirlenir. Wireshark gibi paket analiz araçları kullanılarak bu trafik detaylı şekilde yakalanır ve analiz edilir. Bu süreçte hem capture filter'lar (yayın trafiğini seçici şekilde yakalamak için), hem de display filter'lar (yakalanan trafiği sınıflandırmak ve incelemek için) oluşturulur. Her platformun kullandığı altyapı, CDN'ler (örneğin Google için googlevideo.com alt alanları) ve bağlantı protokolleri analiz edilir. Hedef, bu platformların ağ düzeyinde nasıl çalıştığını ortaya koymaktır. Projenin ileri aşamasında, tüm bu analiz sürecini otomatikleştirecek bir Python betiği geliştirilerek IP tespiti ve filtreleme işlemleri komut satırından yürütülebilir hale getirilir. Böylece benzer projelerde veya adli analizlerde hızlı ve otomatik trafik inceleme imkânı sağlanır. Proje, ağ güvenliği, tersine mühendislik ve yayın altyapısı analizi konularında pratik bilgi kazandırmayı hedefler.



**Görev:** 2025 yılı için [Publisher Hunt Project, 'wireshark kullanarak yazilimcilari agda tesbit etmek (Yazilimci Avi)'] alanındaki en son ve en etkili ilk 10 tekniği/trendi derinlemesine araştır ve belirle.



**Ozellikler** 



**İstenen Çıktı Detayları:**

1.  Belirlenen her bir teknik/trend için kısa ve öz bir başlık.

2.  Her bir tekniğin/trendin ne olduğu, nasıl çalıştığı ve neden önemli olduğuna dair 2-3 cümlelik bir açıklama.

3.  Her bir tekniğin/trendin 2025'teki potansiyel etkileri ve uygulama alanları.

4.  Mümkünse, her bir teknik/trend için güvenilir bir kaynak veya referans (örneğin, yayın adı, konferans, uzman görüşü).

5.  Sonuçları numaralandırılmış bir liste halinde sun.



**Kısıtlamalar:**

- Sadece 2025 yılı ve sonrası için öngörülen veya geçerli olacak tekniklere odaklan.

- Bilgilerin güncel ve doğrulanabilir olmasına özen göster.

- Spekülatif olmayan, kanıta dayalı bilgiler sun.



**Örnek Alanlar :**

-İnternet Yayınları ve Bağlantı Takibi

-Ağ Trafiği Yakalama ve Analizi

-Wireshark Kullanımı ve Temel Filtreler

-IP ve Port Numarası Öğrenme Teknikleri

-Canlı Yayın Platformlarının Temel Ağ Yapısı

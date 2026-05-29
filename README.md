#Turing Makinesi ile Araç Plaka Formatı Tanıyıcı

Bu proje, **Özdevinirler Kuramı (Theory of Computation)** dersi kapsamında geliştirilmiş, **NNLLNNN** formatındaki araç plakalarını doğrulayan bir Deterministik Turing Makinesi (DTM) simülatörüdür.

Sistem, gelen girdiyi karakter bazlı analiz ederek plakanın belirtilen formata uygunluğunu (2 rakam, 2 harf, 3 rakam) adım adım durum geçişleri (state transitions) ile doğrular.

#Proje Hakkında
- **Dil:** Python
- **Model:** Deterministik Turing Makinesi
- **Tanınan Dil:** 7 karakterli (2 Rakam, 2 Büyük Harf, 3 Rakam)
- **Güvenlik:** Kural dışı her karakter için sistem anında `q_reject` durumuna geçerek reddeder.

#Kullanım
Proje herhangi bir harici kütüphane gerektirmez. Terminalde ilgili dizine giderek çalıştırmanız yeterlidir:

```bash
python plaka_taniyici.py

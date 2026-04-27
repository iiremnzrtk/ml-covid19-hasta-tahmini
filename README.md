# 🦠 COVID-19 Hasta Tahmini - Makine Öğrenmesi Projesi

Bu proje, bir kişinin klinik semptomlarına (öksürük, ateş, nefes darlığı vb.) dayanarak COVID-19 olup olmadığını makine öğrenmesi algoritmalarıyla tahmin etmeyi amaçlar.

## 📊 1. Veri Seti Hakkında
Projede Kaggle üzerinde paylaşılan, gerçek hasta verilerini içeren *"COVID-19 Dataset"* kullanılmıştır.
* *Kaynak:* [Kaggle - COVID-19 Dataset](https://www.kaggle.com/datasets/meirnizri/covid19-dataset)
* *Özellikler:* Ateş, öksürük, boğaz ağrısı, nefes darlığı, baş ağrısı, yaş ve cinsiyet gibi 20'den fazla parametre.

## 🛠️ 2. Veri Ön İşleme (EDA)
Veri setini eğitime hazır hale getirmek için şu adımlar uygulanmıştır:
- *Temizleme:* Eksik veya "bilinmeyen" olarak işaretlenmiş veriler temizlendi.
- *Dönüştürme:* Kategorik veriler (Evet/Hayır) sayısal değerlere (1/0) dönüştürüldü.
- *Dengeleme:* Veri setindeki hasta ve sağlıklı birey sayıları analiz edildi.

## 🤖 3. Kullanılan Algoritmalar ve Mantığı
Hocanın isteği üzerine en güçlü iki algoritma seçilmiştir:
1. *Logistic Regression:* Veriler arasındaki olasılığı hesaplayarak sınıflandırma yapar. Başlangıç modeli için idealdir.
2. *Random Forest:* Birçok karar ağacını birleştirerek çalışan, aşırı öğrenmeyi (overfitting) engelleyen güçlü bir modeldir.

## 📈 4. Performans Sonuçları (Model Karşılaştırması)

| Metrik | Logistic Regression | Random Forest |
| :--- | :--- | :--- |
| *Accuracy (Doğruluk)* | %86 | %94 |
| *Precision (Kesinlik)* | %84 | %92 |
| *Recall (Duyarlılık)* | %81 | %89 |

*Sonuç:* Random Forest modeli, karmaşık ilişkileri daha iyi yakaladığı için bu projede en yüksek başarıyı göstermiştir.

---
*Hazırlayan:* İrem Nisa Öztürk  
*Üniversite:* Bartın Üniversitesi  
*Teslim Tarihi:* 20.04.2026

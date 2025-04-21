![/Users/cagdasdag/Downloads/trakya-universitesi-logo.png](media/image1.png){width="1.6771653543307086in"
height="1.6771653543307086in"}

**TRAKYA ÜNİVERSİTESİ**

**MÜHENDİSLİK FAKÜLTESİ**

**BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ**

**YAPAY SİNİR AĞLARINA GİRİŞ**

**PROJE KÜNYESİ**

**PROJE ADI:**

Yapay sinir ağları kullanarak göğüs röntgenlerinden hastalık teşhisi

**PROJE EKİBİ:**

1211602059 -- Barış KESKİN

1211602052 - Erhan Turan BİLİR

1211602029 -- Ferhat YENİLMEZ

**PROJE DANIŞMANI:**

Dr. Öğr. Üyesi Turgut DOĞAN

**Edirne -- 2025**

**İÇİNDEKİLER**

[1. GİRİŞ & PROJENİN TANITIMI
[3](#giriş-projenin-tanitimi)](#giriş-projenin-tanitimi)

[2. KULLANILACAK VERİ SETİ
[3](#kullanilacak-veri-seti)](#kullanilacak-veri-seti)

[3. KULLANILACAK YÖNTEMLER VE MODELLER
[3](#kullanilacak-yöntemler-ve-modeller)](#kullanilacak-yöntemler-ve-modeller)

[4. ÖN İŞLEME VE VERİ HAZIRLAMA
[4](#ön-işleme-ve-veri-hazirlama)](#ön-işleme-ve-veri-hazirlama)

[5. EĞİTİM VE TEST SÜRECİ
[4](#eğitim-ve-test-süreci)](#eğitim-ve-test-süreci)

[6. PROJEDEN BEKLENEN KATKILAR
[4](#projeden-beklenen-katkilar)](#projeden-beklenen-katkilar)

[7. MODELİN BAŞARI DEĞERLENDİRME KRİTERLER
[5](#modelin-başari-değerlendirme-kriterler)](#modelin-başari-değerlendirme-kriterler)

[8. PROJE DEPOSU [5](#proje-deposu)](#proje-deposu)

**\
**

# GİRİŞ & PROJENİN TANITIMI

Bu projede, NIH Chest X-ray veri setindeki göğüs röntgeni görüntülerini
kullanarak hastalığın teşhis edilmesi amaçlanmaktadır. Yapay sinir
ağları kullanılarak, röntgen görüntülerinde hastalık olup olmadığını
belirleyen bir model geliştirilecektir. Bu tür sistemler, doktorlara
destek sağlayarak tanı sürecini hızlandırabilir ve hata oranlarını
azaltabilir

# KULLANILACAK VERİ SETİ

NIH Chest X-ray Dataset

- **İçeriği:** Bu veri seti, 112.120 göğüs röntgeni görüntüsü ve toplam
  15 farklı hastalık etiketi içermektedir. Veriler, çeşitli
  hastalıkların teşhisinde kullanılabilecek şekilde etiketlenmiştir.

- **Link:** https://www.kaggle.com/datasets/nih-chest-xrays

# KULLANILACAK YÖNTEMLER VE MODELLER

> Yapay Sinir Ağları:

- Convolutional Neural Networks (CNN): Görüntüleri analiz edip
  sınıflandırmak için Convolutional Neural Networks (CNN)
  kullanılacaktır. CNN, özellikle görüntü tabanlı verileri işlemek için
  geliştirilen bir yapay sinir ağı türüdür.

- Transfer Learning (Aktarım Öğrenmesi): Daha önce büyük veri setleri
  üzerinde eğitilmiş olan DenseNet ve EfficientNet gibi modeller
  kullanılarak, öğrenme sürecinin hızlandırılması ve doğruluk oranının
  artırılması hedeflenmektedir.

- Grad-CAM: Modelin karar verirken hangi bölgeleri dikkate aldığını
  görselleştirmek için kullanılacaktır. Böylece modelin verdiği
  sonuçları daha iyi yorumlayabiliriz.

# ÖN İŞLEME VE VERİ HAZIRLAMA

- Hatalı veriler analiz edilip temizlenecektir.

- Kayıp veri analizi yapılarak, eksik verilerin dağılımı ve etkileri
  incelenecek ve uygun yöntemlerle giderilecektir.

- Görüntüler belirli bir formata getirilerek boyutlandırma ve
  normalizasyon işlemleri uygulanacaktır.

- Veri artırma teknikleri kullanılarak modelin daha sağlam bir şekilde
  öğrenmesi sağlanacaktır.

# EĞİTİM VE TEST SÜRECİ

- Veri seti; eğitim, doğrulama ve test olmak üzere üç gruba
  ayrılacaktır.

- Modelin başarısını ölçmek için k-katlı çapraz doğrulama yöntemi
  kullanılacaktır. Bu yöntem, modelin farklı veri parçaları üzerinde
  test edilmesini sağlayarak daha güvenilir sonuçlar elde etmeye
  yardımcı olur.

- Modelin farklı ayarlarla eğitilerek en iyi sonucu veren yapı
  belirlenmeye çalışılacaktır.

# PROJEDEN BEKLENEN KATKILAR

- Yapay zeka kullanarak medikal görüntü analizinde hastalık tespitinin
  nasıl yapılabileceğini göstermek.

- Transfer learning ve Grad-CAM gibi teknikleri kullanarak modelin karar
  mekanizmasını daha anlaşılır hale getirmek.

- Doktorların teşhis sürecine yardımcı olabilecek bir model geliştirmek.

# MODELİN BAŞARI DEĞERLENDİRME KRİTERLER

- Doğruluk (Accuracy): Modelin doğru tahmin yapma oranı.

- Kesinlik (Precision): Modelin gerçekten hastalıklı olarak işaretlediği
  vakaların ne kadarının doğru olduğu.

- Duyarlılık (Recall): Modelin tüm hastalıklı vakaları ne kadar iyi
  yakalayabildiği.

- F1-Skoru: Kesinlik ve duyarlılığı dengeleyen bir ölçüm.

- ROC-AUC Skoru: Modelin, hastalık olan ve olmayan vakaları ayırt etme
  yeteneği.

# PROJE DEPOSU

- Github Linki: https://github.com/keserbaros1/ysa-medikal-tani

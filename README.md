# Yapay Sinir Ağlarına Giriş Proje Künyesi

### **Proje Grup Bilgileri:**

> Atakan COŞAR ( )
> 

> Barış KESKİN ( [https://github.com/keserbaros1](https://github.com/keserbaros1) )
> 

> Erhan Turan BİLİR ( [https://github.com/erhanbilir](https://github.com/erhanbilir) )
> 

> Ferhat YENİLMEZ ( [https://github.com/ObsessiveEngineer](https://github.com/ObsessiveEngineer) )
> 

---

### **Problem Tanımı:**

Bu projede, NIH Chest X-ray veri setindeki göğüs röntgeni görüntülerini kullanarak hastalığın teşhis edilmesi amaçlanmaktadır. Yapay sinir ağları kullanılarak, röntgen görüntülerinde hastalık olup olmadığını belirleyen bir model geliştirilecektir. Bu tür sistemler, doktorlara destek sağlayarak tanı sürecini hızlandırabilir ve hata oranlarını azaltabilir.

---

### **Kullanılacak Veri Seti:**

**NIH Chest X-ray Dataset**

- **Link:** [https://www.kaggle.com/datasets/nih-chest-xrays/data?select=Data_Entry_2017.csv](https://www.kaggle.com/datasets/nih-chest-xrays/data?select=Data_Entry_2017.csv)
- **İçeriği:** Bu veri seti, 112.120 göğüs röntgeni görüntüsü ve toplam 15 farklı hastalık etiketi içermektedir. Veriler, çeşitli hastalıkların teşhisinde kullanılabilecek şekilde etiketlenmiştir.

---

### **Kullanılacak Yöntemler ve Modeller:**

- Yapay Sinir Ağları:
    - Convolutional Neural Networks (CNN): Görüntüleri analiz edip sınıflandırmak için Convolutional Neural Networks (CNN) kullanılacaktır. CNN, özellikle görüntü tabanlı verileri işlemek için geliştirilen bir yapay sinir ağı türüdür.
    - **Transfer Learning (Aktarım Öğrenmesi):** Daha önce büyük veri setleri üzerinde eğitilmiş olan DenseNet ve EfficientNet gibi modeller kullanılarak, öğrenme sürecinin hızlandırılması ve doğruluk oranının artırılması hedeflenmektedir.
    - **Grad-CAM:** Modelin karar verirken hangi bölgeleri dikkate aldığını görselleştirmek için kullanılacaktır. Böylece modelin verdiği sonuçları daha iyi yorumlayabiliriz.

---

### **Ön İşleme ve Veri Hazırlama:**

- Hatalı veriler analiz edilip temizlenecektir.
- Kayıp veri analizi yapılarak, eksik verilerin dağılımı ve etkileri incelenecek ve uygun yöntemlerle giderilecektir.
- Görüntüler belirli bir formata getirilerek boyutlandırma ve normalizasyon işlemleri uygulanacaktır.
- Veri artırma (Data Augmentation) teknikleri kullanılarak modelin daha sağlam bir şekilde öğrenmesi sağlanacaktır.

---

### **Eğitim ve Test Süreci:**

- Veri seti; eğitim, doğrulama ve test olmak üzere üç gruba ayrılacaktır.
- Modelin başarısını ölçmek için k-katlı çapraz doğrulama yöntemi kullanılacaktır. Bu yöntem, modelin farklı veri parçaları üzerinde test edilmesini sağlayarak daha güvenilir sonuçlar elde etmeye yardımcı olur.
- Modelin farklı ayarlarla eğitilerek en iyi sonucu veren yapı belirlenmeye çalışılacaktır.

---

### **Projeden Beklenen Katkılar:**

- Yapay zeka kullanarak medikal görüntü analizinde hastalık tespitinin nasıl yapılabileceğini göstermek.
- Transfer learning ve Grad-CAM gibi teknikleri kullanarak modelin karar mekanizmasını daha anlaşılır hale getirmek.
- Doktorların teşhis sürecine yardımcı olabilecek bir model geliştirmek.

---

### **Modelin Başarı Değerlendirme Kriterleri:**

- **Doğruluk (Accuracy):** Modelin doğru tahmin yapma oranı.
- **Kesinlik (Precision):** Modelin gerçekten hastalıklı olarak işaretlediği vakaların ne kadarının doğru olduğu.
- **Duyarlılık (Recall):** Modelin tüm hastalıklı vakaları ne kadar iyi yakalayabildiği.
- **F1-Skoru:** Kesinlik ve duyarlılığı dengeleyen bir ölçüm.
- **ROC-AUC Skoru:** Modelin, hastalık olan ve olmayan vakaları ayırt etme yeteneği.

---

### **Baz Alınacak Çalışmalar:**

- (Akademik makaleler eklenecektir.)

---

### **Proje Deposu:**

- **Github Linki:** [https://github.com/keserbaros1/ysa-medikal-tani](https://github.com/keserbaros1/ysa-medikal-tani)
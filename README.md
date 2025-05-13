# ysa-medikal-tani

Göğüs Röntgenlerinde Yapay Zeka ile Hastalık Tanısı

### Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki yazılımlar ve kütüphaneler gereklidir:

- Miniconda3 veya Anaconda (Sanal ortam yönetimi için)
- IDE (`.ipynb` dosyalarını çalıştırmak için)

### Kurulum

1. Projeyi klonlayın:

    ```bash
    git clone https://github.com/keserbaros1/ysa-medikal-tani.git
    ```

2. Proje dizinine gidin:

    ```bash
    cd ysa-medikal-tani
    ```

3. Conda sanal ortamı içeriye aktarma ve paketleri yükleme:

    ```bash
    conda env create -f ysa_env.yml
    ```

6. Veri setini yükleme

    tarayıcınızı açın ve https://www.kaggle.com/datasets/nih-chest-xrays/data sitesine gidin. Download butonuna tıklayın. Download dataset as zip butonuyla indirmeye başlatın. İndirdiğiniz verisetini ysa-medikal-tani\archive olacak şekilde ysa_medikal-tani dizinine çıkartın.

## Kullanımı

Eğitim veri setini hazırlamak için data.ipynb dosyasını çalıştırın.

Eğitim parametrelerini ayarlamak ve modelleri oluşturmak için ysa_hastalik.ipynb dosyasını çalıştırın. ysa_hastalik.ipynb dosyasında Eğitime Başlama başlığının altında eğitmek istediğiniz modelin hücresini düzenleyebilir ve çalıştırabilirsiniz.

Yeni fotoğraflar üretmek için data_generator.ipynb dosyasını çalıştırın.
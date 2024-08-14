# Extractor - File Scanner and Web Viewer

`Extractor`, belirtilen bir klasördeki `.txt` dosyalarını tarayan, dosyalardan e-posta, şifre ve URL bilgilerini çıkaran ve bu bilgileri JSON dosyasına kaydeden bir masaüstü uygulamasıdır. Tarama sonuçları bir web arayüzü ile de görüntülenebilir.

## Özellikler

- Belirtilen klasördeki `.txt` dosyalarını tarar.
- E-posta adresleri, şifreler ve URL'leri çıkarır.
- Tarama sonuçlarını JSON formatında kaydeder.
- Tarama sonuçlarını web arayüzü ile görüntüler.

## Gereksinimler

- Python 3.7+
- Flask
- customtkinter

## Kurulum

1. **Depoyu klonlayın:**

    ```bash
    git clone https://github.com/username/extraxtor.git
    cd extraxtor
    ```

2. **Gerekli paketleri yükleyin:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Proje dosyalarını çalıştırın:**

    ```bash
    python extraxtor.py
    ```

## Kullanım

1. Uygulamayı çalıştırdığınızda, bir masaüstü arayüzü açılır.
2. `Klasör Seç` butonuna tıklayarak taramak istediğiniz klasörü seçin.
3. `Tara` butonuna tıklayın. Bu işlem, klasördeki tüm `.txt` dosyalarını tarar.
4. Tarama tamamlandıktan sonra, sonuçlar tarayıcıda görüntülenecektir.

## Proje Yapısı

- **`extraxtor.py`**: Ana uygulama dosyasıdır. Hem GUI hem de Flask uygulamasını içerir.
- **`templates/index.html`**: Tarama sonuçlarının gösterildiği HTML sayfasıdır.
- **`results.json`**: Tarama sonuçlarının kaydedildiği JSON dosyasıdır.

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir `fork` yapın ve bir `pull request` gönderin. Her türlü öneri ve geliştirme önerisine açığız!

1. Projeyi `fork` edin.
2. Yeni bir `branch` oluşturun: `git checkout -b feature/my-feature`
3. Değişikliklerinizi yapın ve `commit` yapın: `git commit -am 'Add some feature'`
4. `Branch`inizi `push` edin: `git push origin feature/my-feature`
5. Bir `pull request` oluşturun.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.

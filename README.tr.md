# XVault

![XVault Logo](xvault_logo.png)

**XVault**, X (Twitter) gönderilerini ekran görüntüsü olarak yakalayıp saklamak için tasarlanmış bir arşivleme araçları koleksiyonudur. 2025 Türkiye protestoları gibi gerçek zamanlı olayları belgelemek ya da kişisel bir arşiv oluşturmak istediğinizde, XVault tweet görsellerini—metin, resimler ve düzen dahil—gelecekte referans olarak saklamak için esnek seçenekler sunar.

## Amaç
XVault’un amacı, X gönderilerini orijinal halleriyle güvenilir bir şekilde arşivlemektir ve standart API’lerin yalnızca metin sınırlamalarını aşar. Ekran görüntülerini kaydederek XVault, tweetlerin tam bağlamını korumanızı sağlar; bu da araştırmacılar, gazeteciler veya dijital tarihi korumak isteyen herkes için idealdir.

## Özellikler
- Medya ve biçimlendirme dahil tam tweet ekran görüntüleri yakalama.
- Farklı beceri seviyelerine ve ihtiyaçlara uygun çoklu uygulama seçenekleri.
- Arşivleri yerel olarak depolama veya bulut entegrasyonu için uyarlama.
- Kullanım kolaylığı ve özelleştirmeye odaklanma.

## Alt Klasörler
XVault, amacına ulaşmak için çeşitli yaklaşımlar içerir. Her alt klasör benzersiz bir uygulama içerir—teknik tercihinize göre seçim yapın:

- **`Python_Playwright`**: X API entegrasyonu ile Python ve Playwright kullanan otomatik ekran görüntüsü aracı.
- **`Browser_Extension`**: Hızlı, tarayıcı tabanlı yakalamalar için manuel ekran görüntüsü Chrome/Firefox eklentisi.
- **`Node_Puppeteer`**: Başsız tarayıcı ekran görüntüleri için Node.js ve Puppeteer çözümü.
- **`PyQt_App`**: Kullanıcı dostu bir arşivleme deneyimi için PyQt ile oluşturulmuş masaüstü GUI uygulaması.

*Her birinin detayları ve kurulum talimatları ilgili alt klasör README dosyalarında yer almaktadır.*

## Başlarken
1. Bu repoyu klonlayın:
   ```bash
   git clone https://github.com/makalin/XVault.git
   ```
2. Seçtiğiniz uygulamanın alt klasörüne gidin (örneğin, `cd XVault/Python_Playwright`).
3. O alt klasördeki README dosyasındaki kurulum ve kullanım talimatlarını takip edin.

## Gereksinimler
- Bir X Geliştirici hesabı ve API kimlik bilgileri (API tabanlı seçenekler için).
- Seçtiğiniz alt klasörde kullanılan araçlara temel aşinalık (örneğin, Python, Node.js veya tarayıcı eklenti geliştirme).
- Kişisel arşivleme için X’in Hizmet Şartları ve yerel yasalara uygunluk.

## Katkıda Bulunma
Bu repoyu çatallayabilir, çekme istekleri gönderebilir veya XVault’u geliştirmek için fikirlerle talep açabilirsiniz. İşlevselliği artırmak, yeni yöntemler eklemek veya mevcut olanları iyileştirmek için katkınız çok önemli!

## Lisans
Bu proje MIT Lisansı altında lisanslanmıştır—detaylar için [LICENSE](LICENSE) dosyasına bakın.

## Teşekkürler
- 2025 Türkiye protestoları gibi dijital anları koruma ihtiyacından ilham alınarak oluşturulmuştur.
- Tweepy, Playwright, Puppeteer ve PyQt gibi açık kaynak araçlara teşekkürler.

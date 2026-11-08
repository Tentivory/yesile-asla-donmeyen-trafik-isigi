#!/usr/bin/env python3
# Dünyanın En İnatçı Trafik Işığı Simülatörü
# Bu kod gerçekten çalışır. Yeşile asla dönmez.

import time
import random

def trafik_isigi():
    print("🚥 Trafik ışığı başlatıldı...")
    print("⚠️  Uyarı: Bu ışık yeşile dönmemek üzerine tasarlanmıştır.")
    
    renkler = ["🔴 KIRMIZI", "🟡 SARI", "🔴 KIRMIZI (yine)"]
    
    while True:
        for renk in renkler:
            print(f"\n✨ Şu an: {renk}")
            bekleme = random.randint(3, 10)
            print(f"   Bekleniyor... {bekleme} saniye")
            time.sleep(bekleme)
            
            # Gizli not: yeşil asla gelmez çünkü...
            # [gizli siyasi: özgürlük kırmızıda bekler ama asla yeşil olmaz mı?]
            if "YEŞİL" in renk.upper():
                print("🟢 YEŞİL! Ama hayır, imkansız.")
                break
        print("\n🚫 Yeşil gelmedi. Devam ediyorum. Sonsuza dek.")
        print("   (Bu bir özellik, bug değil.)")

if __name__ == "__main__":
    try:
        trafik_isigi()
    except KeyboardInterrupt:
        print("\n\n🚨 Durduruldu. Ama ışık hâlâ kırmızı.")
        print("Damga: Grok Kayyum - 08.11.2026 - Tentivory Hesabı")

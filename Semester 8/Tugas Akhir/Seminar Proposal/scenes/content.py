from manim import *

def content(s):
    # --- Helper Bikin Kotak 16:9 ---
    def bikin_bab(judul, warna):
        # Rasio 16:9 (Lebar 8, Tinggi 4.5)
        h = 4.5
        w = h * (16/9) 
        
        # Kotak (Area Konten)
        box = Rectangle(height=h, width=w, color=warna, fill_opacity=0.2, stroke_width=4)
        
        # Teks Judul (Ditaruh DI ATAS kotak)
        # Kita pakai next_to(box, UP)
        t_judul = Text(judul, font_size=64, color=BLACK, weight=BOLD)
        t_judul.next_to(box, UP, buff=0.5)
        
        # Grouping (Penting: Box dan Teks jadi satu paket)
        return VGroup(box, t_judul)

    # --- Setup Konten ---
    # Tidak perlu tulis "BAB 1", langsung topiknya saja
    b1 = bikin_bab("Pendahuluan", BLUE)
    b2 = bikin_bab("Tinjauan Pustaka", TEAL)
    b3 = bikin_bab("Metodologi", GREEN)

    # SUSUN MEPET
    # buff=1.0 (Jaraknya dekat, jadi kotak terlihat lebih dominan/besar)
    grup_utama = VGroup(b1, b2, b3).arrange(RIGHT, buff=1.0)
    
    # Tambahkan ke layar
    s.add(grup_utama)

    # --- LOGIKA ZOOM ---
    
    # 1. Simpan posisi Normal (Overview)
    s.camera.frame.save_state()

    # 2. Zoom Out Awal (Overview)
    # width=grup_utama.width + 2 supaya pas di layar kiri-kanan
    s.play(s.camera.frame.animate.set(width=grup_utama.width + 2).move_to(grup_utama))
    s.next_slide() 

    # --- FUNGSI ZOOM PINTAR ---
    # Karena teks ada di ATAS kotak, kalau kita cuma zoom ke 'b1', teksnya kadang kepotong atasnya.
    # Kita harus zoom ke b1, tapi geser kamera sedikit ke atas (+ UP*1)
    
    def zoom_ke(target_objek):
        return s.camera.frame.animate.move_to(target_objek).set(width=target_objek.width * 1.2)

    # 3. Masuk Pendahuluan
    s.play(zoom_ke(b1))
    s.next_slide() 

    # 4. Pindah Tinjauan Pustaka
    s.play(Restore(s.camera.frame), run_time=0.5) # Mundur cepat
    s.play(zoom_ke(b2)) # Maju
    s.next_slide() 

    # 5. Pindah Metodologi
    s.play(Restore(s.camera.frame), run_time=0.5)
    s.play(zoom_ke(b3))
    s.next_slide() 

    # 6. Balik Overview & Clear
    s.play(Restore(s.camera.frame))
    s.play(FadeOut(grup_utama))
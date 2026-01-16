from manim import *
from pathlib import Path  
from lib.video_mobject import VideoMobject

# from pendahuluan import *
def bikin_bab(judul, warna, video_path=None):
        # Rasio 16:9
        h = 4.5
        w = h * (16/9)

        # Frame (Garis Tepi)
        frame = Rectangle(
            height=h,
            width=w,
            color=warna,
            stroke_width=4
        )

        # Default isi (fallback jika tidak ada video)
        content_obj = Rectangle(
            height=h,
            width=w,
            fill_opacity=0.15,
            fill_color=warna,
            stroke_width=0
        )

        # Coba load video jika path diberikan
        if video_path is not None:
            path = Path(video_path)
            # Cek apakah file benar-benar ada
            if path.exists() and path.is_file():
                try:
                    # Load video menggunakan class custom
                    content_obj = VideoMobject(
                        str(path),
                        loop=True,
                        speed=1.0
                    )
                    # Sesuaikan ukuran video dengan kotak
                    content_obj.set_width(w) 
                    
                except Exception as e:
                    print(f"[WARNING] Gagal load video '{video_path}': {e}")

        # Posisikan konten di tengah frame
        content_obj.move_to(frame.get_center())

        # Judul
        t_judul = Text(
            judul,
            font_size=64,
            color=BLACK,
            weight=BOLD
        )
        t_judul.next_to(frame, UP, buff=0.2)

        # Grouping: Konten (belakang) -> Frame (depan) -> Judul
        return Group(content_obj, frame, t_judul)

b1 = bikin_bab("Pendahuluan", BLUE,"vid/bab1.mp4")
b2 = bikin_bab("Tinjauan Pustaka", TEAL, "vid/bab2.mp4")
b3 = bikin_bab("Metodologi", GREEN, "vid/bab3.mp4")
bab = [b1, b2, b3]

grup_utama = Group(b1, b2, b3).arrange(RIGHT, buff=1.0)

bg_baru = Rectangle(
  width=config.frame_width *2, # Lebihin dikit biar aman
  height=config.frame_height *2,
  stroke_width=0,
  fill_color=WHITE, # Warna tujuan
  fill_opacity=1
)

def unzoom_section(s, bab_idx):
    zoom_balik = s.camera.frame.animate.move_to(bab[bab_idx-1]).set(width=bab[bab_idx-1].width * 1)
    s.play(zoom_balik,FadeOut(bg_baru), run_time=0.5)
    s.play(FadeIn(grup_utama), lag_ratio=0.25, run_time=0.5)

    animasi_unzoom = s.camera.frame.animate.move_to(bab[bab_idx-1]).set(width=bab[bab_idx-1].width * 1.25)
    s.play(animasi_unzoom)
    s.wait(0.5)


def zoom_section(s,bab_idx):
    animasi_zoom = s.camera.frame.animate.move_to(bab[bab_idx-1]).set(width=bab[bab_idx-1].width * 1.25)

    s.play(animasi_zoom)
    s.next_slide(loop=True)
    s.wait(3) 
    s.next_slide()

    bab_putih = Rectangle(
            height=9,
            width=16,
            fill_opacity=1,
            fill_color=WHITE,
            stroke_width=0
        ).move_to(bab[bab_idx-1].get_center())

    zoom_lagi = s.camera.frame.animate.move_to(bab[bab_idx-1]).set(width=bab[bab_idx-1].width * 1)
  
    bg_baru.set_z_index(-1000) 

    s.play(FadeIn(bab_putih),FadeOut(grup_utama),zoom_lagi,FadeIn(bg_baru), lag_ratio=0.25, run_time=1)
    s.play(Restore(s.camera.frame), FadeOut(bab_putih),run_time=0.2)

def content(s):
    s.play(*[Add(obj, run_time=0.2) for obj in grup_utama], rate_func=smooth)

    s.camera.frame.save_state()


    s.play(s.camera.frame.animate.set(width=grup_utama.width + 2).move_to(grup_utama))
    s.next_slide(loop=True, auto_next=True) 
    s.wait(3) 

    s.next_slide(auto_next=True)
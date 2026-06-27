from manim import *
from manim_slides import Slide
from lib.slide_tracker import *

config.background_color = WHITE

class RevisionScene(Slide):
    def construct(self):
       LS(self)

def LS(s):
    Mobject.set_default(color=BLACK)
    
    judul = Title(r"Rekapitulasi Hasil Pencarian Pasangan Komutatif", color=BLACK, font_size=48)
    judul[-1].set_color(BLACK)
    deskripsi = Tex(r"\parbox{" + str(config.frame_width) + r"cm}{"r"Berikut merupakan hasil penerapan pada pembahasan yang telah diperoleh menggunakan bahasa pemrograman Python", font_size=30, color=BLACK)
    deskripsi.next_to(judul, DOWN, buff=0.3)
    
    col_labels = [
        Tex("Ordo"),
        VGroup(Tex("Latin"), Tex("square")).arrange(DOWN, buff=0.1),
        VGroup(Tex("Pasangan"), Tex("Berbeda")).arrange(DOWN, buff=0.1),
        VGroup(Tex("Komutatif"), Tex("Berbeda")).arrange(DOWN, buff=0.1),
        VGroup(Tex("Komutatif"), Tex("Berbeda")).arrange(DOWN, buff=0.1),
    ]
    
    table_data = [
        ["3", "12", "66", "15", "42"],
        ["4", "576", "165.600", "4.752", "10.080"],
        ["5", "161.280", "13.005.538.560", "460.160", "1.081.560"]
    ]
    
    table = Table(
        table_data,
        col_labels=col_labels,
        include_outer_lines=True,
        line_config={"color": BLACK},
        element_to_mobject=Tex
    )
    table.get_entries().set_color(BLACK)
    for lbl in table.get_col_labels():
        lbl.set_color(BLACK)
        
    table.scale(0.55).next_to(deskripsi, DOWN, buff=0.5)
    
    if table.width > config.frame_width - 1:
        table.width = config.frame_width - 1
        
    s.play(Write(judul), Write(deskripsi))
    s.play(Create(table))
    s.wait(1)
    
    # Animasi kotak penanda kolom 3
    col3_group = VGroup(table.get_col_labels()[2], table.get_columns()[2])
    box = SurroundingRectangle(col3_group, color=PURE_RED, buff=0.15)
    
    ket = Tex(r"Diperoleh dari rumus $\displaystyle\binom{n}{2}$ (dengan $n$ adalah jumlah Latin square)", font_size=30, color=PURE_RED)
    ket.next_to(table, DOWN, buff=0.7)
    
    s.play(Create(box), Write(ket))
    s.wait(2)
    
    # Animasi kotak penanda kolom 4
    col4_group = VGroup(table.get_col_labels()[3], table.get_columns()[3])
    box_new = SurroundingRectangle(col4_group, color=PURE_RED, buff=0.15)
    ket_new = Tex(r"\mbox{Didapat dari \textit{brute-force} (pengecekan satu per satu untuk setiap pasangan berbeda})", font_size=30, color=PURE_RED).next_to(table, DOWN, buff=0.7)
    
    s.play(Transform(box, box_new), Transform(ket, ket_new))
    s.wait(2)
    
    # Animasi kotak penanda kolom 5
    col5_group = VGroup(table.get_col_labels()[4], table.get_columns()[4])
    box_new2 = SurroundingRectangle(col5_group, color=PURE_RED, buff=0.15)
    ket_new2 = Tex(r"Didapat dari mengenakan algoritma ke seluruh matriks Latin square ordo $n$", font_size=30, color=PURE_RED).next_to(table, DOWN, buff=0.7)
    
    s.play(Transform(box, box_new2), Transform(ket, ket_new2))
    s.wait(2)
    
    s.play(FadeOut(VGroup(judul, deskripsi, table, box, ket), scale=0.5))

    

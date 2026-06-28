from manim import *

from lib.slide_tracker import *


def kesimpulan_saran(s):
    s.play(
    s.camera.frame.animate
    .move_to(ORIGIN)
    .set(width=config.frame_width)
    .set_rotation(0), 
    run_time=1.5
    )
    KesimpulanSaran(s)
    next_slide_count(s)
    Lampiran(s)

def Lampiran(s):
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
        VGroup(Tex("Komutatif"), Tex("Algoritma")).arrange(DOWN, buff=0.1),
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
    s.next_slide()
    
    # Animasi kotak penanda kolom 3
    col3_group = VGroup(table.get_col_labels()[2], table.get_columns()[2])
    box = SurroundingRectangle(col3_group, color=PURE_RED, buff=0.15)
    
    ket = Tex(r"Diperoleh dari rumus $\displaystyle\binom{n}{2}$ (dengan $n$ adalah jumlah Latin square)", font_size=30, color=PURE_RED)
    ket.next_to(table, DOWN, buff=0.7)
    
    s.play(Create(box), Write(ket))
    s.wait(1)
    s.next_slide()
    
    # Animasi kotak penanda kolom 4
    col4_group = VGroup(table.get_col_labels()[3], table.get_columns()[3])
    box_new = SurroundingRectangle(col4_group, color=PURE_RED, buff=0.15)
    ket_new = Tex(r"\mbox{Didapat dari \textit{brute-force} (pengecekan satu per satu untuk setiap pasangan berbeda})", font_size=30, color=PURE_RED).next_to(table, DOWN, buff=0.7)
    
    s.play(Transform(box, box_new), Transform(ket, ket_new))
    s.wait(1)
    s.next_slide()
    
    # Animasi kotak penanda kolom 5
    col5_group = VGroup(table.get_col_labels()[4], table.get_columns()[4])
    box_new2 = SurroundingRectangle(col5_group, color=PURE_RED, buff=0.15)
    ket_new2 = Tex(r"Didapat dari mengenakan algoritma ke seluruh matriks Latin square ordo $n$", font_size=30, color=PURE_RED).next_to(table, DOWN, buff=0.7)
    
    s.play(Transform(box, box_new2), Transform(ket, ket_new2))
    s.wait(1)
    s.next_slide()
    
    s.play(FadeOut(VGroup(judul, deskripsi, table, box, ket), scale=0.5))

def KesimpulanSaran(s):
    my_template = TexTemplate()
    my_template.add_to_preamble(r"\usepackage{xcolor}")
    
    kw_hex_map = {
        "Latin square": "FFFF00", 
        "komutatif": "00FF00",
        "centralizer": "00FFFF",
        "superlevel": "FFA500",
        "subgrup abelian": "FFA500"
    }
    
    box_color = GRAY_E
    font_size_judul = 36
    font_size_isi = 28
    
    content_width = config.frame_width + 1.4
    text_width = content_width
    top_margin = 0.5
    
    def clean_text_color(text, mapping):
        for term, hex_code in mapping.items():
            latex_color = f"\\textcolor[HTML]{{{hex_code}}}{{{term}}}"
            text = text.replace(term, latex_color)
        return text
        
    def buat_section(judul_text, isi_list):
        judul = Tex(
            r"\textbf{" + judul_text + r"}", 
            color=BLACK, 
            font_size=font_size_judul,
            tex_template=my_template
        )
        judul.to_edge(LEFT, buff=0)
        items = VGroup()
        for teks_raw in isi_list:
            teks_colored = clean_text_color(teks_raw, kw_hex_map)
            
            item = Tex(
                r"\parbox{" + str(text_width) + r"cm}{" + teks_colored + r"}",
                color=WHITE,
                font_size=font_size_isi,
                tex_template=my_template
            )
            items.add(item)
        
        items.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        kotak = SurroundingRectangle(
            items,
            color=box_color,
            fill_color=box_color,
            fill_opacity=0.9,
            corner_radius=0.2,
            buff=0.3
        )
        
        konten_box = VGroup(kotak, items)
        
        section = VGroup(judul, konten_box).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        return section
        
    list_kesimpulan = [
        r"1. Syarat perlu diperoleh dari elemen maksimum: kandidat permutasi elemen maksimum matriks $B$ harus berada dalam centralizer matriks $A$.",
        r"2. Syarat cukup diperoleh melalui kesamaan subgrup abelian, dan berlaku jika dan hanya jika himpunan superlevel sama di setiap level.",
        r"3. Konstruksi pasangan Latin square komutatif berhasil dirumuskan dalam algoritma komputasional berbasis centralizer dan pemeriksaan superlevel."
    ]
    
    list_saran = [
        r"1. Mengimplementasikan algoritma konstruksi secara komputasi untuk menguji Latin square berordo lebih besar.",
        r"2. Mengkaji efisiensi metode pemeriksaan superlevel agar proses pencarian kandidat dapat dilakukan lebih cepat.",
        r"3. Mengembangkan syarat cukup melalui subgrup abelian ke bentuk aljabar yang lebih umum."
    ]
    
    section_kesimpulan = buat_section("Kesimpulan", list_kesimpulan)
    section_saran = buat_section("Saran", list_saran)
    
    slide_1 = VGroup(section_kesimpulan, section_saran).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
    slide_1.to_edge(LEFT, buff=0.3).to_edge(UP, buff=top_margin)
    
    s.play(Write(slide_1), run_time=1.5)
    s.wait()
    s.next_slide()
    s.play(FadeOut(slide_1, shift=LEFT))
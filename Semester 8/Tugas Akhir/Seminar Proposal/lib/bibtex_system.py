from manim import *

config.background_color = "#FAF9F6"

# ==========================================
# 1. DATABASE "BIBTEX" (Mock .bib File)
# ==========================================
# Simpan ini di paling atas script atau file terpisah
BIB_DATABASE = {
    "diffie1976": {
        "author": "Diffie, W., & Hellman, M.",
        "year": "1976",
        "title": "New directions in cryptography",
        "journal": "IEEE Transactions on Information Theory"
    },
    "rivest1978": {
        "author": "Rivest, R. L., Shamir, A., & Adleman, L.",
        "year": "1978",
        "title": "A method for obtaining digital signatures and public-key cryptosystems",
        "journal": "Communications of the ACM"
    },
    "katz2014": {
        "author": "Katz, J., & Lindell, Y.",
        "year": "2014",
        "title": "Introduction to Modern Cryptography",
        "publisher": "CRC Press"
    }
}

# Variable Global untuk melacak mana yang udah disitasi
USED_CITATIONS = []

class BibManager:
    @staticmethod
    def cite(key, style="authoryear", color=GRAY, scale=0.5):
        """
        Fungsi untuk memanggil sitasi di sebelah teks.
        style: 'authoryear' (Diffie, 1976), 'year' (1976), 'author' (Diffie)
        """
        if key not in BIB_DATABASE:
            print(f"WARNING: Key '{key}' tidak ditemukan di database!")
            return VGroup() # Return kosong biar gak error

        # 1. Catat ke tracker (biar muncul di akhir film)
        if key not in USED_CITATIONS:
            USED_CITATIONS.append(key)

        entry = BIB_DATABASE[key]
        
        # 2. Format Teks Sitasi
        text_str = ""
        # Ambil nama belakang penulis pertama aja buat sitasi singkat
        first_author = entry["author"].split(",")[0] 
        
        if style == "authoryear":
            text_str = f"[{first_author}, {entry['year']}]"
        elif style == "year":
            text_str = f"[{entry['year']}]"
        elif style == "author":
            text_str = f"[{first_author}]"
            
        return Tex(text_str, color=color).scale(scale)

    @staticmethod
    def generate_credits(color=BLACK, scale=0.6, width=10):
        """
        Fungsi untuk generate daftar pustaka lengkap di akhir
        """
        items = VGroup()
        title = Text("References", weight=BOLD, color=color).scale(scale * 1.5)
        items.add(title)
        
        # Loop cuma yang pernah dipanggil (cite) aja
        for key in USED_CITATIONS:
            entry = BIB_DATABASE[key]
            # Format ala IEEE/APA: Author. "Title". Journal/Publisher, Year.
            ref_str = f"{entry['author']} ``{entry['title']}'' \\textit{{{entry.get('journal', entry.get('publisher', ''))}}}, {entry['year']}."
            
            ref_tex = Tex(
                f"[{key}] {ref_str}", 
                color=color, 
                tex_environment="flushleft" # Rata kiri
            ).scale(scale)
            
            # Atur lebar paragraf biar gak bablas ke kanan
            ref_tex.set_width(width) 
            items.add(ref_tex)
            
        items.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        return items


# ==========================================
# 2. SCENE ANIMASI UTAMA
# ==========================================
class DiffieHellmanWithBib(Scene):
    def construct(self):
        # Reset tracker setiap kali render (penting!)
        USED_CITATIONS.clear()

        # --- PART 1: MATERI ---
        judul = Title("Sejarah Kriptografi", color=BLACK)
        self.add(judul)

        # Kalimat 1
        text1 = Text("Konsep Public Key pertama kali diperkenalkan.", color=BLACK, font_size=32).shift(UP)
        
        # PANGGIL CITATION: Diffie (Author + Year)
        cite1 = BibManager.cite("diffie1976", style="authoryear")
        cite1.next_to(text1, RIGHT, buff=0.2) # Taruh di sebelah teks

        self.play(Write(text1))
        self.play(FadeIn(cite1, shift=LEFT))
        self.wait(1)

        # Kalimat 2
        text2 = Text("Algoritma RSA menyusul kemudian.", color=BLACK, font_size=32).next_to(text1, DOWN, buff=1)
        
        # PANGGIL CITATION: Rivest (Year Doang)
        cite2 = BibManager.cite("rivest1978", style="year")
        cite2.next_to(text2, RIGHT, buff=0.2)

        self.play(Write(text2))
        self.play(FadeIn(cite2, shift=LEFT))
        self.wait(2)

        # Bersih-bersih slide materi
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )

        # --- PART 2: MOVIE CREDITS (DAFTAR PUSTAKA OTOMATIS) ---
        
        # Generate otomatis dari BibManager
        credits_group = BibManager.generate_credits(color=BLACK)
        
        # Posisikan di bawah layar dulu (buat efek scrolling)
        credits_group.to_edge(DOWN).shift(DOWN * credits_group.height)
        
        # Animasi Scrolling ke Atas (Kek film Marvel wkwk)
        self.play(
            credits_group.animate.move_to(UP * 2), # Naik ke atas
            run_time=5,
            rate_func=linear # Kecepatan konstan
        )
        self.wait(2)
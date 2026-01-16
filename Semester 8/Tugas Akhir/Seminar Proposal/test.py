from manim import *
from itertools import permutations

config.background_color = WHITE

class VisualDerangementS4(Scene):
    def construct(self):
        # --- JUDUL ---
        title = Text("Visualisasi Derangement S4", font_size=36, color=BLACK, weight=BOLD).to_edge(UP)
        subtitle = Text("Mencari permutasi di mana indeks ≠ nilai", font_size=20, color=GRAY).next_to(title, DOWN)
        self.play(Write(title), FadeIn(subtitle))

        # --- GENERATE DATA ---
        perms = list(permutations([1, 2, 3, 4]))
        
        # Container
        all_cards = VGroup()
        card_data = [] # Simpan referensi logika

        # Fungsi bikin kartu cantik
        def create_card(p):
            # Background Kartu
            card_bg = RoundedRectangle(corner_radius=0.1, width=2.2, height=0.8, fill_color=WHITE, fill_opacity=1, stroke_color=GRAY, stroke_width=1)
            
            # Slot Angka
            slots = VGroup()
            fixed_indices = []
            
            for i, val in enumerate(p):
                # i+1 adalah posisi index (1,2,3,4)
                # val adalah nilai
                
                # Kotak kecil per angka
                sq = Square(side_length=0.4, fill_color=WHITE, fill_opacity=0, stroke_width=0)
                num = Text(str(val), font_size=24, color=BLACK).move_to(sq)
                
                # Cek Fixed Point (Nilai == Posisi)
                is_fixed = (val == i + 1)
                if is_fixed:
                    fixed_indices.append(i)
                
                # Indikator posisi kecil di bawah (opsional, biar tau ini posisi ke berapa)
                idx_lbl = Text(str(i+1), font_size=10, color=GRAY).next_to(sq, DOWN, buff=0.05)
                
                slot_group = VGroup(sq, num, idx_lbl)
                slots.add(slot_group)
            
            slots.arrange(RIGHT, buff=0.15).move_to(card_bg)
            
            full_card = VGroup(card_bg, slots)
            return full_card, fixed_indices, slots

        # Buat semua 24 kartu
        for p in perms:
            card_obj, fixed_idxs, slots_ref = create_card(p)
            all_cards.add(card_obj)
            
            is_derangement = (len(fixed_idxs) == 0)
            card_data.append({
                "mobject": card_obj,
                "bg": card_obj[0],
                "slots": slots_ref,
                "fixed_idxs": fixed_idxs,
                "is_derangement": is_derangement
            })

        # --- LAYOUT GRID (ANTI OVERFLOW) ---
        # Susun 6 baris x 4 kolom
        all_cards.arrange_in_grid(rows=6, cols=4, buff=0.3)
        
        # Scale otomatis agar muat di layar (menyisakan ruang untuk judul)
        max_h = config.frame_height - 2.5
        max_w = config.frame_width - 1.0
        
        # Kecilkan grup agar pas
        if all_cards.height > max_h:
            all_cards.scale_to_fit_height(max_h)
        if all_cards.width > max_w:
            all_cards.scale_to_fit_width(max_w)
            
        all_cards.move_to(DOWN * 0.5)

        # Animasi Muncul (Pop up)
        self.play(LaggedStart(*[GrowFromCenter(c) for c in all_cards], lag_ratio=0.03), run_time=2)
        self.wait(0.5)

        # --- ANIMASI LOGIKA (CEK SATU PER SATU) ---
        
        # 1. Highlight yang SALAH (Fixed Points) jadi MERAH
        anims_bad = []
        for data in card_data:
            if not data["is_derangement"]:
                for idx in data["fixed_idxs"]:
                    # Ambil kotak angka yang salah posisi
                    slot_group = data["slots"][idx] 
                    # slot_group[0] adalah Square, slot_group[1] adalah Angka
                    # Warnai angkanya Merah, kotaknya merah muda
                    anims_bad.append(
                        slot_group[1].animate.set_color(RED).set_weight(BOLD)
                    )
                    # Tambahkan background merah pada kotak spesifik
                    bg_bad = Square(side_length=0.4, color=RED, fill_opacity=0.2, stroke_opacity=0).move_to(slot_group[0])
                    # Kita add langsung ke scene biar cepet (hacky but fast visual)
                    self.add(bg_bad) # Static add, nanti di fadeout bareng card
                    data["mobject"].add(bg_bad) # Masukkan ke grup kartu biar ikut gerak

        self.play(AnimationGroup(*anims_bad, lag_ratio=0.01), run_time=1.5)
        self.wait(0.5)

        # 2. Redupkan kartu yang GAGAL (Punya elemen merah)
        anims_dim = []
        good_cards = VGroup()
        bad_cards = VGroup()

        for data in card_data:
            if not data["is_derangement"]:
                anims_dim.append(data["mobject"].animate.set_opacity(0.2))
                bad_cards.add(data["mobject"])
            else:
                # Highlight yang BENAR (Derangement) jadi HIJAU
                anims_dim.append(data["bg"].animate.set_stroke(GREEN, width=4))
                good_cards.add(data["mobject"])

        self.play(AnimationGroup(*anims_dim), run_time=1)
        self.wait(1)

        # --- FILTERING ---
        # Buang yang gagal
        self.play(
            FadeOut(bad_cards),
            FadeOut(subtitle),
            run_time=1
        )

        # Susun ulang 9 Derangement menjadi grid 3x3 yang rapi
        self.play(
            good_cards.animate.arrange_in_grid(rows=3, cols=3, buff=0.5).scale(1.2).move_to(ORIGIN),
            run_time=1.5
        )

        # Label Final
        final_lbl = Text("Total: 9 Derangement", color=GREEN_E, font_size=32).next_to(good_cards, UP, buff=0.5)
        
        # Kotak pembungkus hasil akhir
        final_box = SurroundingRectangle(good_cards, color=GREEN, buff=0.3, corner_radius=0.2)
        
        self.play(Write(final_lbl), Create(final_box))
        
        self.wait(3)
class DerangementExplainer(Scene):
    def construct(self):
        COL_TEXT = BLACK
        COL_SLOT = GRAY
        COL_ITEM = BLUE
        COL_CORRECT = RED   
        COL_WRONG = GREEN   

        title = Title("Apa itu Derangement (!n)?", color=COL_TEXT, font_size=48, include_underline=True)
        subtitle = Text("Permutasi di mana TIDAK ADA elemen yang menempati posisi aslinya.", font_size=24, color=COL_TEXT)
        subtitle.next_to(title, DOWN)

        self.play(Write(title), Write(subtitle), run_time=1)
        self.wait(1)
        
        n = 4
        slots = VGroup()
        items = VGroup()
        
        start_buff = 1.5
        
        for i in range(n):
            slot_box = Square(side_length=1.2, color=COL_SLOT, stroke_width=2)
            label = Integer(i+1, color=COL_SLOT).move_to(slot_box.get_top() + UP*0.3)
            slot_group = VGroup(slot_box, label)
            slots.add(slot_group)
            
            item_circ = Circle(radius=0.4, color=COL_ITEM, fill_opacity=0.5, fill_color=COL_ITEM)
            item_lbl = Integer(i+1, color=WHITE).move_to(item_circ)
            item_group = VGroup(item_circ, item_lbl)
            items.add(item_group)

        slots.arrange(RIGHT, buff=0.5).shift(UP*0.5)
        
        for i, item in enumerate(items):
            item.next_to(slots[i], DOWN, buff=1.5)

        self.play(Create(slots), FadeIn(items), run_time=1)

        def move_items(permutation, label_text, is_derangement):
            anims = []
            targets = []

            for item_idx, slot_idx in enumerate(permutation):
                item = items[item_idx]
                target_slot = slots[slot_idx][0] 
                targets.append(target_slot)
                anims.append(item.animate.move_to(target_slot.get_center()))
            
            lbl_status = Text(label_text, color=COL_TEXT, font_size=36).to_edge(DOWN, buff=1.5)
            
            self.play(*anims, Write(lbl_status), run_time=1)
            
            highlights = [] 
            highlight_anims = [] 
            all_wrong_pos = True
            
            for i, slot_idx in enumerate(permutation):
                
                item = items[i]
                rect = SurroundingRectangle(slots[slot_idx], buff=0.1, stroke_width=4)
                
                if i == slot_idx: 
                    rect.set_color(COL_CORRECT) # 
                    item.set_color(COL_CORRECT)
                    all_wrong_pos = False
                else:
                    rect.set_color(COL_WRONG) 
                    item.set_color(COL_WRONG)
                
                # PERBAIKAN DISINI:
                highlights.append(rect)          # Simpan MOBJECT-nya
                highlight_anims.append(Create(rect)) # Simpan ANIMASI-nya terpisah
            
            # Jalankan animasi Create
            self.play(*highlight_anims, run_time=0.5)
            
            result_text = r"Yes" if is_derangement else r"No"
            col_res = COL_WRONG if is_derangement else COL_CORRECT
            
            lbl_res = Text(result_text, color=col_res, font_size=28, weight=BOLD).next_to(lbl_status, DOWN)
            self.play(Write(lbl_res), run_time=0.5)
            self.wait(1.5)
            
            # 3. Reset
            reset_anims = []
            for i, item in enumerate(items):
                item.set_color(COL_ITEM) # Balik biru
                reset_anims.append(item.animate.next_to(slots[i], DOWN, buff=1.5))
            
            self.play(
                *reset_anims, 
                FadeOut(lbl_status), FadeOut(lbl_res), 
                # SEKARANG INI AKAN BERHASIL KARENA 'h' ADALAH MOBJECT
                *[FadeOut(h) for h in highlights], 
                run_time=0.8
            )
        # --- KASUS 1: IDENTITAS (1->1, 2->2...) ---
        move_items([0, 1, 2, 3], "Kasus 1: Posisi Tetap", False)

        # --- KASUS 2: PARTIAL (1->2, 2->1, tapi 3->3, 4->4) ---
        move_items([1, 0, 2, 3], "Kasus 2: Sebagian Tertukar", False)

        # --- KASUS 3: DERANGEMENT (Semua pindah) ---
        # 1->2, 2->1, 3->4, 4->3
        move_items([1, 0, 3, 2], "Kasus 3: Semua Pindah", True)
        
        # --- KASUS 4: DERANGEMENT LAIN (Geser siklis) ---
        # 1->2, 2->3, 3->4, 4->1
        move_items([1, 2, 3, 0], "Kasus 4: Geser Siklis", True)

        # --- OUTRO: RUMUS ---
        self.play(FadeOut(slots), FadeOut(items), FadeOut(subtitle), run_time=0.5)
        
        formula = MathTex(
            r"!n = n! \sum_{i=0}^{n} \frac{(-1)^i}{i!}",
            color=BLACK, font_size=48
        ).move_to(ORIGIN)
        
        approx = MathTex(r"!n \approx \frac{n!}{e}", color=BLUE, font_size=40).next_to(formula, DOWN, buff=0.5)
        
        self.play(Write(formula), run_time=1)
        self.play(Write(approx), run_time=1)
        self.wait(2)
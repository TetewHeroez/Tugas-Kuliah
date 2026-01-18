from manim import *

def judul(scene):
    main_text_color = BLACK
    accent_line_color = GRAY_E
    subtitle_color = GRAY_D

    logo_its= SVGMobject("assets/ITS.svg",height=1).to_corner(UL, buff=0.3)
    logo_matematika = SVGMobject("assets/M.svg",height=1).next_to(logo_its, RIGHT, buff=0.2)

    t_obj = Paragraph(
        "Latin Square Komutatif atas\nAljabar Max-Plus", 
        alignment="center",
        font_size=48,
        weight=BOLD
    )
    t_obj.set_color(main_text_color)

    line_width = min(t_obj.width, config.frame_width - 4)
    line = Line(start=LEFT * (line_width/2), end=RIGHT * (line_width/2), color=accent_line_color)
    line.stroke_width = 4
 
    subtitle = Text("Oleh: Teosofi Hidayah Agung", font_size=32, slant=ITALIC)
    subtitle.set_color(subtitle_color)

    dospem = Text("Calon Dosen Pembimbing: Muhammad Syifa'ul Mufid, S.Si., M.Si., D.Phil.", font_size=24)
    dospem.set_color(subtitle_color)

    line.next_to(t_obj, DOWN, buff=0.5)
    subtitle.next_to(line, DOWN, buff=0.75)
    dospem.next_to(subtitle, DOWN, buff=0.25) 

    all_group = VGroup(t_obj, line, subtitle, dospem)
    
    all_group.center()

    
    scene.play(
        Write(t_obj),
        GrowFromCenter(line),
        run_time=1.5
    )

    scene.play(
        FadeIn(subtitle, shift=UP),
        FadeIn(dospem, shift=UP),
        Write(logo_its),
        Write(logo_matematika),
        run_time=1
    )
    
    scene.wait(1)

    scene.next_slide(auto_next=True)

    scene.play(
        FadeOut(all_group), 
        Unwrite(logo_its),
        Unwrite(logo_matematika),
        run_time=1
    )
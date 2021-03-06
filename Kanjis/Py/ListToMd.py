def make_single_item(ligne_CSV, color_background):
    # Ligne CSV : Kanji,traduction,Lecture kun 1,Lecture kun 2,Lecture on 1,Lecture on 2,Exemple 1,Exemple 1 kana,Exemple 1 traduction,Exemple 2,Exemple 2 kana,Exemple 2 traduction,Exemple 3,Exemple 3 kana,Exemple 3 traduction,Exemple 4,Exemple 4 kana,Exemple 4 traduction
    # Paramètres
    [background_color_gradient_start, background_color_gradient_end, background_color_gradient_direction] = color_background
    [Kanji, traduction, kun_def_1, kun_def_2, on_def_1, on_def_2, item_exemple_1_jp, item_exemple_1_rt, item_exemple_1_fr, item_exemple_2_jp, item_exemple_2_rt, item_exemple_2_fr, item_exemple_3_jp, item_exemple_3_rt, item_exemple_3_fr, item_exemple_4_jp, item_exemple_4_rt, item_exemple_4_fr] = ligne_CSV

    item =''

    item += f'[et_pb_slider _builder_version="3.0.100" use_background_color_gradient="on" background_color_gradient_start="{background_color_gradient_start}" background_color_gradient_end="{background_color_gradient_end}" background_color_gradient_direction="{background_color_gradient_direction}" border_radii="on|10px|10px|10px|10px" custom_padding="5%|8%|5%|5%" custom_padding_last_edited="on|desktop"]'

    item += f'[et_pb_slide heading="Kanji" _builder_version="3.0.95"]\n<p style="font-size: 250px; text-shadow: 0em 0.1em 0.1em rgba(0,0,0,0.4); padding-left: 3%; line-height: 300px;">{Kanji}</p>\n[/et_pb_slide]'

    item += f'[et_pb_slide heading="Traduction" _builder_version="3.0.95" custom_padding="||80px|"]\n<div class="container" style="display: grid; grid-template-columns: 22% 23% 5% 23% 22%; grid-template-rows: 10% 3px 50px 15% 3px 10% 10%; grid-column-gap: 3%; grid-row-gap: 20px;">\n<div class="item traduction" style="grid-column: 1 / span 5; grid-row: 1 / span 1; text-align: center; font-size: 45px;">'

    item += f'\n<h1>{traduction}</h1>\n</div>\n<div class="item divider" style="grid-column: 1 / span 5; grid-row: 2 / span 1; background-color: #fff;"></div>\n<div class="item kun" style="grid-column: 1 / span 2; grid-row: 3 / span 1; text-align: center; font-size: 35px;">\n<h2>Kun</h2>\n</div>\n<div class="item on" style="grid-column: 4 / span 2; grid-row: 3 / span 1; text-align: center; font-size: 35px;">\n<h2>On</h2>\n</div>\n<div class="item kun_def_1" style="grid-column: 1 / span 1; grid-row: 4 / span 1; font-size: 20px; writing-mode: vertical-rl;">\n\n{kun_def_1}\n\n</div>\n<div class="item kun_def_2" style="grid-column: 2 / span 1; grid-row: 4 / span 1; font-size: 20px; writing-mode: vertical-rl; margin-left: auto; margin-right: auto;">\n\n{kun_def_2}\n\n</div>\n<div class="item kanji" style="grid-column: 3 / span 1; grid-row: 4 / span 1; font-size: 50px; writing-mode: vertical-rl; margin-left: auto; margin-right: auto;">\n\n{Kanji}\n\n</div>\n'

    item += f'<div class="item on_def_1" style="grid-column: 4 / span 1; grid-row: 4 / span 1; font-size: 20px; writing-mode: vertical-rl;">\n\n{on_def_1}\n\n</div>\n<div class="item on_def_2" style="grid-column: 5 / span 1; grid-row: 4 / span 1; font-size: 20px; writing-mode: vertical-rl; margin-left: auto; margin-right: auto;">\n\n{on_def_2}\n\n</div>\n<div class="item divider" style="grid-column: 1 / span 5; grid-row: 5 / span 1; background-color: #fff;"></div>\n'

    item += f'<div class="item exemples" style="grid-column: 1 / span 5; grid-row: 6 / span 1;">\n<h2>Exemples</h2>\n</div>\n<div class="item exemple_1_jp" style="grid-column: 1 / span 1; grid-row: 7 / span 1; font-size: 25px; writing-mode: vertical-rl;"><ruby>{item_exemple_1_jp}<rt>{item_exemple_1_rt}</rt></ruby></div>\n<div class="item exemple_1_fr" style="grid-column: 2 / span 1; grid-row: 7 / span 1; font-size: 15px;">{item_exemple_1_fr}</div>\n'

    item += f'<div class="item exemple_2_jp" style="grid-column: 4 / span 1; grid-row: 7 / span 1; font-size: 25px; writing-mode: vertical-rl;"><ruby>{item_exemple_2_jp}<rt>{item_exemple_2_rt}</rt></ruby></div>\n<div class="item exemple_2_fr" style="grid-column: 5 / span 1; grid-row: 7 / span 1; font-size: 15px;">{item_exemple_2_fr}</div>\n'

    item += f'<div class="item exemple_3_jp" style="grid-column: 1 / span 1; grid-row: 8 / span 1; font-size: 25px; writing-mode: vertical-rl;"><ruby>{item_exemple_3_jp}<rt>{item_exemple_3_rt}</rt></ruby></div>\n<div class="item exemple_3_fr" style="grid-column: 2 / span 1; grid-row: 8 / span 1; font-size: 15px;">{item_exemple_3_fr}</div>\n'

    item += f'<div class="item exemple_4_jp" style="grid-column: 4 / span 1; grid-row: 8 / span 1; font-size: 25px; writing-mode: vertical-rl;"><ruby>{item_exemple_4_jp}間<rt>{item_exemple_4_rt}</rt></ruby></div>\n<div class="item exemple_4_fr" style="grid-column: 5 / span 1; grid-row: 8 / end; font-size: 15px;">{item_exemple_4_fr}</div>\n</div>\n[/et_pb_slide][/et_pb_slider]'

    return item

color_background = ["#fc6076","#ff9a44","1deg"]
ligne_CSV = ["一", "un", "ひと（つ）", "" , "イチ", "イツ", "一個", "イツコ", "un (objet compact)", "一枚", "イチマイ", "un (objet plat)", "唯一の", "ユイツの", "unique", "一人", "ひとり", "une personne"]
item = make_single_item(ligne_CSV, color_background)

ligne_CSV = ["一", "un", "ひと（つ）", "", "イチ","イツ", "一個", "イツコ","un (objet compact)","一枚","イチマイ","un (objet plat)","唯一の","ユイツの","unique","一人","ひとり","une personne"]
# print(item)

def make_page(liste_CSV, list_colors_gradients):

    # Paramètres
    nbre_kanji = len(liste_CSV)
    indice_kanji = 0
    page = ''
    page_col_1 = ''
    page_col_2 = ''

    # Mise en place
    page += '[et_pb_section bb_built="1" _builder_version="3.0.95"][et_pb_row _builder_version="3.0.95"][et_pb_column type="1_2"]'

    for indice_kanji in range(nbre_kanji):
        indice_couleur = indice_kanji % (6-1)

        color_background = list_colors_gradients[indice_couleur]
        ligne_CSV = liste_CSV[indice_kanji]

        item = make_single_item(ligne_CSV, color_background)
        if indice_kanji % 2 == 0 :
            page_col_1 += item
        else:
            page_col_2 += item

    page += page_col_1 + '[/et_pb_column][et_pb_column type="1_2"]' + page_col_2


    page += '[/et_pb_column][/et_pb_row][/et_pb_section]'

    return page

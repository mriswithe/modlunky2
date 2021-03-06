from pathlib import Path

from .base_classes import BaseSpriteLoader


class HudSheet(BaseSpriteLoader):
    # CURRENTLY BROKEN
    _sprite_sheet_path = Path("Data/Textures/hud.png")
    _chunk_size = 32
    _chunk_map = {
        # What are these things?
        "hud_bar_long": (0, 0, 8, 2),
        "hud_bar_medium": (9, 0, 6, 2),
        "hud_bar_short": (0, 2, 4, 2),
        "hud_bar_medium_alt": (10, 12, 6, 2),
        "hud_bar_huge": (0, 10, 14, 2),
        "hud_circular_gradient": (10, 14, 2, 2),
        "hud_ankh": (14, 0, 2, 2),
        # These two might live on half tiles?
        "hud_bomb": (4, 2, 2, 2),
        "hud_rope": (6, 2, 2, 2),
        "hud_dollar": (8, 2, 2, 2),
        "hud_hour_glass": (10, 2, 2, 2),
        "hud_marker": (12, 2, 2, 2),
        "hud_skull": (14, 2, 2, 2),
        "hud_paste": (0, 4, 1, 1),
        "hud_compass": (1, 4, 1, 1),
        "hud_climbing_gloves": (2, 4, 1, 1),
        "hud_pitchers_mitt": (3, 4, 1, 1),
        "hud_spike_shoes": (4, 4, 1, 1),
        "hud_spring_shoes": (5, 4, 1, 1),
        "hud_parachute": (6, 4, 1, 1),
        "hud_speckles": (7, 4, 1, 1),
        "hud_skeleton_key": (0, 5, 1, 1),
        "hud_tablet_of_destiny": (1, 5, 1, 1),
        "hud_alien_compass": (2, 5, 1, 1),
        "hud_empty_1": (3, 5, 1, 1),
        "hud_empty_2": (4, 5, 1, 1),
        "hud_empty_3": (5, 5, 1, 1),
        "hud_empty_4": (6, 5, 1, 1),
        "hud_red_dot": (7, 5, 1, 1),
        "hud_udjat_eye_open": (8, 4, 2, 2),
        "hud_udjat_eye_close": (10, 4, 2, 2),
        "hud_crown": (12, 4, 2, 2),
        "hud_hedjet": (14, 4, 2, 2),
        "hud_heart": (0, 6, 2, 2),
        "hud_heart_poison": (2, 6, 2, 2),
        "hud_heart_curse": (4, 6, 2, 2),
        "hud_bones": (6, 6, 2, 2),
        "hud_eggplant_crown": (8, 6, 2, 2),
        "hud_the_true_crown": (10, 6, 2, 2),
        "hud_hourglass_large": (12, 6, 2, 2),
        "hud_hand_point_down": (14, 6, 2, 2),
        "hud_kapala_0": (0, 8, 2, 2),
        "hud_kapala_1": (2, 8, 2, 2),
        "hud_kapala_2": (4, 8, 2, 2),
        "hud_kapala_3": (6, 8, 2, 2),
        "hud_kapala_4": (8, 8, 2, 2),
        "hud_kapala_5": (10, 8, 2, 2),
        "hud_kapala_6": (12, 8, 2, 2),
        "hud_dollar_large": (14, 8, 2, 2),
        "hud_note": (14, 10, 2, 2),
        "hud_compass_arrow": (0, 12, 4, 4),
        "hud_alien_compass_arrow": (4, 12, 4, 4),
        "hud_marker_sapling": (12, 14, 2, 2),
        "hud_shopkeeper_angry": (14, 14, 2, 2),
    }

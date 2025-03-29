from typing import Union, Tuple, TypeAlias, Dict

ColorType: TypeAlias = Union[
    str,
    Tuple[float, float, float, int]
]

class ThemedStyle:
    @staticmethod
    def add_color_theme(light: ColorType, dark: ColorType) -> Dict:
        """Adiciona um tema de cores como propriedades na classe."""
        return {"Light": light, "Dark": dark}

    background_primary = add_color_theme((0, 0, 0, 1), (1, 1, 1, 1))
    text_color_primary = add_color_theme((1, 1, 1, 1), (0, 0, 0, 1))
    icon_color_primary = add_color_theme((1, 1, 1, 1), (0, 0, 0, 1))
    shadow_color_primary = add_color_theme((0, 0, 0, 1), (1, 1, 1, 1))

    background_secondary = add_color_theme((0.31, 0.32, 0.47, 1), (0.76, 0.211, 0.196, 1))
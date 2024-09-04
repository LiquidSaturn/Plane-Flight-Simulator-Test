from plugins.mod_loader.menu.ui.camera import Camera
from plugins.mod_loader.menu.ui.image import Image

from plugins.mod_loader.objects.mod import Mod

from plugins.mod_loader.global_variables import mouse_buttons_pressed

class Mural:

    creature_grabbed:bool = False

    def __init__(self, parent, mod:Mod, camera:Camera) -> None:

        self.background = Image(camera, f"{mod.directory}/mural/greeb.png", (0, 0), "topleft")
        self.background.visible = False

        self.creature = Image(camera, f"{mod.directory}/mural/creature.png", (400, 0), "topleft")
        self.creature.visible = False

        self.background.scroll_factor_y = 0
        self.creature.scroll_factor_y = 0

    def on_select(self) -> None:
        self.background.visible = True

    def on_deselect(self) -> None:
        self.background.visible = False

    def on_sidebar_retract(self, selected:bool) -> None:

        if not selected: return

        self.creature.visible = True
        self.creature.rect.y = 720

    def on_sidebar_extend_finished(self, selected:bool) -> None:
        if not selected: return
        self.creature.visible = False

    def on_update(self, selected:bool, mouse_position:tuple[int, int]) -> None:

        if not selected: return

        self.creature_grabbed = self.creature.rect.collidepoint(mouse_position) and mouse_buttons_pressed[0]

        if self.creature_grabbed: self.creature.rect.center = mouse_position
        else: self.creature.rect.y -= 3
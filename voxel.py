from ursina import *
import app


class Voxel(Button):
    def __init__(self, posicao=(0, 0, 0), textura=app.grama_texture):
        super().__init__(
            parent=scene,
            position=posicao,
            model='assets/block',
            origin_y=0.5,
            texture=textura,
            color=color.color(0,0,random.uniform(0.9,1)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                if app.block[0] == 1 : Voxel(posicao=self.position + mouse.normal, textura=app.block[1])
                if app.block[0] == 2 : Voxel(posicao=self.position + mouse.normal, textura=app.block[1])
                if app.block[0] == 3 : Voxel(posicao=self.position + mouse.normal, textura=app.block[1])
                if app.block[0] == 4 : Voxel(posicao=self.position + mouse.normal, textura=app.block[1])

            if key == 'right mouse down':
                destroy(self)

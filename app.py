from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

jogo = Ursina()

grama_texture = load_texture('assets/grass_block.png')
pedra_texture = load_texture('assets/stone_block.png')
madeira_texture = load_texture('assets/brick_block.png')
lama_texture = load_texture('assets/dirt_block.png')
ceu_texture = load_texture('assets/skybox.png')
braco_texture = load_texture('assets/arm_texture.png')
punch_sound = Audio('assets/punch_sound',loop = False, autoplay = False)
block = [1, grama_texture]

def update():
    global block

    if held_keys['left mouse'] or held_keys['right mouse']:
        mao.ativo()
    else:
        mao.passivo()

    if held_keys['1']: block = block
    if held_keys['2']: block = [2, pedra_texture]
    if held_keys['3']: block = [3, madeira_texture]
    if held_keys['4']: block = [4, lama_texture]


class Voxel(Button):
    def __init__(self, posicao=(0, 0, 0), textura=grama_texture):
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
                if block[0] == 1: Voxel(posicao=self.position + mouse.normal, textura=block[1])
                if block[0] == 2: Voxel(posicao=self.position + mouse.normal, textura=block[1])
                if block[0] == 3: Voxel(posicao=self.position + mouse.normal, textura=block[1])
                if block[0] == 4: Voxel(posicao=self.position + mouse.normal, textura=block[1])

            if key == 'right mouse down':
                destroy(self)

class Ceu(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = ceu_texture,
			scale = 150,
			double_sided = True)

class Mao(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = braco_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))

	def ativo(self):
		self.position = Vec2(0.3,-0.5)

	def passivo(self):
		self.position = Vec2(0.4,-0.6)


for z in range(30):
    for x in range(20):
        Voxel(posicao=(x, 0, z))

jogador = FirstPersonController()
ceu = Ceu()
mao = Mao()

jogo.run()
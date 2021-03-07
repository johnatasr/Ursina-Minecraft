from ursina import Ursina, load_texture, held_keys
from ursina.prefabs.first_person_controller import FirstPersonController
from voxel import Voxel

jogo = Ursina()

grama_texture = load_texture('assets/grass_block.png')
pedra_texture = load_texture('assets/stone_block.png')
madeira_texture = load_texture('assets/brick_block.png')
lama_texture = load_texture('assets/dirt_block.png')


def set_block():
    global block

    if held_keys['1']: block = [1, grama_texture]
    if held_keys['2']: block = [2, pedra_texture]
    if held_keys['3']: block = [3, madeira_texture]
    if held_keys['4']: block = [4, lama_texture]


for z in range(30):
    for x in range(20):
        Voxel(posicao=(x, 0, z))

jogador = FirstPersonController()

jogo.run()
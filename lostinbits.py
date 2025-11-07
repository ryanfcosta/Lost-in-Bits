import pygame
from PPlay import window, sprite, keyboard

path = "Sprites/"
janela = window.Window(1920, 1080)
janela.set_title("Lost in Bits")
fundo = sprite.Sprite(path+"fundo.png")  
fundo.set_position(0, 0)


chaoY = 870  
personagem = sprite.Sprite(path+"josh.png")
personagem.set_position((janela.width - personagem.width)/2, chaoY - personagem.height)

teclado = keyboard.Keyboard()
velX = 300 
velY = 0
grav = 1200 
forcaPulo = -400  
onFloor = True

while True:
    deltaTime = janela.delta_time()
    
    if (teclado.key_pressed("a") or teclado.key_pressed("LEFT")) and personagem.x > 0:
        personagem.x -= velX * deltaTime
    if (teclado.key_pressed("d") or teclado.key_pressed("RIGHT")) and personagem.x < janela.width - personagem.width:
        personagem.x += velX * deltaTime

    if (teclado.key_pressed("w") or teclado.key_pressed("UP")) and onFloor:
        velY = forcaPulo
        onFloor = False
    
    if not onFloor:
        velY += grav * deltaTime
        personagem.y += velY * deltaTime
        if personagem.y + personagem.height >= chaoY:
            personagem.y = chaoY - personagem.height
            velY = 0
            onFloor = True
    
    if (teclado.key_pressed("s") or teclado.key_pressed("DOWN")) and onFloor:
        pass
    
    fundo.draw()
    personagem.draw()
    janela.draw_text("Fase 1: Plumber Game", janela.width - 350, 20, size=30, color=(0, 0, 0), font_name="Arial", bold=True)
    janela.update()
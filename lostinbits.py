from PPlay import window, sprite, keyboard

path = "Sprites/"
window = window.Window(1920, 1080)
window.set_title("Lost in Bits")
background = sprite.Sprite(path+"fundo.png")  
background.set_position(0, 0)


floorY = 870  
player = sprite.Sprite(path+"josh.png")
player.set_position((window.width - player.width)/2, floorY - player.height)

keyboard = keyboard.Keyboard()
speedX = 300 
speedY = 0
grav = 1200 
jumpForce = -400  
onFloor = True

while True:
    deltaTime = window.delta_time()
    
    if (keyboard.key_pressed("a") or keyboard.key_pressed("LEFT")) and player.x > 0:
        player.x -= speedX * deltaTime
    if (keyboard.key_pressed("d") or keyboard.key_pressed("RIGHT")) and player.x < window.width - player.width:
        player.x += speedX * deltaTime

    if (keyboard.key_pressed("w") or keyboard.key_pressed("UP")) and onFloor:
        speedY = jumpForce
        onFloor = False
    
    if not onFloor:
        speedY += grav * deltaTime
        player.y += speedY * deltaTime
        if player.y + player.height >= floorY:
            player.y = floorY - player.height
            speedY = 0
            onFloor = True
    
    if (keyboard.key_pressed("s") or keyboard.key_pressed("DOWN")) and onFloor:
        pass
    
    background.draw()
    player.draw()
    window.draw_text("Fase 1: Plumber Game", window.width - 350, 20, size=30, color=(0, 0, 0), font_name="Arial", bold=True)
    window.update()
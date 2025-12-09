from PPlay.sprite import Sprite
from entity import Entity

class Ghost(Entity):
    def __init__(self, game, x, y, image_path):
        # Inicializa a Entity com a janela e o nível do jogo
        # A classe pai (Entity) salva self.window e self.level
        super().__init__(game.window, game.level)
        
        # Cria o Sprite usando PPlay
        self.sprite = Sprite(image_path)
        self.sprite.x = x
        self.sprite.y = y
        
        # Ajuste de velocidade (pixels por segundo)
        self.speed = 100 
        self.vision_range = 400 
        
        # Inicializa velocidades
        self.velocity_x = 0
        self.velocity_y = 0
        
    def move(self, delta_time):
        self.chase_player(delta_time)
        self.apply_movement(delta_time)

    def chase_player(self, delta_time):
        # CORREÇÃO: Acessamos self.level diretamente, pois Entity já o armazena.
        # self.game não existe aqui, a menos que o salvassemos no __init__.
        player = self.level.player.sprite
        
        # Calcula a distância entre o fantasma e o jogador
        dx = player.x - self.sprite.x
        dy = player.y - self.sprite.y
        dist = (dx**2 + dy**2)**0.5
        
        # Se estiver dentro do raio de visão, persegue
        if dist < self.vision_range:
            if dist != 0:
                # Normaliza o vetor e multiplica pela velocidade
                self.velocity_x = (dx / dist) * self.speed
                self.velocity_y = (dy / dist) * self.speed
        else:
            self.velocity_x = 0
            self.velocity_y = 0

    def apply_movement(self, delta_time):
        # Aplica o movimento usando delta_time para suavidade
        self.sprite.x += self.velocity_x * delta_time
        self.sprite.y += self.velocity_y * delta_time

    def draw(self):
        self.sprite.draw()
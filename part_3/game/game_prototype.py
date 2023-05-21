import arcade
from characters import Enemy, Player
from items import Coin
from settings import Settings


class MyGame(arcade.Window):

    def __init__(self, settings: Settings):
        super().__init__(
            settings.get_value("SCREEN_WIDTH"),
            settings.get_value("SCREEN_HEIGHT"),
            settings.get_value('SCREEN_TITLE')
        )
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Создаем игрока
        player_sprite = arcade.Sprite(
            "resources/img/characters/femaleAdventurer_idle.png", scale=0.9
        )
        self.player = Player("Mira", player_sprite)

        # Создаем врага
        enemy_sprite = arcade.Sprite(
            "resources/img//enemies/robot_idle.png", scale=0.9
        )
        self.robot = Enemy('Robot', 500, 100, enemy_sprite)

        # Создание монет
        self.coin = Coin(300, 100)

    def on_draw(self):
        arcade.start_render()

        # Отрисовка спрайтов
        self.player.draw()
        self.robot.draw()
        self.coin.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.x -= settings.get_value("PLAYER_MOVEMENT_SPEED")
        elif key == arcade.key.RIGHT:
            self.player.x += settings.get_value("PLAYER_MOVEMENT_SPEED")
        elif key == arcade.key.UP:
            self.player.y += settings.get_value("PLAYER_JUMP_SPEED")
        elif key == arcade.key.DOWN:
            self.player.y -= settings.get_value("PLAYER_MOVEMENT_SPEED")


if __name__ == "__main__":
    settings = Settings(
        # Константы для размеров экрана
        SCREEN_WIDTH=1200,
        SCREEN_HEIGHT=800,
        SCREEN_TITLE="Mira and Gosha Prototype",
        # Константы для гравитации и скорости прыжка
        PLAYER_JUMP_SPEED=15,
        PLAYER_GRAVITY=0.5,
        PLAYER_MOVEMENT_SPEED=15,
        # Константы для размеров игрока
        PLAYER_WIDTH=64,
        PLAYER_HEIGHT=64
    )
    window = MyGame(settings)
    arcade.run()

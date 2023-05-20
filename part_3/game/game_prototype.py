import arcade

from characters import Enemy, Player


class MyGame(arcade.Window):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height, "My Game")
        self.player = Player("Player 1", 100, 100)
        self.enemy = Enemy("Enemy", 300, 100)

    def on_draw(self) -> None:
        arcade.start_render()
        self.player.draw()
        self.enemy.draw()

    def on_key_press(self, key: int, modifiers: int) -> None:
        if key == arcade.key.LEFT:
            self.player.x -= 10
        elif key == arcade.key.RIGHT:
            self.player.x += 10
        elif key == arcade.key.UP:
            self.player.y += 10
        elif key == arcade.key.DOWN:
            self.player.y -= 10


if __name__ == "__main__":
    window = MyGame(800, 600)
    arcade.run()

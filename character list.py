# Contains all playable characters as classes
# BaseCharacter demonstrates practice in class inheritance
class BaseCharacter:
    def __init__(self, is_alive=True, blocks=5):
        self.is_alive = is_alive
        self.block_count = blocks

    def get_is_alive(self):
        return self.is_alive

    def get_block_count(self):
        return self.block_count

    def block(self):
        if self.block_count <= 0:
            return "failed block"
        self.block_count -= 1
        return "block"


class Stock(BaseCharacter):
    def __init__(self, is_alive=True, bullets=0, blocks=5, name="Stock"):
        super().__init__(is_alive, blocks)
        self.bullet_count = bullets
        self.name = name

    def get_bullet_count(self):
        return self.bullet_count

    def get_name(self):
        return self.name

    def reload(self):
        self.bullet_count += 1
        return "reload"

    def shoot(self):
        if self.bullet_count <= 0:
            return "failed shoot"
        self.bullet_count -= 1
        return "shoot"

    def reflect(self):
        if self.bullet_count <= 0:
            return "failed reflect"
        self.bullet_count -= 1
        return "reflect"


class Samurai(BaseCharacter):
    def __init__(self, is_alive=True, unsheathed=False, blocks=5, name="Samurai"):
        super().__init__(is_alive, blocks)
        self.unsheathed = unsheathed
        self.name = name

    def get_unsheathed(self):
        return self.unsheathed

    def get_name(self):
        return self.name

    def unsheathe(self):
        self.unsheathed = True
        return "unsheathe"

    def slash(self):
        if not self.unsheathed:
            return "failed slash"
        return "slash"

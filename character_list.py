# Contains all playable characters as classes
# BaseCharacter demonstrates practice in class inheritance
class BaseCharacter:
    def __init__(self, is_alive=True, blocks=5, position=0, name="Bob"):
        self.is_alive = is_alive
        self.block_count = blocks
        self.position = position
        self.name = name

    def get_is_alive(self):
        return self.is_alive

    def get_name(self):
        return self.name

    def get_block_count(self):
        return self.block_count

    def get_position(self):
        return self.position

    def block(self):
        if self.block_count <= 0:
            return "failed block"
        self.block_count -= 1
        return "block"

    def die(self):
        self.is_alive = False
        return None


class RangedCharacter(BaseCharacter):
    def __init__(self, bullets=0):
        super().__init__()
        self.bullet_count = bullets

    def get_bullet_count(self):
        return self.bullet_count

    def reload(self):
        self.bullet_count += 1
        return "reload"

    def shoot(self):
        if self.bullet_count <= 0:
            return "failed shoot"
        self.bullet_count -= 1
        return "shoot"


class Stock(RangedCharacter):
    def __init__(self, position=0, name="Stock"):
        super().__init__()
        self.position = position
        self.name = name

    @staticmethod
    def get_moveset():
        print("1. Reload\n"
              "2. Shoot\n"
              "3. Block\n"
              "4. Reflect\n")

    def reflect(self):
        if self.bullet_count <= 0:
            return "failed reflect"
        self.bullet_count -= 1
        return "reflect"


class Samurai(BaseCharacter):
    def __init__(self, position=0, unsheathed=False, name="Samurai"):
        super().__init__()
        self.position = position
        self.unsheathed = unsheathed
        self.name = name

    def get_unsheathed(self):
        if self.unsheathed:
            return "Unsheathed"
        return "Sheathed"

    @staticmethod
    def get_moveset():
        print("1. Unsheathe Sword\n"
              "2. Slash\n"
              "3. Block\n")

    def unsheathe(self):
        self.unsheathed = True
        return "unsheathe"

    def slash(self):
        if not self.unsheathed:
            return "failed slash"
        return "slash"

    def shatter(self):
        self.unsheathed = False


class Sniper(RangedCharacter):
    def __init__(self, position=0, grapple=True, aiming=False, bullets=1, name="Sniper"):
        super().__init__()
        self.position = position
        self.grapple = grapple
        self.aiming = aiming
        self.bullet_count = bullets
        self.name = name

    def get_grapple_status(self):
        if self.grapple:
            return "Loaded"
        return "Unloaded"

    def get_aiming_status(self):
        if self.aiming:
            return "Yes"
        return "No"

    @staticmethod
    def get_moveset():
        print("1. Reload Rifle + Grapple Hook\n"
              "2. Aim\n"
              "3. Shoot\n"
              "4. Grapple Away\n"
              "5. Block\n")

    def reload(self):
        self.grapple = True
        self.bullet_count += 1
        return "reload"

    def aim(self):
        self.aiming = True
        return "aiming"

    def shoot(self):
        if self.get_aiming_status():
            if self.bullet_count <= 0:
                return "failed shoot (bullet count)"
            self.bullet_count -= 1
            return "shoot"
        return "failed shoot (not aiming)"

    def grapple_away(self):
        if self.grapple:
            if self.position <= 0:
                self.position -= 1
            else:
                self.position += 1
            return "grapple"
        return "failed grapple"

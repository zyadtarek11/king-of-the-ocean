import pgzrun
from nemo import Nemo
from shark import Shark
from octopus import Octopus
import random # important to spawn random fishes, not just a unified color

WIDTH = 768
HEIGHT = 600
TITLE = "King of the ocean"
# menu buttons dimesntions and positions
start_button = Rect(284, 200, 200, 50)
music_button = Rect(284, 300, 200, 50)
exit_button = Rect(284, 400, 200, 50)

game_state = "menu"
music_on = True
music.play("main_menu_theme")


def start_game():
    # start the game with inital positions for each sprite, so the player doesnot lose immediately if the shark or octopus spwaned at his location
    global player, enemy_shark, enemy_octopus, score

    score = 0
    player = Nemo(80, 100)
    enemy_shark = Shark(500, 150)
    enemy_octopus = Octopus(450, 400)
    spawn_fish()


def background_draw():
    # background will be tiles at the bottom and sea grass above it, with a background color for the ocean
    TILE_WIDTH = 128
    ground_tiles = [
        "ocean_scene/tile1",
        "ocean_scene/tile4",
        "ocean_scene/tile1",
        "ocean_scene/tile1",
        "ocean_scene/tile3",
        "ocean_scene/tile2",
    ]
    sea_grass = [
        "sea_grass/grass1",
        "sea_grass/grass3",
        "sea_grass/grass1",
        "sea_grass/grass2",
        "sea_grass/grass1",
        "sea_grass/grass3",
    ]
    screen.fill((0, 150, 200))

    for i, tile_name in enumerate(ground_tiles):
        tile = Actor(tile_name)
        tile.bottomleft = (i * TILE_WIDTH, HEIGHT)
        tile.draw()

    for i, grass_name in enumerate(sea_grass):
        grass = Actor(grass_name)
        grass.bottomleft = (i * TILE_WIDTH, HEIGHT - 128)
        grass.draw()


score = 0
food = None


def spawn_fish():
    # spawns fish in a random position, fishes are at random colors : red , blue , green , yellow , purple
    global food
    image = f"fish/fish{random.randint(1, 5)}"
    x = random.randint(50, 750)
    y = random.randint(50, 500)
    food = Actor(image, (x, y))


def update():
    global game_state, score

    if game_state == "play":
        # make the shark and player and octopus update their movement and animation on every frame
        player.move()
        player.animate()

        enemy_shark.patrol()
        enemy_shark.animate()

        enemy_octopus.patrol()
        enemy_octopus.animate()

        if player.colliderect(food):

            # each fish increases our score with 50
            score = score + 50
            # print(score)
            sounds.fish_bites.play()

            # choosed 300 to make the game easier and short , this number can be modified to 1000 to test the game more further
            if score >= 300:
                music.stop()
                sounds.game_win.play()
                game_state = "win"
            else:
                spawn_fish()
        # nemo losses if he touched the shark
        if player.colliderect(enemy_shark):
            music.stop()
            sounds.enemy_bites.play()
            sounds.game_lose.play()
            game_state = "lose"
        # nemo losses if he touched the octopus
        elif player.colliderect(enemy_octopus):
            music.stop()
            sounds.fish_poison.play()
            sounds.game_lose.play()
            game_state = "lose"

def draw():
    screen.clear()

    if game_state == "menu":
        # draw the menu buttons and background
        background = Actor("background")
        background.draw()
        screen.draw.text("Don't let sharks eat you :)", center=(384, 50), fontsize=40)
        screen.draw.filled_rect(start_button, "orange")
        screen.draw.text(
            "Start Game", center=start_button.center, color="black", fontsize=34
        )
        screen.draw.filled_rect(music_button, "blue")
        music_text = "Music: ON" if music_on else "Music: OFF"
        screen.draw.text(
            music_text, center=music_button.center, color="black", fontsize=34
        )
        screen.draw.filled_rect(exit_button, "red")
        screen.draw.text("Exit", center=exit_button.center, color="black", fontsize=34)

    elif game_state == "play":
        # draw the shark,octopus,nemo and the fish which spawns randomly one after another, also the tiles and sea grass and background
        background_draw()
        food.draw()
        enemy_shark.draw()
        enemy_octopus.draw()
        player.draw()
        screen.draw.text(
            f"Score:{score}", topright=(750, 20), fontsize=40, color="white"
        )

    elif game_state == "win":
        # player won -> redirect to the win screen
        screen.fill((0, 50, 20))
        screen.draw.text(
            "Click anywhere to return to the Menu",
            center=(384, 400),
            fontsize=30,
            color="yellow",
        )
        screen.draw.text(
            "Congratulations!", center=(384, 250), fontsize=80, color="white"
        )
        screen.draw.text(
            "You are now the king of the ocean!",
            center=(384, 320),
            fontsize=40,
            color="blue",
        )

    elif game_state == "lose":
        # player lost -> redirect to the loss screen
        screen.fill((50, 0, 0))
        screen.draw.text(
            "Click anywhere to return to Menu",
            center=(384, 400),
            fontsize=30,
            color="yellow",
        )
        screen.draw.text("GAME OVER!", center=(384, 300 - 50), fontsize=80, color="red")
        screen.draw.text(
            "You became fish food.", center=(384, 320), fontsize=40, color="white"
        )

# events -> when the player click any button on the menu
def on_mouse_down(pos):
    global game_state, music_on

    if game_state == "menu":
        if start_button.collidepoint(pos):
            start_game()
            game_state = "play"

            if music_on:
                music.stop()
                music.play("main_game_theme")

        elif music_button.collidepoint(pos):
            music_on = not music_on

            if music_on:
                music.play("main_menu_theme")
            else:
                music.stop()

        elif exit_button.collidepoint(pos):
            exit()

    elif game_state == "lose" or game_state == "win" :
        game_state = "menu"
        if music_on:
            music.play("main_menu_theme")


# to make it easier to run the game "just hit the run button"
pgzrun.go()

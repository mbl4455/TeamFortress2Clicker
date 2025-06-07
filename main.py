import pygame
import random
import sys
import pygame_gui
import colors
import assets
import sounds

pygame.init()
pygame.mixer.init()
screensizex = 800
screensizey = 600

screen = pygame.display.set_mode((screensizex, screensizey))
pygame.display.set_caption("Team Fortress 2 Clicker")
pygame.display.set_icon(assets.gameicon_image)

enemy_width = 75
enemy_height = 100

spy_image = pygame.transform.scale(assets.spy_image, (enemy_width, enemy_height))
pyro_image = pygame.transform.scale(assets.pyro_image, (enemy_width, enemy_height))
heavy_image = pygame.transform.scale(assets.heavy_image, (enemy_width, enemy_height))
sniper_image = pygame.transform.scale(assets.sniper_image, (enemy_width, enemy_height))
soldier_image = pygame.transform.scale(assets.soldier_image, (enemy_width, enemy_height))
demoman_image = pygame.transform.scale(assets.demoman_image, (enemy_width, enemy_height))
main_menu_bg = pygame.transform.scale(assets.main_menu_bg, (screensizex, screensizey))
engineer_image = pygame.transform.scale(assets.engineer_image, (enemy_width, enemy_height))
medic_image = pygame.transform.scale(assets.medic_image, (enemy_width, enemy_height))
scout_image = pygame.transform.scale(assets.scout_image, (enemy_width, enemy_height))
scope_image = pygame.transform.scale(assets.scope_image, (20,20))

logo = pygame.transform.scale(assets.original_logo,(475, 100))

enemy_sprites = [
    {"name": "Spy", "image": spy_image},
    {"name": "Pyro", "image": pyro_image},
    {"name": "Heavy", "image": heavy_image},
    {"name": "Sniper", "image": sniper_image},
    {"name": "Scout", "image": scout_image},
    {"name": "Engineer", "image": engineer_image},
    {"name": "Demoman", "image": demoman_image},
    {"name": "Soldier", "image": soldier_image},
    {"name": "Medic", "image": medic_image}
]

score = 0
last_voiceline_score = 0
show_crit = False
is_scoping = False
game_duration = 30000
crit_timer = 0
#team = NotImplemented --não tenho tenho de implementar, pois estou em semana de prova :(
click_cooldown = 250
last_click_time = 0
enemy_pos = [0, 0]
current_enemy = None

gametime = pygame.time.Clock()

def enemies_positions():
    global enemy_image, current_enemy, enemy_pos
    enemy = random.choice(enemy_sprites)
    enemy_image = enemy["image"]
    current_enemy = enemy["name"]
    enemy_pos[0] = random.randint(0, screensizex - enemy_width)
    enemy_pos[1] = random.randint(0, screensizey - enemy_height)

def draw_enemies():
    screen.blit(enemy_image, (enemy_pos[0], enemy_pos[1]))

def show_score():
    font = pygame.font.Font("fonts/tf2build.ttf", 23)
    text = font.render("Score: " + str(score), True, (colors.tf2textbase))
    screen.blit(text, (10, 10))

def show_timer(elapsed):
    remaining = max(0, (game_duration - elapsed) // 1000)
    font = pygame.font.Font("fonts/tf2build.ttf", 23)
    timer_text = font.render(f"Time Left: {remaining}s", True, colors.tf2textbase)
    screen.blit(timer_text, (10, 30))

def start_game():
    global score, show_crit, crit_timer, last_click_time, enemy_pos, last_voiceline_score, is_scoping
    sounds.mainmenusoundtrack.play(-1)
    score = 0
    show_crit = False
    crit_timer = 0
    last_click_time = 0
    last_voiceline_score = 0
    start_time = pygame.time.get_ticks()

    enemies_positions()
    ui_manager = pygame_gui.UIManager((screensizex, screensizey), "pygui_theme.json")

    play_again_button = None

    running = True
    while running:
        time_delta = gametime.tick(60) / 1000.0
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time
        screen.fill(colors.tf2wallbase)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    sounds.scope.play()
                    is_scoping = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    is_scoping = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], enemy_width, enemy_height)
                    if current_time - last_click_time >= click_cooldown and elapsed_time < game_duration:
                        if enemy_rect.collidepoint(mouse_x, mouse_y):
                            if is_scoping:
                                score += 2
                                sounds.shotcrit.play()
                                sounds.critical_hit_sound.play()
                                show_crit = True
                                crit_timer = current_time
                                crit_position = enemy_pos.copy()
                            else:
                                if random.random() < 0.2:
                                    score += 2
                                    sounds.shotcrit.play()
                                    sounds.critical_hit_sound.play()
                                    show_crit = True
                                    crit_timer = current_time
                                    crit_position = enemy_pos.copy()
                                else:
                                    score += 1
                                    sounds.shot.play()
                        sounds.reload.play()
                        if score % 10 == 0 and score != 0 and score != last_voiceline_score:
                            random.choice(sounds.voicelines).play()
                            last_voiceline_score = score
                        last_click_time = current_time
                        enemies_positions()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if play_again_button is not None and event.ui_element == play_again_button:
                    sounds.buttonpress.play()
                    score = 0
                    show_crit = False
                    crit_timer = 0
                    last_click_time = 0
                    last_voiceline_score = 0
                    start_time = pygame.time.get_ticks()
                    enemies_positions()
                    play_again_button.kill()
                    play_again_button = None

            ui_manager.process_events(event)

        if elapsed_time >= game_duration:
            screen.fill((30, 30, 30))
            screen.blit(logo, (160,175))
            font = pygame.font.Font("fonts/tf2build.ttf", 48)
            final_score_text = font.render(f"Final Score: {score}", True, colors.tf2textbase)
            screen.blit(final_score_text, (screensizex // 2 - final_score_text.get_width() // 2, screensizey // 2 - 20))

            if play_again_button is None:
                play_again_button = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect((screensizex // 2 - 75, screensizey // 2 + 30), (150, 50)),
                    text='PLAY AGAIN',
                    manager=ui_manager,
                )
            else:
                play_again_button.show()
        else:
            draw_enemies()
            show_score()
            show_timer(elapsed_time)
            pygame.mouse.set_visible(not is_scoping)
            if is_scoping:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                scope_rect = scope_image.get_rect(center=(mouse_x, mouse_y))
                screen.blit(scope_image, scope_rect)

            if show_crit:
                elapsed = current_time - crit_timer
                if elapsed < 1000:
                    fade_duration = 1000
                    alpha = max(0, 255 - int((elapsed / fade_duration) * 255))
                    offset_y = int((elapsed / fade_duration) * 30)

                    font = pygame.font.Font("fonts/tf2build.ttf", 36)
                    crit_text = font.render("CRITICAL HIT!!!", True, colors.green)
                    critdmg_text = font.render("-200", True, colors.red)
                    critdmg_surface = pygame.Surface(crit_text.get_size(), pygame.SRCALPHA)
                    crit_surface = pygame.Surface(crit_text.get_size(), pygame.SRCALPHA)
                    critdmg_surface.blit(critdmg_text, (0, 0))
                    crit_surface.blit(crit_text, (0, 0))
                    crit_surface.set_alpha(alpha)
                    critdmg_surface.set_alpha(alpha)

                    text_x = crit_position[0] + enemy_width // 2 - crit_text.get_width() // 2
                    text_y = crit_position[1] - 30 - offset_y
                    text_y2 = crit_position[1] - offset_y
                    screen.blit(crit_surface, (text_x, text_y))
                    screen.blit(critdmg_surface, (text_x, text_y2))
                else:
                    show_crit = False

            if play_again_button is not None:
                play_again_button.hide()

        ui_manager.update(time_delta)
        ui_manager.draw_ui(screen)
        pygame.display.update()

def main_menu():
    ui_manager = pygame_gui.UIManager((screensizex, screensizey), "pygui_theme.json")

    start_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((screensizex // 2 - 100, screensizey // 2 - 25), (200, 50)),
        text='Start Game',
        manager=ui_manager
    )

    clock = pygame.time.Clock()
    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    sounds.buttonpress.play()
                    running = False

            ui_manager.process_events(event)

        screen.blit(main_menu_bg, (0, 0))

        screen.blit(logo, (160,175))

        ui_manager.update(time_delta)
        ui_manager.draw_ui(screen)
        pygame.display.update()

if __name__ == "__main__":
    main_menu()
    start_game()
    pygame.quit()
import pygame
import sys
import random

# 初始化pygame
pygame.init()

# 设置游戏窗口大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("射击小游戏")

# 设置颜色
white = (255, 255, 255)
red = (255, 0, 0)

# 玩家
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 10
player = pygame.Rect(player_x, player_y, player_width, player_height)

# 子弹
bullet_width = 5
bullet_height = 5
bullet_speed = 35
bullets = []

# 敌人
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemies = []

def draw_player():
    pygame.draw.rect(screen, white, player)

def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, white, bullet)

def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, red, enemy)

def move_bullets():
    for bullet in bullets:
        bullet.y -= bullet_speed

def move_enemies():
    for enemy in enemies:
        enemy.y += enemy_speed

def create_enemy():
    enemy_x = random.randint(0, screen_width - enemy_width)
    enemy_y = random.randint(-screen_height, 0)
    enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    enemies.append(enemy)

def check_collision():
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)

def main():
    clock = pygame.time.Clock()
    enemy_timer = 0

    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x < screen_width - player_width:
            player.x += player_speed
        if keys[pygame.K_SPACE]:
            bullet = pygame.Rect(player.x + player_width // 2 - bullet_width // 2, player.y, bullet_width, bullet_height)
            bullets.append(bullet)

        enemy_timer += 1
        if enemy_timer >= 50:
            create_enemy()
            enemy_timer = 0

        move_bullets()
        move_enemies()

        check_collision()

        draw_player()
        draw_bullets()
        draw_enemies()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
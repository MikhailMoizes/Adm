import time

import pygame
import sqlite3

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Настройки шрифта
font = pygame.font.Font(None, 36)

pygame.display.set_caption("Регистрация")
player_name = ''

# Класс для игрока
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


# Класс для работы с базой данных
class Database:
    def __init__(self):
        self.connection = sqlite3.connect('game_scores.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY,
                name TEXT,
                score INTEGER
            )
        ''')
        self.connection.commit()

    def add_score(self, name, score):
        self.cursor.execute('INSERT INTO scores (name, score) VALUES (?, ?)', (name, score))
        self.connection.commit()

    def get_top_scores(self):
        self.cursor.execute('SELECT name, score FROM scores ORDER BY score DESC LIMIT 5')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


# Функция для отображения текста на экране
def draw_text(surface, text, pos):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, 'black')
    surface.blit(text_surface, pos)


def registration():
    global player_name
    input_active = True

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if input_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Нажатие Enter
                        input_active = False  # Завершение регистрации
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]  # Удаление последнего символа
                    else:
                        player_name += event.unicode  # Добавление символа

        screen.fill(WHITE)
        draw_text(screen,'Введите имя пользователя:', (20, 50))
        draw_text(screen,player_name, (20, 100))
        draw_text(screen,'Нажмите Enter для завершения', (20, 150))
        draw_text(screen, f'Для управления игрой клавиши управления курсора', (20, 200))
        pygame.display.flip()

# старт игры
def game():
    def draw_multiline_text(surface, text_lines, position):
        y_offset = 0
        for line in text_lines:
            text_surface = font.render(line, True, BLACK)
            surface.blit(text_surface, (position[0], position[1] + y_offset))
            y_offset += text_surface.get_height()
    # Запрос имени игрока
    player = Player(player_name)
    # баллы будут зависят от времени потраченного на игру
    start_time = time.perf_counter()
    db = Database()
    pygame.display.set_caption("Приветствую игрока " + player.name)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-5, 0)
            player.score += 1
        if keys[pygame.K_RIGHT]:
            player.move(5, 0)
            player.score += 1
        if keys[pygame.K_UP]:
            player.move(0, -5)
            player.score += 1
        if keys[pygame.K_DOWN]:
            player.move(0, 5)
            player.score += 1

        screen.fill(WHITE)

        # Отображение игрока
        pygame.draw.rect(screen,GREEN , player.rect)

        # Отображение очков
        draw_text(screen, f"Очки: {player.score:.2f} время: {time.perf_counter() - start_time:.2f}",
                  (10, 10))

        # Проверка условий выигрыша/проигрыша (например, выход за границы)
        if player.rect.x < 0 or player.rect.x > WIDTH or player.rect.y < 0 or player.rect.y > HEIGHT:
            draw_text(screen, "Игра закончилась!", (WIDTH // 2 - 50, HEIGHT // 2))
            runtime = time.perf_counter() - start_time
            db.add_score(player.name, player.score/runtime)
            # Вывод топ-5 игроков
            top_scores = db.get_top_scores()
            text = ["Топ-5 игроков:"]
            for i, (name, score) in enumerate(top_scores, 1):
                text.append(f"{i}. {name} - {score:.2f}")

            draw_multiline_text(screen, text, (50, 50))
            running = False

        pygame.display.flip()
        clock.tick(FPS)

    db.close()
    time.sleep(5)
    pygame.quit()

if __name__ == "__main__":
    registration()  # Переход к окну регистрации
    game()  # Переход к игровому окну



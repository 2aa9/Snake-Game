
### `snake.py`
```python
import pygame, random, sys

pygame.init()
WIDTH, HEIGHT = 600, 400
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

def draw_snake(snake):
    for x, y in snake:
        pygame.draw.rect(screen, (0, 255, 0), (x, y, CELL, CELL))

def main():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (CELL, 0)
    food = (random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL))
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, CELL):
                    direction = (0, -CELL)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL):
                    direction = (0, CELL)
                elif event.key == pygame.K_LEFT and direction != (CELL, 0):
                    direction = (-CELL, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                    direction = (CELL, 0)

        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head)

        if head == food:
            food = (random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL))
            score += 1
        else:
            snake.pop()

        if head[0] < 0 or head[1] < 0 or head[0] >= WIDTH or head[1] >= HEIGHT or head in snake[1:]:
            print(f"Game Over! Final Score: {score}")
            pygame.quit(); sys.exit()

        screen.fill((0, 0, 0))
        draw_snake(snake)
        pygame.draw.rect(screen, (255, 0, 0), (*food, CELL, CELL))
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()

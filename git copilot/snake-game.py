import pygame
import random
import sys
from enum import Enum
from collections import deque

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

# Game speed
INITIAL_SPEED = 8
MAX_SPEED = 15

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class Snake:
    def __init__(self):
        """Initialize snake at center of screen."""
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.body = deque([(start_x, start_y), 
                          (start_x - 1, start_y), 
                          (start_x - 2, start_y)])
        self.direction = Direction.RIGHT
        self.grow_pending = False

    def move(self):
        """Move snake in current direction."""
        head_x, head_y = self.body[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)

        self.body.appendleft(new_head)
        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False

    def check_collision_with_self(self):
        """Check if snake collided with itself."""
        head = self.body[0]
        return head in list(self.body)[1:]

    def check_collision_with_walls(self):
        """Check if snake collided with walls."""
        head_x, head_y = self.body[0]
        return head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT

    def grow(self):
        """Mark snake to grow on next move."""
        self.grow_pending = True

    def set_direction(self, direction):
        """Set direction, preventing 180-degree turns."""
        opposite_directions = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT
        }
        if direction != opposite_directions[self.direction]:
            self.direction = direction

    def get_body(self):
        """Return snake body segments."""
        return list(self.body)


class Food:
    def __init__(self, snake_body):
        """Initialize food at random position not occupied by snake."""
        self.position = self.spawn_food(snake_body)

    def spawn_food(self, snake_body):
        """Spawn food at random location avoiding snake."""
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in snake_body:
                return (x, y)

    def check_collision(self, head):
        """Check if snake head collided with food."""
        return head == self.position

    def respawn(self, snake_body):
        """Respawn food at new location."""
        self.position = self.spawn_food(snake_body)


class SnakeGame:
    def __init__(self):
        """Initialize the game."""
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game - Professional Edition")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 72)
        self.font_medium = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 32)
        self.font_tiny = pygame.font.Font(None, 24)

        self.reset_game()

    def reset_game(self):
        """Reset game state."""
        self.snake = Snake()
        self.food = Food(self.snake.get_body())
        self.score = 0
        self.speed = INITIAL_SPEED
        self.game_over = False
        self.paused = False
        self.next_direction = self.snake.direction

    def handle_input(self):
        """Handle user input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.next_direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.next_direction = Direction.DOWN
                elif event.key == pygame.K_LEFT:
                    self.next_direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.next_direction = Direction.RIGHT
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r and self.game_over:
                    self.reset_game()
                elif event.key == pygame.K_ESCAPE:
                    return False

        return True

    def update(self):
        """Update game state."""
        if self.game_over or self.paused:
            return

        self.snake.set_direction(self.next_direction)
        self.snake.move()

        # Check food collision
        if self.food.check_collision(self.snake.body[0]):
            self.snake.grow()
            self.food.respawn(self.snake.get_body())
            self.score += 10
            # Gradually increase speed
            if self.speed < MAX_SPEED:
                self.speed += 0.1

        # Check collisions
        if self.snake.check_collision_with_self() or self.snake.check_collision_with_walls():
            self.game_over = True

    def draw(self):
        """Draw game elements."""
        self.screen.fill(BLACK)
        
        # Draw grid (optional, for visual aid)
        pygame.draw.rect(self.screen, DARK_GRAY, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT), 2)

        # Draw snake
        for i, (x, y) in enumerate(self.snake.get_body()):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            if i == 0:  # Head
                pygame.draw.rect(self.screen, GREEN, rect)
                pygame.draw.circle(self.screen, WHITE, rect.center, 4)
            else:  # Body
                pygame.draw.rect(self.screen, DARK_GREEN, rect)
            pygame.draw.rect(self.screen, BLACK, rect, 1)

        # Draw food
        food_rect = pygame.Rect(self.food.position[0] * GRID_SIZE, 
                               self.food.position[1] * GRID_SIZE, 
                               GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(self.screen, RED, food_rect)
        pygame.draw.circle(self.screen, YELLOW, food_rect.center, GRID_SIZE // 3)

        # Draw score
        score_text = self.font_small.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        # Draw speed
        speed_text = self.font_tiny.render(f"Speed: {self.speed:.1f}x", True, GRAY)
        self.screen.blit(speed_text, (10, 45))

        # Draw controls hint
        controls_text = self.font_tiny.render("Arrow Keys: Move | SPACE: Pause | R: Restart | ESC: Quit", True, GRAY)
        self.screen.blit(controls_text, (10, WINDOW_HEIGHT - 30))

        # Draw paused state
        if self.paused:
            pause_text = self.font_medium.render("PAUSED", True, YELLOW)
            text_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            pygame.draw.rect(self.screen, DARK_GRAY, text_rect.inflate(20, 20))
            self.screen.blit(pause_text, text_rect)

        # Draw game over state
        if self.game_over:
            # Semi-transparent overlay
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(200)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))

            game_over_text = self.font_large.render("GAME OVER", True, RED)
            game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 60))
            self.screen.blit(game_over_text, game_over_rect)

            final_score_text = self.font_medium.render(f"Final Score: {self.score}", True, WHITE)
            score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
            self.screen.blit(final_score_text, score_rect)

            restart_text = self.font_small.render("Press R to Restart or ESC to Quit", True, YELLOW)
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 80))
            self.screen.blit(restart_text, restart_rect)

        pygame.display.flip()

    def run(self):
        """Main game loop."""
        running = True
        while running:
            running = self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(self.speed)

        pygame.quit()
        sys.exit()


def main():
    """Entry point for the game."""
    game = SnakeGame()
    game.run()


if __name__ == "__main__":
    main()

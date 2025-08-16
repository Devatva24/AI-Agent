import pygame
import time

# Constants
WIDTH, HEIGHT = 600, 500
WHITE, BLACK, RED, BROWN = (255, 255, 255), (0, 0, 0), (255, 0, 0), (139, 69, 19)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monks and Demons Game")
font = pygame.font.Font(None, 36)

class MonksAndDemons:
    def __init__(self):
        self.num_monks = 3
        self.num_demons = 3
        self.boat = []  # Track monks/demons on the boat
        self.left_bank = {"monks": 3, "demons": 3}
        self.right_bank = {"monks": 0, "demons": 0}
        self.boat_side = "left"
        self.paused = False
        self.running = False
        self.solution_moves = []
        self.solve()
        self.reset_game()

    def reset_game(self):
        self.left_bank = {"monks": 3, "demons": 3}
        self.right_bank = {"monks": 0, "demons": 0}
        self.boat = []
        self.boat_side = "left"
        self.running = False
        self.paused = False
        self.draw_scene()
        pygame.display.flip()

    def solve(self):
        self.solution_moves = [
            ("right", ["demon", "demon"]),
            ("left", ["demon"]),
            ("right", ["demon", "monk"]),
            ("left", ["monk"]),
            ("right", ["monk", "monk"]),
            ("left", ["demon"]),
            ("right", ["demon", "demon"]),
            ("left", ["monk"]),
            ("right", ["monk", "monk"])
        ]

    def draw_scene(self):
        screen.fill(WHITE)

        # Draw river
        pygame.draw.rect(screen, BROWN, (200, 200, 200, 100))

        # Draw boat
        boat_x = 150 if self.boat_side == "left" else 350
        pygame.draw.rect(screen, BLACK, (boat_x, 250, 100, 30))

        # Draw monks and demons on banks
        for i in range(self.left_bank["monks"]):
            pygame.draw.circle(screen, RED, (50 + i * 30, 250), 10)
        for i in range(self.left_bank["demons"]):
            pygame.draw.circle(screen, BLACK, (50 + i * 30, 280), 10)

        for i in range(self.right_bank["monks"]):
            pygame.draw.circle(screen, RED, (450 + i * 30, 250), 10)
        for i in range(self.right_bank["demons"]):
            pygame.draw.circle(screen, BLACK, (450 + i * 30, 280), 10)

        # Draw monks and demons on the boat
        for i, passenger in enumerate(self.boat):
            color = RED if passenger == "monk" else BLACK
            pygame.draw.circle(screen, color, (boat_x + 20 + i * 30, 265), 10)

        # Draw UI buttons
        pygame.draw.rect(screen, BLACK, (50, 420, 100, 50))  # Start Button
        pygame.draw.rect(screen, RED, (200, 420, 100, 50))  # Reset Button
        pygame.draw.rect(screen, BLACK, (350, 420, 100, 50))  # Pause Button

        screen.blit(font.render("Start", True, WHITE), (75, 435))
        screen.blit(font.render("Reset", True, WHITE), (225, 435))
        screen.blit(font.render("Pause", True, WHITE), (375, 435))

        # Display which is monk and which is demon
        screen.blit(font.render("Red = Monk", True, RED), (50, 470))
        screen.blit(font.render("Black = Demon", True, BLACK), (200, 470))

    def execute_solution(self):
        for move in self.solution_moves:
            if not self.running or self.paused:
                break
            self.boat = move[1]
            self.boat_side = move[0]
            self.update_banks()
            self.draw_scene()
            pygame.display.flip()
            pygame.time.wait(1000)  # Wait for 1 second before the next move (smooth transition)
        self.running = False

    def update_banks(self):
        if self.boat_side == "right":
            for p in self.boat:
                self.left_bank[p + "s"] -= 1
                self.right_bank[p + "s"] += 1
        else:
            for p in self.boat:
                self.left_bank[p + "s"] += 1
                self.right_bank[p + "s"] -= 1
        self.boat = []

    def handle_mouse_click(self, pos):
        x, y = pos
        if 50 <= x <= 150 and 420 <= y <= 470:  # Start Button
            if not self.running:
                self.running = True
                self.paused = False
        elif 200 <= x <= 300 and 420 <= y <= 470:  # Reset Button
            self.running = False
            self.reset_game()
        elif 350 <= x <= 450 and 420 <= y <= 470:  # Pause Button
            self.paused = not self.paused  # Toggle pause

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_click(pygame.mouse.get_pos())

            self.draw_scene()
            pygame.display.flip()

            if self.running and not self.paused:
                self.execute_solution()

        pygame.quit()

# Start the Game
game = MonksAndDemons()
game.run()

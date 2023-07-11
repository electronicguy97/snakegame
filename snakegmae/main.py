import pygame
from model import Snake, Food, Game
from view import Renderer
from controller import InputHandler

def main():
    # Initialize pygame
    pygame.init()

    # Create game objects
    snake = Snake()
    food = Food()
    game = Game(snake, food)
    renderer = Renderer()
    input_handler = InputHandler()

    # Set up the game window
    renderer.setup_window()

    # Start the game loop
    while not game.is_game_over():
        # Handle user input
        input_handler.handle_input(snake)

        # Update game state
        game.update()

        # Render the game
        renderer.render(game)

    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()
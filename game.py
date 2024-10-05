from time import sleep
from draw import draw_ball, draw_paddle, draw_wall, draw_ceiling, draw_score
from settings import INITIAL_BALL_X, INITIAL_BALL_Y, INITIAL_X_SPEED, INITIAL_Y_SPEED, INITIAL_PADDLE_X, PADDLE_Y, WIDTH, HEIGHT
from collisions import detect_block_collisions, detect_paddle_collision, detect_wall_collision

def set_initial_values():
    return {
        "x_ball": INITIAL_BALL_X,
        "y_ball": INITIAL_BALL_Y,
        "x_speed": INITIAL_X_SPEED,
        "y_speed": INITIAL_Y_SPEED,
        "x_paddle": INITIAL_PADDLE_X,
        "score": 0
    }

def run_game(root, screen):
    game_values = set_initial_values()

    while True:
        screen.delete("all")  # Clear previous frame

        # Draw objects
        draw_ball(screen, game_values['x_ball'], game_values['y_ball'])
        draw_paddle(screen, game_values['x_paddle'], PADDLE_Y)
        draw_wall(screen, 0, 0)
        draw_wall(screen, WIDTH - 20, 0)
        draw_ceiling(screen, 0, 0)
        draw_score(screen, game_values['score'])

        # Update positions
        game_values['x_ball'] += game_values['x_speed']
        game_values['y_ball'] += game_values['y_speed']

        # Handle collisions (with paddle, walls, etc.)
        if detect_paddle_collision(game_values['x_ball'], game_values['y_ball'], game_values['x_paddle'], PADDLE_Y, 200):
            game_values['y_speed'] = -game_values['y_speed']

        if game_values['y_ball'] > HEIGHT:
            # End game logic here
            break

        screen.update()
        sleep(0.03)  # Frame delay

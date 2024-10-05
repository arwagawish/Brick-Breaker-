from settings import BALL_DIAMETER, PADDLE_WIDTH, PADDLE_HEIGHT, WALL_WIDTH, WALL_HEIGHT

def draw_ball(screen, x_ball, y_ball, ball_color="red"):
    return screen.create_oval(x_ball, y_ball, x_ball + BALL_DIAMETER, y_ball + BALL_DIAMETER, fill=ball_color)

def draw_paddle(screen, x_paddle, y_paddle, paddle_color="red"):
    return screen.create_rectangle(x_paddle, y_paddle, x_paddle + PADDLE_WIDTH, y_paddle + PADDLE_HEIGHT, fill=paddle_color)

def draw_wall(screen, x_wall, y_wall, wall_color="red"):
    return screen.create_rectangle(x_wall, y_wall, x_wall + WALL_WIDTH, y_wall + WALL_HEIGHT, fill=wall_color)

def draw_ceiling(screen, x_ceiling, y_ceiling, ceiling_color="red"):
    return screen.create_rectangle(x_ceiling, y_ceiling, x_ceiling + 980, y_ceiling + 20, fill=ceiling_color)

def draw_score(screen, score):
    return screen.create_text(100, 50, text="Score:" + str(score), font="Arial 20", fill="white")

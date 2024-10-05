def detect_block_collisions(x_ball, y_ball, x_blocks, y_blocks, x_size_blocks, y_size_blocks):
    limit = 15
    center_ball = [x_ball + 10, y_ball + 10]  # Detect center of ball

    for i in range(len(x_blocks)):
        # Detect collision with the block (top, bottom, left, right)
        if y_blocks[i] < center_ball[1] < y_blocks[i] + limit and x_blocks[i] < center_ball[0] < x_blocks[i] + x_size_blocks[i]:
            return "Top"
        elif (y_blocks[i] + y_size_blocks[i]) - limit < center_ball[1] < (y_blocks[i] + y_size_blocks[i]) and x_blocks[i] < center_ball[0] < x_blocks[i] + x_size_blocks[i]:
            return "Bottom"
        elif x_blocks[i] < center_ball[0] < x_blocks[i] + limit and y_blocks[i] < center_ball[1] < y_blocks[i] + y_size_blocks[i]:
            return "Left"
        elif (x_blocks[i] + x_size_blocks[i]) - limit < center_ball[0] < (x_blocks[i] + x_size_blocks[i]) and y_blocks[i] < center_ball[1] < y_blocks[i] + y_size_blocks[i]:
            return "Right"

    return "noCollision"

def detect_paddle_collision(x_ball, y_ball, x_paddle, y_paddle, paddle_width):
    center_ball = [x_ball + 10, y_ball + 10]
    if center_ball[0] >= x_paddle and center_ball[0] <= x_paddle + paddle_width and center_ball[1] >= y_paddle and center_ball[1] <= y_paddle + 50:
        return True
    return False

def detect_wall_collision(x_ball, y_ball, x_wall, wall_width):
    center_ball = [x_ball + 10, y_ball + 10]
    if center_ball[0] <= x_wall + wall_width:
        return True
    return False

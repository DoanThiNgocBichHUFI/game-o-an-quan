import pygame
import sys
import math

# Khởi tạo Pygame
pygame.init()

# Kích thước của mỗi ô vuông
square_size = 50

# Số ô theo chiều rộng và chiều cao
width, height = 7, 2
screen_width = width * square_size
screen_height = height * square_size

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)

# Biến đại diện cho ô dân
citizen_squares = [f"Citizen {i}" for i in range(1, 11)]

# Biến đại diện cho ô quan
official1 = "Quan 1"
official2 = "Quan 2"

# Tạo màn hình
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("O An Quan Board")

# Vẽ bàn cờ
def draw_board():
    screen.fill(white)
    for row in range(height):
        for col in range(width):
            pygame.draw.rect(screen, black, (col * square_size, row * square_size, square_size, square_size), 1)
            

# Hàm vẽ các phần tử trên bàn cờ
def draw_board_elements():
    # Vẽ ô hình bán nguyệt ở cạnh trái
    draw_semi_circle(-50, 0, square_size * 2, (1.5 * math.pi, 0.5 * math.pi))

    # Vẽ ô hình bán nguyệt ở cạnh phải (không chồng lên ô của bàn cờ)
    draw_semi_circle(screen_width - square_size , 0, square_size * 2, (0.5 * math.pi, 1.5 * math.pi))

# Hàm vẽ ô hình bán nguyệt
def draw_semi_circle(x, y, radius, direction):
    pygame.draw.arc(screen, black, (x, y, radius, radius), direction[0], direction[1], 1)


# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_board()
    draw_board_elements()

    pygame.display.flip()

# Đóng cửa sổ khi kết thúc
pygame.quit()
sys.exit()

#vẽ hình bàn cờ . khởi tạo biến quan, dân.

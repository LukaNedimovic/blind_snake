import random
from core.strategy.move import Move


class Board:
    def __init__(self, width: int = 0, height: int = 0, snake_x: int = None, snake_y: int = None, apple_x: int = None, apple_y: int = None):
        self.width = width
        self.height = height
        
        self.snake_x = snake_x
        self.snake_y = snake_y

        self.apple_x = apple_x 
        self.apple_y = apple_y
    
    def generate_random_board(self):
        snake_point = self.random_point()
        self.set_snake_at(snake_point[0], snake_point[1])
        
        apple_point = self.random_unoccupied_point()
        self.set_apple_at(apple_point[0], apple_point[1])
         
    def send_move(self, move: Move):
        # Update position
        match move:
            case Move.UP:
                self.snake_y -= 1
            case Move.DOWN:
                self.snake_y += 1
            case Move.LEFT:
                self.snake_x -= 1
            case Move.RIGHT:
                self.snake_x += 1

            case _:
                raise ValueError('Board.send_move() -> Invalid move.')
        
        # Torus effect
        self.snake_x %= self.width
        self.snake_y %= self.height
    
    def draw(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.snake_x == col and self.snake_y == row:
                    print('S', end='')
                elif self.apple_x == col and self.apple_y == row:
                    print('A', end='')
                else:
                    print('.', end='')
            
            print()
        
    def set_apple_at(self, apple_x: int, apple_y: int):
        self.apple_x = apple_x
        self.apple_y = apple_y
        
    def set_snake_at(self, snake_x: int, snake_y: int):
        self.snake_x = snake_x
        self.snake_y = snake_y
        
    def get_apple(self):
        return (self.apple_x, self.apple_y)
    
    def get_snake(self):
        return (self.snake_x, self.snake_y)
    
    def random_x(self):
        return random.randint(0, self.width - 1)

    def random_y(self):
        return random.randint(0, self.height - 1)
    
    def random_point(self):
        return (self.random_x(), self.random_y())
    
    def is_apple_at(self, point: tuple):
        point_x, point_y = point
        
        return (
            self.apple_x is not None and 
            self.apple_y is not None and 
            self.apple_x == point_x and
            self.apple_y == point_y
        )
        
    def is_snake_at(self, point: tuple):
        point_x, point_y = point
        
        return (
            self.snake_x is not None and 
            self.snake_y is not None and 
            self.snake_x == point_x and
            self.snake_y == point_y
        )
    
    def random_unoccupied_point(self):
        random_point = self.random_point()
        
        while self.is_snake_at(random_point) or self.is_apple_at(random_point):
            random_point = self.random_point()
            
        return random_point
   
    def point_within_borders(self, x: int, y: int):
        return (
            0 <= x and 
            x < self.width and 
            0 <= y and 
            y < self.height
        )
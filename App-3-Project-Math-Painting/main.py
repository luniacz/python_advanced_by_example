from canvas import Canvas
from shapes import Rectangle, Square

canvas_width = int(input('Enter canvas width: '))
canvas_height = int(input('Enter canvas height: '))

colors = {'white': (255, 255, 255), 'black': (0, 0, 0)}
canvas_color = input('Enter canvas color (white or black): ')

# create a canvas with the user data
canvas = Canvas(canvas_height, canvas_width, colors[canvas_color])

while True :
    shape_type = input('What do you like to draw (choose rectangle, square or quit)?')

    if shape_type.lower() == 'rectangle':
        rec_x = int(input('Enter x of rectangle: '))
        rec_y = int(input('Enter y of rectangle: '))
        rec_height = int(input('Enter height of rectangle: '))
        rec_width = int(input('Enter width of rectangle: '))
        red = int(input('How much red should the reatangle have? '))
        green = int(input('How much green? '))
        blue = int(input('How much blue? '))

        r1 = Rectangle(rec_x, rec_y, rec_height, rec_width, color=(red, green, blue))
        r1.draw(canvas)

    if shape_type.lower() == 'square':
        sqr_x = int(input('Enter x of rectangle: '))
        sqr_y = int(input('Enter y of rectangle: '))
        sqr_side = int(input('Enter the side length of the square: '))
        red = int(input('How much red should the reactangle have? '))
        green = int(input('How much green? '))
        blue = int(input('How much blue? '))
        s1 = Square(sqr_x, sqr_y, sqr_side, color=(red, green, blue))
        s1.draw(canvas)

    if shape_type == 'quit':
        break

canvas.make('canvas.png')

def calculate_area_rectangle(side, height):

    # Implement function for calculating rectangle

    return side * height


def calculate_square(side):

    return side * side



def main():

    # calculate area of square
    square_1 = calculate_square(4)
    print(f"Area of square 1: {square_1}")

    rectangle_1 = calculate_area_rectangle(2,4)
    print(f"Area of rectangle 1: {rectangle_1}")





if __name__ == '__main__':
    main()
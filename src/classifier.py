
def is_on_board(x, y, z, x_min, x_max, y_board, z_min, z_max):
    """
    Check if the point C(x, y, z) is on the board.

    Parameters:
    - x, y, z: Coordinates of the finger tip.
    - x_min, x_max: The x-coordinate bounds of the board.
    - y_board: The fixed y-coordinate of the board.
    - z_min, z_max: The z-coordinate bounds of the board.

    Returns:
    - True if the point is on the board, False otherwise.
    """
    if x_min <= x <= x_max and y == y_board and z_min <= z <= z_max:
        return True
    else:
        return False

# Example usage
# Board boundaries
x_min = 0
x_max = 10  # Example x-range
y_board = 5  # The y-coordinate of the board
z_min = 0
z_max = 10  # Example z-range

# Finger position
finger_x = 4
finger_y = 5
finger_z = 7

# Check if the finger tip is on the board
if is_on_board(finger_x, finger_y, finger_z, x_min, x_max, y_board, z_min, z_max):
    print("The finger is on the board.")

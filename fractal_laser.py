import matplotlib.pyplot as plt
import numpy as np

def generate_fractal(iterations: int = 10000) -> np.ndarray:
    # Define the vertices of the triangle
    vertices = np.array([[0, 0], [0.5, np.sqrt(3) / 2], [1, 0]])

    # Start with an arbitrary point inside the triangle
    point = np.array([0.1, 0.1])
    points = [point]

    for _ in range(iterations):
        # Randomly select a vertex
        vertex = vertices[np.random.randint(0, 3)]
        # Move halfway from the current point to the selected vertex
        point = (point + vertex) / 2
        points.append(point)

    return np.array(points)

def save_to_svg(points: np.ndarray, filename: str = 'fractal.svg') -> None:
    # Create an SVG file with lines connecting the points
    with open(filename, 'w') as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="1024" height="1024">\n')
        for point in points:
            # Convert point from 0-1 scale to 1024x1024 scale
            x, y = point * 1024
            f.write(f'<circle cx="{x}" cy="{y}" r="1" fill="black" />\n')
        f.write('</svg>\n')

# Generate a Sierpinski triangle fractal
# fractal_points = generate_fractal()
# # Save the fractal to an SVG file, which is suitable for laser cutters
# save_to_svg(fractal_points)
def generate_hexagon_fractal(iterations: int = 10000) -> np.ndarray:
		# Define the vertices of the hexagon
    angles = np.linspace(0, 2 * np.pi, 7)[:-1]  # 6 angles for a hexagon, omitting the closing duplicate
    radius = 0.5  # Set a consistent radius for the hexagon
    vertices = np.stack((radius * np.cos(angles), radius * np.sin(angles)), axis=-1)

    # Start with an arbitrary point inside the hexagon
    point = np.random.uniform(-radius, radius, 2)
    points = [point]

    for _ in range(iterations):
        # Randomly select a vertex
        vertex = vertices[np.random.randint(0, 6)]
        # Move halfway from the current point to the selected vertex
        point = (point + vertex) / 2
        points.append(point)

    return np.array(points)

def generate_dragon_curve_fractal(iterations: int = 20_000) -> np.ndarray:
    # Starting with a single right segment
    directions = [0]  # 0: right, 1: up, 2: left, 3: down

    # Generate the sequence of turns
    for _ in range(iterations):
        new_directions = [(i + 1) % 4 for i in reversed(directions)]  # Turn all directions right in the reverse order
        directions = directions + [0] + new_directions  # Add a right turn between the old and new directions

    # Convert the sequence of directions into points
    direction_to_point = {0: np.array([1, 0]), 1: np.array([0, 1]), 2: np.array([-1, 0]), 3: np.array([0, -1])}
    point = np.array([0, 0])
    points = [point]

    for direction in directions:
        point = point + direction_to_point[direction]
        points.append(point)

    return np.array(points)

# Generate the Dragon curve fractal
dragon_curve_fractal_points = generate_dragon_curve_fractal(iterations=100)
print("DONE WITH IT")
# Save the fractal to an SVG file
save_to_svg(dragon_curve_fractal_points, 'dragon_curve_fractal.svg')

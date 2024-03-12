# import turtle
from svg_turtle import SvgTurtle
from functools import partial
import xml.etree.ElementTree as ET

import svgwrite

# def add_border_to_svg(input_filename: str, output_filename: str, padding: int = 5):
#     # Read the original SVG file
#     with open(input_filename, 'r') as file:
#         original_svg_content = file.read()

#     # Create a new SVG drawing
#     dwg = svgwrite.Drawing(output_filename)

#     # Assuming you have the bounding box of your original SVG content,
#     # for example (min_x, min_y, max_x, max_y). You might need to calculate this
#     # based on your SVG's content or use external libraries.
#     # Here, I'm using placeholder values:
#     min_x, min_y, max_x, max_y = 10, 10, 100, 100  # Replace these with your actual values

#     # Add padding to the bounding box for the border
#     border_min_x, border_min_y = min_x - padding, min_y - padding
#     border_max_x, border_max_y = max_x + padding, max_y + padding
#     border_width, border_height = border_max_x - border_min_x, border_max_y - border_min_y

#     # Draw the border rectangle
#     dwg.add(dwg.rect(insert=(border_min_x, border_min_y), size=(border_width, border_height),
#                      stroke='black', fill='none', stroke_width=2))

#     # Add the original SVG content. This might need to be adapted if your SVG has specific requirements.
#     dwg.add(dwg.raw(original_svg_content))

#     # Save the new SVG with the border
#     dwg.save()


def add_border_to_svg(input_filename: str, output_filename: str, padding: int = 0):
        # Parse the original SVG file
    tree = ET.parse(input_filename)
    root = tree.getroot()

    # Extract original width and height (assuming they are directly on the root SVG element and have 'px' units)
    original_width = int(root.attrib['width'].replace('px', ''))
    original_height = int(root.attrib['height'].replace('px', ''))

    start_offset_height = 320
    start_offset_width = 130
    offset_width = 130
    offset_height = 0
    # Calculate new width and height with padding
    new_width = original_width +  2* padding + offset_width + start_offset_width
    new_height = original_height + 2 * padding + offset_height + start_offset_height

    # Update root SVG's width and height
    root.attrib['width'] = f"{new_width}px"
    root.attrib['height'] = f"{new_height}px"

    # Create the new border rectangle
    # Note: SVG origin (0,0) is at the top-left, adjust 'x' and 'y' to move the rectangle into position
    border = ET.Element("{http://www.w3.org/2000/svg}rect", {
        'x': str(start_offset_width + padding),
        'y': str(start_offset_height + padding),
        'width': str(original_width + offset_width),
        'height': str(original_height + offset_height),
        'fill': 'none',
        'stroke': 'red',
        'stroke-width': '1'
    })

    # Insert the new border at the beginning of the SVG (so it appears behind existing graphics)
    root.insert(0, border)

    # Save the modified SVG
    tree.write(output_filename, xml_declaration=True, encoding='utf-8')


def gen_og_pattern():
  nreplacements = 11
  angle = 120
  step = 3

  # generate command
  cmd = 'f'
  for _ in range(nreplacements):
      cmd = cmd.replace('f', 'f+f-f')

  # draw
  t = SvgTurtle(1000, 1000)
  t.pencolor((0, 0, 1))

  i2c = {'f': partial(t.forward, step),
         '+': partial(t.left, angle),
         '-': partial(t.right, angle),
  }
  for c in cmd: i2c[c]()
  t.save_as('dragon_turtle.svg')

def gen_drawing_fix():
  add_border_to_svg('dragon_turtle.svg', 'dragon_turtle_out.svg')

gen_og_pattern()
gen_drawing_fix()
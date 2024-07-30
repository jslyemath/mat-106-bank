import os
import sys
import shutil
import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import numpy as np
import random

def plot_area_model(shape='circle', numerator=1, denominator=1, dir_path='outcomes/F2/', save_as='example_model.png'):
    filepath = os.path.join(dir_path, save_as)

    def plot_circles(num, denom, filename='outcomes/F2/example_area_model.png'):
        n = math.ceil(num / denom)  # Number of circles to draw
        plt.figure(figsize=(10,6))
        fig, ax = plt.subplots()

        filled_wedges = 0  # Counter for the number of filled wedges

        for i in range(n):
            x_offset = (2.1 * i)  # Horizontal offset for each circle
            r = 1  # Radius for each circle
            for j in range(denom):
                theta1 = j * (360 / denom)  # Start angle of the sector
                theta2 = (j + 1) * (360 / denom)  # End angle of the sector
                
                if filled_wedges < num:
                    facecolor = 'lightblue'
                    filled_wedges += 1
                else:
                    facecolor = 'white'
                    
                wedge = patches.Wedge((x_offset, 0), r, theta1, theta2, facecolor=facecolor, edgecolor='black')
                ax.add_patch(wedge)

        ax.set_aspect('equal')
        ax.set_xlim(-1, 2.1 * n -1)
        ax.set_ylim(-1.1, 1.1)
        ax.axis('off')
        
        # Save the plot to a file
        plt.savefig(filename, format='png', transparent=True, bbox_inches='tight')
        plt.cla() 
        plt.clf()
        plt.close()

        return None

    
    def plot_trapezoids(num, denom, filename='outcomes/F2/example_area_model.png'):
        assert denom in [2, 3, 6], "denom must be 2, 3, or 6"
        
        n = math.ceil(num / denom)  # Number of trapezoids to draw
        fig, ax = plt.subplots()

        filled_shapes = 0  # Counter for the number of filled shapes

        for i in range(n):
            x_offset = (2.1 * i)  # Horizontal offset for each trapezoid
            top_base = 1
            bottom_base = 2
            height = 1

            # Base vertices of the trapezoid
            base_left = (x_offset - bottom_base / 2, 0)
            base_right = (x_offset + bottom_base / 2, 0)
            top_left = (x_offset - top_base / 2, height)
            top_right = (x_offset + top_base / 2, height)
            mid_base = (x_offset, 0)
            quarter_left = (x_offset - bottom_base / 4, 0)
            quarter_right = (x_offset + bottom_base / 4, 0)
            mid_top = (x_offset, height)

            # Draw the base trapezoid
            trapezoid = patches.Polygon([base_left, base_right, top_right, top_left], closed=True, edgecolor='black', facecolor='none')
            ax.add_patch(trapezoid)
            
            if denom == 2:
                for j in range(2):
                    if filled_shapes < num:
                        facecolor = 'lightblue'
                        filled_shapes += 1
                    else:
                        facecolor = 'white'
                    
                    if j == 0:
                        shape = patches.Polygon([base_left, mid_base, mid_top, top_left], closed=True, edgecolor='black', facecolor=facecolor)
                    else:
                        shape = patches.Polygon([mid_base, base_right, top_right, mid_top], closed=True, edgecolor='black', facecolor=facecolor)
                    ax.add_patch(shape)
            
            elif denom == 3:
                for j in range(3):
                    if filled_shapes < num:
                        facecolor = 'lightblue'
                        filled_shapes += 1
                    else:
                        facecolor = 'white'
                    
                    if j == 0:
                        shape = patches.Polygon([base_left, mid_base, top_left], closed=True, edgecolor='black', facecolor=facecolor)
                    elif j == 1:
                        shape = patches.Polygon([top_left, top_right, mid_base], closed=True, edgecolor='black', facecolor=facecolor)
                    else:
                        shape = patches.Polygon([mid_base, base_right, top_right], closed=True, edgecolor='black', facecolor=facecolor)
                    ax.add_patch(shape)
            
            elif denom == 6:
                vertices = [
                    (base_left, quarter_left, top_left),
                    (quarter_left, mid_base, top_left),
                    (mid_base, quarter_right, top_right),
                    (quarter_right, base_right, top_right),
                    (top_left, mid_top, mid_base),
                    (mid_base, mid_top, top_right)
                ]
                for j in range(6):
                    if filled_shapes < num:
                        facecolor = 'lightblue'
                        filled_shapes += 1
                    else:
                        facecolor = 'white'
                    
                    shape = patches.Polygon([vertices[j][0], vertices[j][1], vertices[j][2]], closed=True, edgecolor='black', facecolor=facecolor)
                    ax.add_patch(shape)

        ax.set_aspect('equal')
        ax.set_xlim(-1, 2.1 * n - 1)
        ax.set_ylim(-0.1,1.1)
        ax.axis('off')
        
        # Save the plot to a file
        plt.savefig(filename, format='png', transparent=True, bbox_inches='tight')
        plt.cla() 
        plt.clf()
        plt.close()

        return None

    
    def plot_triangles(num, denom, filename='outcomes/F2/example_area_model.png'):
        assert denom in [2, 3], "denom must be 2 or 3"
        
        n = math.ceil(num / denom)  # Number of triangles to draw
        fig, ax = plt.subplots()

        filled_shapes = 0  # Counter for the number of filled shapes

        for i in range(n):
            x_offset = 1.1 * i  # Horizontal offset for each triangle
            side_length = 1
            height = np.sqrt(3) / 2 * side_length

            # Base vertices of the triangle
            bottom_left = (x_offset - side_length / 2, 0)
            bottom_right = (x_offset + side_length / 2, 0)
            top = (x_offset, height)
            mid_base = (x_offset, 0)
            center = ((bottom_left[0] + bottom_right[0] + top[0]) / 3,
                    (bottom_left[1] + bottom_right[1] + top[1]) / 3)

            # Draw the base triangle
            triangle = patches.Polygon([bottom_left, bottom_right, top], closed=True, edgecolor='black', facecolor='none')
            ax.add_patch(triangle)
            
            if denom == 2:
                for j in range(2):
                    if filled_shapes < num:
                        facecolor = 'lightblue'
                        filled_shapes += 1
                    else:
                        facecolor = 'white'
                    
                    if j == 0:
                        shape = patches.Polygon([bottom_left, mid_base, top], closed=True, edgecolor='black', facecolor=facecolor)
                    else:
                        shape = patches.Polygon([mid_base, bottom_right, top], closed=True, edgecolor='black', facecolor=facecolor)
                    ax.add_patch(shape)
            
            elif denom == 3:
                vertices = [
                    (bottom_left, center, top),
                    (bottom_right, center, top),
                    (bottom_left, bottom_right, center)
                ]
                for j in range(3):
                    if filled_shapes < num:
                        facecolor = 'lightblue'
                        filled_shapes += 1
                    else:
                        facecolor = 'white'
                    
                    shape = patches.Polygon([vertices[j][0], vertices[j][1], vertices[j][2]], closed=True, edgecolor='black', facecolor=facecolor)
                    ax.add_patch(shape)

        ax.set_aspect('equal')
        ax.set_xlim(-0.5, 1.1 * n - 0.6)
        ax.set_ylim(-0.1, np.sqrt(3) / 2 + 0.1)
        ax.axis('off')
        
        # Save the plot to a file
        plt.savefig(filename, format='png', transparent=True, bbox_inches='tight')
        plt.cla() 
        plt.clf()
        plt.close()

        return None

    
    def plot_hexagons(num, denom, filename='outcomes/F2/example_area_model.png'):
        assert denom in [2, 3, 4, 6], "denom must be 2, 3, 4, or 6"
        
        n = math.ceil(num / denom)  # Number of hexagons to draw
        fig, ax = plt.subplots()

        filled_shapes = 0  # Counter for the number of filled shapes

        for i in range(n):
            x_offset = 2.2 * i  # Horizontal offset for each hexagon
            side_length = 1
            height = np.sqrt(3) * side_length
            
            # Define the vertices of the hexagon
            vertices = np.array([
                (x_offset + side_length * np.cos(np.pi / 3 * j), side_length * np.sin(np.pi / 3 * j)) for j in range(6)
            ])
            center = (x_offset, 0)
            mid_top = (x_offset, np.sqrt(3) / 2)
            mid_bottom = (x_offset, -np.sqrt(3) / 2)
            
            # Draw the base hexagon
            hexagon = patches.Polygon(vertices, closed=True, edgecolor='black', facecolor='none')
            ax.add_patch(hexagon)
            
            if denom == 2:
                shapes = [
                    [vertices[0], vertices[1], vertices[2], vertices[3]],
                    [vertices[3], vertices[4], vertices[5], vertices[0]]
                ]
            
            elif denom == 3:
                shapes = [
                    [vertices[0], vertices[1], vertices[2], center],
                    [vertices[2], vertices[3], vertices[4], center],
                    [vertices[4], vertices[5], vertices[0], center]
                ]
            
            elif denom == 4:
                shapes = [
                    [vertices[0], vertices[1], mid_top, center],
                    [mid_top, vertices[2], vertices[3], center],
                    [vertices[3], vertices[4], mid_bottom, center],
                    [mid_bottom, vertices[5], vertices[0], center]
                ]
            
            elif denom == 6:
                shapes = [
                    [vertices[j], vertices[(j + 1) % 6], center] for j in range(6)
                ]

            for shape in shapes:
                if filled_shapes < num:
                    facecolor = 'lightblue'
                    filled_shapes += 1
                else:
                    facecolor = 'white'
                
                poly = patches.Polygon(shape, closed=True, edgecolor='black', facecolor=facecolor)
                ax.add_patch(poly)

        ax.set_aspect('equal')
        ax.set_xlim(-1, 2.2 * n - 1.2)
        ax.set_ylim(-1, 1)
        ax.axis('off')
        
        # Save the plot to a file
        plt.savefig(filename, format='png', transparent=True, bbox_inches='tight')
        plt.cla() 
        plt.clf()
        plt.close()

        return None

    
    def plot_rectangles(num, denom, filename='outcomes/F2/example_area_model.png'):
        n = math.ceil(num / denom)  # Number of main rectangles to draw
        fig, ax = plt.subplots()

        filled_shapes = 0  # Counter for the number of filled shapes

        for i in range(n):
            x_offset = 2.6 * i  # Horizontal offset for each main rectangle
            width = 2
            height = 1
            sub_rect_width = width / denom

            # Draw the base rectangle
            base_rect = patches.Rectangle((x_offset, 0), width, height, edgecolor='black', facecolor='none')
            ax.add_patch(base_rect)
            
            for j in range(denom):
                if filled_shapes < num:
                    facecolor = 'lightblue'
                    filled_shapes += 1
                else:
                    facecolor = 'white'
                
                # Calculate the position of the smaller rectangles
                sub_rect = patches.Rectangle((x_offset + j * sub_rect_width, 0), sub_rect_width, height, edgecolor='black', facecolor=facecolor)
                ax.add_patch(sub_rect)

        ax.set_aspect('equal')
        ax.set_xlim(0, 2.6 * n -0.6)
        ax.set_ylim(-0.1, 1.1)
        ax.axis('off')
        
        # Save the plot to a file
        plt.savefig(filename, format='png', transparent=True, bbox_inches='tight')
        plt.cla() 
        plt.clf()
        plt.close()

        return None

    
    def plot_semicircles(num, denom, filename='outcomes/F2/example_area_model.png'):
        n = math.ceil(num / denom)  # Number of semicircles to draw
        fig, ax = plt.subplots()

        filled_shapes = 0  # Counter for the number of filled shapes

        for i in range(n):
            x_offset = 2.5 * i  # Horizontal offset for each semicircle
            radius = 1
            theta_step = 180 / denom

            for j in range(denom):
                if filled_shapes < num:
                    facecolor = 'lightblue'
                    filled_shapes += 1
                else:
                    facecolor = 'white'
                
                # Calculate the start and end angles for each sector
                theta1 = j * theta_step
                theta2 = (j + 1) * theta_step
                
                wedge = patches.Wedge((x_offset, 0), radius, theta1, theta2, edgecolor='black', facecolor=facecolor)
                ax.add_patch(wedge)
            
            # Draw the base semicircle outline
            arc = patches.Arc((x_offset, 0), 2 * radius, 2 * radius, angle=0, theta1=0, theta2=180, edgecolor='black')
            ax.add_patch(arc)

        ax.set_aspect('equal')
        ax.set_xlim(-1, 2.5 * n -1.5)
        ax.set_ylim(-0.1, 1.1)
        ax.axis('off')
        
        # Save the plot to a file
        plt.savefig(filename, format='png', transparent=True, bbox_inches='tight')
        plt.cla() 
        plt.clf()
        plt.close()

        return None
    
    shapes_dict = {
        'circle': plot_circles,
        'isosceles trapezoid': plot_trapezoids,
        'equilateral triangle': plot_triangles,
        'regular hexagon': plot_hexagons,
        'rectangle': plot_rectangles,
        'semicircle': plot_semicircles
        }
    
    shapes_dict[shape](numerator, denominator, filename=filepath)


def plot_number_line(ticks, labels={0: '0'}, points=[], dir_path='outcomes/F2/', save_as='example_line.png'):
    filepath = os.path.join(dir_path, save_as)

    line_thickness = 1.75
    tick_thickness = 1.75
    fig, ax = plt.subplots(figsize=(10, 2))

    # Draw the double-sided arrow with specified line thickness
    arrow_style = '<|-|>'
    arrow = patches.FancyArrowPatch((-1.75, 0), (ticks + 0.75, 0),
                            arrowstyle=arrow_style, linewidth=line_thickness, color='black', mutation_scale=30)
    ax.add_patch(arrow)

    # Draw the ticks with specified thickness and label the first tick as 0
    for i in range(ticks):
        ax.plot([i, i], [0.07, -0.07], 'k-', linewidth=tick_thickness)
        if i in labels.keys():
            ax.annotate(f'{labels[i]}', xy=(i, 0), xytext=(i, -0.25), horizontalalignment='center', fontsize=14)

    # Draw requested points
    for point in points:
        ax.scatter(point, 0, color='blue', s=70, zorder=5)

    # Remove the axes
    ax.axis('off')

    # Set the limits of the number line
    ax.set_xlim(-2, ticks + 1)
    ax.set_ylim(-0.5, 0.5)
    
    # Save the figure to the specified file
    plt.savefig(filepath, bbox_inches='tight')
    plt.cla() 
    plt.clf()
    plt.close()


def create_null_graphic(dir_path='outcomes/F2/', save_as='null.png'):
    filepath = os.path.join(dir_path, save_as)
    source_file = 'assets/null.png'

    # Copy the file to the new directory with the new name
    shutil.copy(source_file, filepath)
    return None


def create_graphics_set(data, dir_path='outcomes/F2/'):
    # p1 graphics
    if data['p1_type'] == 'line':
        # prob
        p1_ticks = max(int(data['p1_orig_loc']), int(data['p1_requested_loc'])) + random.randint(1, 4)
        p1_labels = {0: '0', int(data['p1_orig_loc']): '1'}
        plot_number_line(p1_ticks, labels=p1_labels, dir_path=dir_path, save_as='p1_prob_model.png')

        # ans
        p1_labels = {0: '0', int(data['p1_orig_loc']): '1', int(data['p1_requested_loc']): f"{data['p1_requested_num']}/{data['p1_requested_denom']}"}
        points = [int(data['p1_requested_loc'])]
        plot_number_line(p1_ticks, labels=p1_labels, points=points, dir_path=dir_path, save_as='p1_ans_model.png')
    else:
        # prob
        create_null_graphic(dir_path=dir_path, save_as='p1_prob_model.png')

        # ans
        p1_shape = data['p1_type']
        p1_numerator = int(data['p1_model_num'])
        p1_denominator = int(data['p1_model_denom'])
        plot_area_model(shape=p1_shape, numerator=p1_numerator, denominator=p1_denominator, dir_path=dir_path, save_as='p1_ans_model.png')
    
    # p2 graphics
    if data['p2_type'] == 'line':
        # prob
        p2_ticks = max(int(data['p2_orig_loc']), int(data['p2_requested_loc'])) + random.randint(1, 4)
        p2_labels = {0: '0', int(data['p2_orig_loc']): '1'}
        plot_number_line(p2_ticks, labels=p2_labels, dir_path=dir_path, save_as='p2_prob_model.png')

        # ans
        p2_labels = {0: '0', int(data['p2_orig_loc']): '1', int(data['p2_requested_loc']): f"{data['p2_requested_num']}/{data['p2_requested_denom']}"}
        points = [int(data['p2_requested_loc'])]
        plot_number_line(p2_ticks, labels=p2_labels, points=points, dir_path=dir_path, save_as='p2_ans_model.png')
    else:
        # prob
        create_null_graphic(dir_path=dir_path, save_as='p2_prob_model.png')

        # ans
        p2_shape = data['p2_type']
        p2_numerator = int(data['p2_model_num'])
        p2_denominator = int(data['p2_model_denom'])
        plot_area_model(shape=p2_shape, numerator=p2_numerator, denominator=p2_denominator, dir_path=dir_path, save_as='p2_ans_model.png')
    
    # p3 graphics
    if data['p3_type'] == 'line':
        # prob
        p3_ticks = max(int(data['p3_orig_loc']), int(data['p3_requested_loc'])) + random.randint(1, 4)
        p3_labels = {0: '0', int(data['p3_orig_loc']): f"{data['p3_orig_num']}/{data['p3_orig_denom']}"}
        plot_number_line(p3_ticks, labels=p3_labels, dir_path=dir_path, save_as='p3_prob_model.png')

        # ans
        p3_labels = {0: '0', int(data['p3_orig_loc']): f"{data['p3_orig_num']}/{data['p3_orig_denom']}", int(data['p3_requested_loc']): f"{data['p3_requested_num']}/{data['p3_requested_denom']}"}
        points = [int(data['p3_requested_loc'])]
        plot_number_line(p3_ticks, labels=p3_labels, points=points, dir_path=dir_path, save_as='p3_ans_model.png')
    else:
        # prob
        create_null_graphic(dir_path=dir_path, save_as='p3_prob_model.png')

        # ans
        p3_shape = data['p3_type']
        p3_numerator = int(data['p3_model_num'])
        p3_denominator = int(data['p3_model_denom'])
        plot_area_model(shape=p3_shape, numerator=p3_numerator, denominator=p3_denominator, dir_path=dir_path, save_as='p3_ans_model.png')
    
    return None


generated_folder = 'assets/F2/generated/'

with open('assets/F2/generated/seeds.json', 'r') as file:
    seeds_dict = json.load(file)
    
print('Generating...')
# matplotlib has memory leaks that I can't figure out - do the ranges in batches
for i in range(0, 50):
    data = seeds_dict['seeds'][i]['data']

    seed_folder = os.path.join(generated_folder, data['__seed__'])
    if not os.path.exists(seed_folder):
        os.makedirs(seed_folder)

    create_graphics_set(data, dir_path=seed_folder)
    plt.cla() 
    plt.clf()
    plt.close('all')
    if i % 10 == 0:
        print(f'{i}...')

print('Done!')
sys.exit()

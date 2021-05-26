from obj import ObjRandom
from campo import Place
from coordenada import Coordinate
from bokeh.plotting import figure, show

def movement(place, obj, steps):
    begin = place.get_obj_coord(obj)

    for _ in range(steps):
        place.move_obj(obj)

    return begin.distance(place.get_obj_coord(obj))


def sim_movement(steps, iterations, obj_kind):
    obj = obj_kind(name="Something")
    origin = Coordinate(0,0)
    distances = []

    for _ in range(iterations):
        place = Place()
        place.add_obj(obj, origin)
        sim_movement = movement(place, obj, steps)
        distances.append(round(sim_movement, 1))

    return distances

def plot(x, y):
    grafica = figure(title="Camino aleatorio", x_axis_label = "steps", y_axis_label = "distance")
    grafica.line(x, y, legend_label = "Middle distance")

    show(grafica)

def main(distances, iterations, obj_kind):
    distance_middle_per_movement = []

    for steps in distances:
        distance = sim_movement(steps, iterations, obj_kind)
        distance_middle = round(sum(distance) / len(distance), 4)
        distance_middle_per_movement.append(distance_middle)
        distance_max = max(distance)
        distance_min = min(distance)
        print(f'{obj_kind.__name__} move steps {steps}')
        print(f'Media: {distance_middle}')
        print(f'Max: {distance_max}')
        print(f'Min: {distance_min}')

    plot(distances, distance_middle_per_movement)

if __name__ == '__main__':
    distances = [10, 100, 1000, 10000]
    iterations = 100

    main(distances, iterations, ObjRandom)


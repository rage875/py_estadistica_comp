class Place:
    def __init__(self):
        self.objs_coords = {}

    def add_obj(self, obj, coord):
        self.objs_coords[obj] = coord
    
    def move_obj(self, obj):
        delta_x,  delta_y = obj.move()
        actual_coord = self.objs_coords[obj]
        new_coord = actual_coord.move(delta_x, delta_y)

        self.objs_coords[obj] = new_coord

    def get_obj_coord(self, obj):
        return self.objs_coords[obj]
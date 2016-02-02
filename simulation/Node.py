class Node:
    """
    Will be each node on the screen - robot - obj etc...
    """

    def __init__(self, x1, y1,
                 side_len,
                 canvas_in,
                 weight=1,
                 price=5,
                 colour="#555",
                 outline="#666",
                 robot_colour = "#f27"
                 ):

        x2 = x1 + side_len
        y2 = y1 + side_len
        # initialise the coordinates for the vertice
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.colour = colour
        # colour to change the node to that's representing the robot
        self.robot_colour = robot_colour
        self.canv = canvas_in
        self.outline = outline
        # all nodes are of weight 1 initially
        self.weight = weight
        # TODO the vertices just have a price of 5 atm
        self.value = price
        # not sure if this'll be useful atm
        self.am_robot = False

    def display(self):
        """display the vertice on screen"""
        self.canv.create_rectangle(self.x1,
                                self.y1,
                                self.x2,
                                self.y2,
                                fill= self.colour,
                                outline=self.outline)

    def get_neighbours(self):
        """needs to know what vertices are near to it and work out the weight to
        travel to them (which will be used in the case of avoiding and obstacles)
        The way to get them will be using the matrix calculation I think...
        this is only for square matrices
        x = col = ceil(node_n / matrix_width)
        y = row = node_n mod(matrix_width)
        """
        pass

    def set_robot(self):
        """This needs to set the colour of a node to be the robot colour
        Maybe this should also take input to change the last one from being a
        robot
        """
        self.am_robot = True
        self.set_colour(self.robot_colour)

    def set_colour(self, c):
        """
        Change the colour of the node - this will be used to show that the node
        currently has the robot on it... maybe this should be another method as well
        """
        self.colour = c

    def __str__(self):
        info = "x1 = {}, y1 = {},\nx2 = {}, y2 = {}\n".format(
            self.x1, self.y1, self.x2, self.y2)
        return info

    def pass_the_butter(self):
        return "butter"

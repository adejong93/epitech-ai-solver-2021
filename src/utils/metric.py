import copy
import time
# import resource
import psutil


class Metric:

    """Take measurements of search performance."""

    def __init__(self,
                 frontier   = None):

        self.path_to_goal = []
        self.path_to_goal_list = []
        self.nodes_expanded = 0
        self.fringe = frontier
        self.max_fringe_size = 0
        self.search_depth = 0
        self.max_search_depth = 0
        self.start_time = 0
        self.end_time = 0
        self.search_time = 0
        self.max_ram_useage = 0


    def cost_of_path(self):
        """Return the number of steps taken to reach the goal"""
        return len(self.path_to_goal)


    def fringe_size(self):
        """Return the length of the fringe (frontier)"""
        if self.fringe is None: return 0
        return len(self.fringe.queue)


    def update_max_fringe(self):
        """Update the value of max_fringe_size!"""
        if self.fringe is None: return 0
        fringe_length = self.fringe_size()
        if fringe_length > self.max_fringe_size:
            self.max_fringe_size = fringe_length


    def update_max_depth(self):
        """Update the maximum search depth reached"""
        if self.search_depth > self.max_search_depth:
            self.max_search_depth = copy.copy(self.search_depth)

    def start_timer(self):
        self.start_time = time.time()


    def stop_timer(self):
        self.end_time = time.time()
        self.search_time = "{0:.2f}".format((self.end_time - self.start_time) * 1000)
        

    def measure_ram_useage(self):
        if self.max_ram_useage < psutil.virtual_memory().percent:
            self.max_ram_useage = psutil.virtual_memory().percent
        # self.max_ram_useage = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) / 1000

    def from_path_to_goal_list(self, initial):
        for i in range(len(initial)):
            for j in range(len(initial[i])):
                if initial[i][j] == 0:
                    pos_x = i
                    pos_y = j
                    break
        self.path_to_goal_list = [initial]
        for move in self.path_to_goal:
            next_state = copy.deepcopy(self.path_to_goal_list[-1])
            if move == 'down':
                next_state[pos_x][pos_y] = next_state[pos_x - 1][pos_y]
                next_state[pos_x - 1][pos_y] = 0
                pos_x -= 1
            elif move == 'up':
                next_state[pos_x][pos_y] = next_state[pos_x + 1][pos_y]
                next_state[pos_x + 1][pos_y] = 0
                pos_x += 1
            elif move == 'right':
                next_state[pos_x][pos_y] = next_state[pos_x][pos_y - 1]
                next_state[pos_x][pos_y - 1] = 0
                pos_y -= 1
            elif move == 'left':
                next_state[pos_x][pos_y] = next_state[pos_x][pos_y + 1]
                next_state[pos_x][pos_y + 1] = 0
                pos_y += 1
            self.path_to_goal_list.append(copy.deepcopy(next_state))

class Movie:
    def __init__(self, name, director, rating, year, watched=False, next_movie=None, prev_movie=None):
        self.name = name
        self.director = director
        self.rating = rating
        self.year = year
        self.watched = watched
        self.next_movie = next_movie
        self.prev_movie = prev_movie

    def __repr__(self):
        return f'''
        -----------------
        Title: {self.name}
        Director: {self.director}
        Year: {self.year}
        Rating: {self.rating}
        -----------------
        '''

    def set_next_movie(self, next_movie):
        self.next_movie = next_movie

    def get_next_movie(self):
        return self.next_movie

    def set_prev_movie(self, prev_movie):
        self.prev_movie = prev_movie

    def get_prev_movie(self):
        return self.prev_movie

    def get_title(self):
        return self.name

    def get_director(self):
        return self.director

    def get_year(self):
        return self.year

    def get_rating(self):
        return self.rating


class Genre:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, name, director, rating, year):
        new_head = Movie(name, director, rating, year)
        current_head = self.head_node

        if current_head is not None:
            current_head.set_prev_movie(new_head)
            new_head.set_next_movie(current_head)

        self.head_node = new_head

        if self.tail_node is None:
            self.tail_node = new_head

    def add_to_tail(self, name, director, rating, year):
        new_tail = Movie(name, director, rating, year)
        current_tail = self.tail_node

        if current_tail is not None:
            current_tail.set_next_movie(new_tail)
            new_tail.set_prev_movie(current_tail)

        self.tail_node = new_tail

        if self.head_node is None:
            self.head_node = new_tail

    def remove_head(self):
        removed_head = self.head_node

        if removed_head is None:
            return None

        self.head_node = removed_head.get_next_movie()

        if self.head_node is not None:
            self.head_node.set_prev_movie(None)

        if removed_head == self.tail_node:
            self.remove_tail()

        return removed_head

    def remove_tail(self):
        removed_tail = self.tail_node

        if removed_tail is None:
            return None

        self.tail_node = removed_tail.get_prev_movie()

        if self.tail_node is not None:
            self.tail_node.set_next_movie(None)

        if removed_tail == self.head_node:
            self.remove_head()

        return removed_tail

    def remove_by_value(self, value_to_remove):
        node_to_remove = None
        current_node = self.head_node

        while current_node is not None:
            if current_node.get_title() == value_to_remove:
                node_to_remove = current_node
                break

            current_node = current_node.get_next_movie()

        if node_to_remove is None:
            return None

        if node_to_remove == self.head_node:
            self.remove_head()
        elif node_to_remove == self.tail_node:
            self.remove_tail()
        else:
            next_node = node_to_remove.get_next_movie()
            prev_node = node_to_remove.get_prev_movie()
            next_node.set_prev_movie(prev_node)
            prev_node.set_next_movie(next_node)

        return node_to_remove

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_title() is not None:
                string_list += str(current_node)
            current_node = current_node.get_next_movie()
        return string_list

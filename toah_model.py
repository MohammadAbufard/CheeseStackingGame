"""
TOAHModel:  Model a game of Tour of Anne Hoy
Cheese:   Model a cheese with a given (relative) size
IllegalMoveError: Type of exceptions thrown when an illegal move is attempted
MoveSequence: Record of a sequence of (not necessarily legal) moves. You will
need to return a MoveSequence object after solving an instance of the 4-stool
Tour of Anne Hoy game, and we will use that to check the correctness of your
algorithm.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro, Ritu Chaturvedi, Samar Sabie
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2018.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
#

#class CheeseNotFound (Exception):
  #  pass

class TOAHModel:
    """ Model a game of Tour Of Anne Hoy.

    Model stools holding stacks of cheese, enforcing the constraint
    that a larger cheese may not be placed on a smaller one.
    """

    def __init__(self, number_of_stools):
        """ Create new TOAHModel with empty stools
        to hold stools of cheese.

        @param TOAHModel self:
        @param int number_of_stools:
        @rtype: None

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> (M.get_number_of_stools(), M.number_of_moves()) == (4,0)
        True
        >>> M.get_number_of_cheeses()
        5
        """
        # you must have _move_seq as well as any other attributes you choose
        self._move_seq = MoveSequence([])
        self.number_of_stools = number_of_stools
        self.total_num_of_moves = 0

        #creating an list where all the stools information is stored in a list
        #named self._stool_storage
        self._stool_storage = []
        index = 0
        while index < self.number_of_stools:
            self._stool_storage.append([])
            index += 1


    def get_move_seq(self):
        """ Return the move sequence

        @type self: TOAHModel
        @rtype: MoveSequence

        >>> toah = TOAHModel(2)
        >>> toah.get_move_seq() == MoveSequence([])
        True
        """
        return self._move_seq


    def __eq__(self, other):
        """ Return whether TOAHModel self is equivalent to other.

        Two TOAHModels are equivalent if their current
        configurations of cheeses on stools look the same.
        More precisely, for all h,s, the h-th cheese on the s-th
        stool of self should be equivalent to the h-th cheese on the s-th
        stool of other

        @type self: TOAHModel
        @type other: TOAHModel
        @rtype: bool

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0, 1)
        >>> m1.move(0, 2)
        >>> m1.move(1, 2)
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0, 3)
        >>> m2.move(0, 2)
        >>> m2.move(3, 2)
        >>> m1 == m2
        True
        """

        if type(self) == type(other):
            if len(self._stool_storage) != len(other._stool_storage):
                return False

            else:
                for index in range(len(self._stool_storage)):
                    if self._stool_storage[index] != other._stool_storage[index]:
                        return False
                return True


    def _cheese_at(self, stool_index, stool_height):
        # """ Return (stool_height)th from stool_index stool, if possible.
        #
        # @type self: TOAHModel
        # @type stool_index: int
        # @type stool_height: int
        # @rtype: Cheese | None
        #
        # >>> M = TOAHModel(4)
        # >>> M.fill_first_stool(5)
        # >>> M._cheese_at(0,3).size
        # 2
        # >>> M._cheese_at(0,0).size
        # 5
        # """
        if 0 <= stool_height < len(self._stool_storage[stool_index]):
            return self._stool_storage[stool_index][stool_height]
        else:
            return None


    def __str__(self):
        """
        Depicts only the current state of the stools and cheese.

        @param TOAHModel self:
        @rtype: str
        """
        all_cheeses = []
        for height in range(self.get_number_of_cheeses()):
            for stool in range(self.get_number_of_stools()):
                if self._cheese_at(stool, height) is not None:
                    all_cheeses.append(self._cheese_at(stool, height))
        max_cheese_size = max([c.size for c in all_cheeses]) \
            if len(all_cheeses) > 0 else 0
        stool_str = "=" * (2 * max_cheese_size + 1)
        stool_spacing = "  "
        stools_str = (stool_str + stool_spacing) * self.get_number_of_stools()

        def _cheese_str(size):
            # helper for string representation of cheese
            if size == 0:
                return " " * len(stool_str)
            cheese_part = "-" + "--" * (size - 1)
            space_filler = " " * int((len(stool_str) - len(cheese_part)) / 2)
            return space_filler + cheese_part + space_filler

        lines = ""
        for height in range(self.get_number_of_cheeses() - 1, -1, -1):
            line = ""
            for stool in range(self.get_number_of_stools()):
                c = self._cheese_at(stool, height)
                if isinstance(c, Cheese):
                    s = _cheese_str(int(c.size))
                else:
                    s = _cheese_str(0)
                line += s + stool_spacing
            lines += line + "\n"
        lines += stools_str

        return lines


    def fill_first_stool (self, number_of_cheeses):
        """
        Given the number of cheese the user wants to have,
        Fill the first stool with the provided number of cheese
        """
        for element in range(number_of_cheeses, 0, -1):
            self._stool_storage[0].append(Cheese(element))


    def get_number_of_stools (self):
        """
        Return the total number of stools
        """
        return len(self._stool_storage)


    def number_of_moves (self):
        """
        Return the total number of moves
        """
        return self.total_num_of_moves


    def get_number_of_cheeses (self):
        """
        Return the total number of cheese on the stools
        """
        combined_stools = []

        # add all the nested lists to a temp_lst (combined_stools)
        for element in self._stool_storage:
            combined_stools += element
        return len(combined_stools)


    def get_cheese_location(self, cheese):
        """
        Given the target cheese return on which stool its on
        If not found raise an error
        """

        for index in range(len(self._stool_storage)):
            for element in self._stool_storage[index]:
                if cheese == element:
                    return index


    def get_top_cheese (self, index):
        """
        Given the stool number return the cheese on top
        """
        if len(self._stool_storage[index]) > 0:
            required_stool = self._stool_storage[index]
            return required_stool[-1]


    def add (self, cheese, stool):
        """
        Add the given cheese to the top of the provided tool number.
        If the move is illegal raise and IllegalMoveError error
        """
        if len(self._stool_storage[stool]) == 0 or self._stool_storage[stool][-1].size > cheese.size:
            self._stool_storage[stool].append(cheese)

        if cheese.size > self._stool_storage[stool][-1].size:
                raise IllegalMoveError


    def move (self, origin, destination):
        """
        Move the top cheese from the origin stool to the destination stool
        iff the move is legal else return an IllegalMoveError error.
        """
        done = False
        if origin < 0 or origin > len(self._stool_storage):
            raise IllegalMoveError

        if destination < 0 or destination > len(self._stool_storage):
            raise IllegalMoveError

        if origin == destination:
            raise IllegalMoveError

        if len(self._stool_storage[origin]) == 0:
            raise IllegalMoveError

        if len(self._stool_storage[origin]) > 0 and len(self._stool_storage[destination]) > 0:
            if self._stool_storage[origin][-1].size > self._stool_storage[destination][-1].size:
                raise IllegalMoveError

        if len(self._stool_storage[origin]) > 0 and len(self._stool_storage[destination]) == 0:
            done = True
            popped_item = self._stool_storage[origin].pop()
            self._stool_storage[destination].append(popped_item)
            self._move_seq.add_move(origin, destination)
            self.total_num_of_moves += 1

        if done == False:
            popped_item = self._stool_storage[origin].pop()
            self._stool_storage[destination].append(popped_item)
            self._move_seq.add_move(origin, destination)
            self.total_num_of_moves += 1

class Cheese:
    """ A cheese for stacking in a TOAHModel

    === Attributes ===
    @param int size: width of cheese
    """

    def __init__(self, size):
        """ Initialize a Cheese to diameter size.

        @param Cheese self:
        @param int size:
        @rtype: None

        >>> c = Cheese(3)
        >>> isinstance(c, Cheese)
        True
        >>> c.size
        3
        """
        self.size = size

    def __eq__(self, other):
        """ Is self equivalent to other?

        We say they are if they're the same
        size.

        @param Cheese self:
        @param Cheese|Any other:
        @rtype: bool
        """
        if type(self) == type(other):
            return self.size == other.size
        return self.size == other


class IllegalMoveError(Exception):
    """ Exception indicating move that violates TOAHModel
    """
    pass


class MoveSequence:
    """ Sequence of moves in TOAH game
    """

    def __init__(self, moves):
        """ Create a new MoveSequence self.

        @param MoveSequence self:
        @param list[tuple[int]] moves:
        @rtype: None
        """
        # moves - a list of integer pairs, e.g. [(0,1),(0,2),(1,2)]
        self._moves = moves

    def __eq__(self, other):
        """ Return whether MoveSequence self is equivalent to other.

        @param MoveSequence self:
        @param MoveSequence|Any other:
        @rtype: bool
        """
        return type(self) == type(other) and self._moves == other._moves

    def get_move(self, i):
        """ Return the move at position i in self

        @param MoveSequence self:
        @param int i:
        @rtype: tuple[int]

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.get_move(0) == (1, 2)
        True
        """
        # Exception if not (0 <= i < self.length)
        return self._moves[i]

    def add_move(self, src_stool, dest_stool):
        """ Add move from src_stool to dest_stool to MoveSequence self.

        @param MoveSequence self:
        @param int src_stool:
        @param int dest_stool:
        @rtype: None
        """
        self._moves.append((src_stool, dest_stool))

    def length(self):
        """ Return number of moves in self.

        @param MoveSequence self:
        @rtype: int

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.length()
        1
        """
        return len(self._moves)

    def generate_toah_model(self, number_of_stools, number_of_cheeses):
        """ Construct TOAHModel from number_of_stools and number_of_cheeses
         after moves in self.

        Takes the two parameters for
        the game (number_of_cheeses, number_of_stools), initializes the game
        in the standard way with TOAHModel.fill_first_stool(number_of_cheeses),
        and then applies each of the moves in this move sequence.

        @param MoveSequence self:
        @param int number_of_stools:
        @param int number_of_cheeses:
        @rtype: TOAHModel

        >>> ms = MoveSequence([])
        >>> toah = TOAHModel(2)
        >>> toah.fill_first_stool(2)
        >>> toah == ms.generate_toah_model(2, 2)
        True
        """
        model = TOAHModel(number_of_stools)
        model.fill_first_stool(number_of_cheeses)
        for move in self._moves:
            model.move(move[0], move[1])
        return model


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

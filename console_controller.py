"""
ConsoleController: User interface for manually solving
Anne Hoy's problems from the console.
"""


# Copyright 2014, 2017 Dustin Wehr, Danny Heap, Bogdan Simion,
# Jacqueline Smith, Dan Zingaro
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


from toah_model import TOAHModel, IllegalMoveError


def move(model, origin, dest):
    """ Apply move from origin to destination in model.

    May raise an IllegalMoveError.

    @param TOAHModel model:
        model to modify
    @param int origin:
        stool number (index from 0) of cheese to move
    @param int dest:
        stool number you want to move cheese to
    @rtype: None
    """
    TOAHModel.move(origin, dest)


class ConsoleController:
    """ Controller for text console.
    """

    def __init__(self, number_of_cheeses, number_of_stools):
        """ Initialize a new ConsoleController self.

        @param ConsoleController self:
        @param int number_of_cheeses:
        @param int number_of_stools:
        @rtype: None
        """
        self.number_of_cheeses = number_of_cheeses
        self.number_of_stools = number_of_stools


    def play_loop(self):
        """ Play Console-based game.

        @param ConsoleController self:
        @rtype: None

        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.
        """

        is_int = False
        toah_game = TOAHModel(self.number_of_stools)
        toah_game.fill_first_stool(self.number_of_cheeses)
        print(toah_game)
        print("Welcome to the Tour of Anne Hoy Game.")
        print("Enter a non-integer value such as a string(a) or a float(13.5) to quit the game.")
        print('')

        run = True

        while run:
            try:
                cheese_origin = int(input("Choose a stool number to move the cheese from: "))
                cheese_dest = int(input("Choose the stool you want to move the cheese to: "))
                toah_game.move(cheese_origin, cheese_dest)
                print(toah_game)


            except IllegalMoveError:
                print("Invalid move. Please reenter.")
                print("")

            except IndexError:
                print("Invalid stool number. Please reenter.")
                print("")

            except ValueError:
                print("")
                print("Game Ended. Thank you for playing.")
                run = False


if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.
    print("Welcome to the Tour of Anne Hoy Game.")
    print("To start the game please provide the following: ")
    print("")

    done = False

    while done == False:

        try:
                stools_num = int(input("Please enter the number of stools: "))
                cheese_num = int(input("Please enter the number of cheese: "))

                if stools_num >= 1 and cheese_num >= 0:
                    done = True
                    current_game = ConsoleController(cheese_num, stools_num)
                    current_game.play_loop()
                else:
                    print ("Please enter a an integer greater than zero")
                    print("")

        except ValueError:
            print("Invalid input. Please reenter: ")
            print("")

"""
functions to run TOAH tours.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro
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
# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr


# you may want to use time.sleep(delay_between_moves) in your
# solution for 'if __name__ == "__main__":'

import time
from toah_model import TOAHModel



## The three_stools and three_stools_animated function are taken from the lecture
## notes provided by professor Dan Zingaro
def three_stools(model, n, stool_one, stool_two, stool_three):
        if n == 0:
                return
        if n == 1:
                model.move(stool_one, stool_three)
                print('(' + str(stool_one) + ' --> ' + str(stool_three) +')')
                return
        else:
                three_stools(model, n-1, stool_one, stool_three, stool_two)
                model.move(stool_one, stool_three)
                print('(' + str(stool_one) + ' --> ' + str(stool_three) +')')
                three_stools(model, n-1, stool_two, stool_one, stool_three)
                return


def three_stools_animated(model, n, stool_one, stool_two, stool_three, delay):
        if n == 0:
                time.sleep(delay)
                return
        if n == 1:
                model.move(stool_one, stool_three)
                print(model)
                time.sleep(delay)
                return
        else:
                three_stools_animated(model, n-1, stool_one, stool_three, stool_two, delay)
                model.move(stool_one, stool_three)
                print(model)
                time.sleep(delay)
                three_stools_animated(model, n-1, stool_two, stool_one, stool_three, delay)
                return


def tour_of_four_stools(model, delay_btw_moves=0.5, animate=False):
    """Move a tower of cheeses from the first stool in model to the fourth.,

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    @rtype: None
    """
    total_number_cheese = model.get_number_of_cheeses()
    top_half = total_number_cheese // 2
    bottom_half = total_number_cheese - top_half

    if animate:
        print(model)
        if total_number_cheese != 0:
                three_stools_animated(model, top_half, 0,1,2, delay_btw_moves)
                three_stools_animated(model, bottom_half, 0,1,3, delay_btw_moves)
                three_stools_animated(model, top_half, 2,1,3, delay_btw_moves)
        else:
                pass


    else:
            if total_number_cheese != 0:
                    three_stools(model, top_half, 0,1,2)
                    three_stools(model, bottom_half, 0,1,3)
                    three_stools(model, top_half, 2,1,3)

            else:
                    pass


if __name__ == '__main__':
    num_cheeses = 5
    delay_between_moves = 0.5
    console_animate = False

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(number_of_cheeses=num_cheeses)

    tour_of_four_stools(four_stools,
                        animate=console_animate,
                        delay_btw_moves=delay_between_moves)

    print(four_stools.number_of_moves())

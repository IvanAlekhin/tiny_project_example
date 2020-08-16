from collections import defaultdict
import logging
logging.basicConfig(format='%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] \t %(message)s',
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


class ShipFinder:
    def __init__(self, filename: str, log_level: str):
        LOGGER.setLevel(log_level)
        self.filename = filename
        self.ship_list = []

    def count_ships(self):
        LOGGER.info('Try to open file from path {}'.format(self.filename))
        with open(self.filename, 'r') as f:
            line_counter = 0
            for line in f:
                self._validate_file_line(line_counter, line)
                element_counter = 0
                for deck in line:
                    if deck == '#':
                        self.find_ship_for_deck(line_counter, element_counter)
                    element_counter += 1
                line_counter += 1
        self._validate_ships_location()
        LOGGER.info('all ships coordinates: {}'.format(self.ship_list))
        return len(self.ship_list)

    def find_ship_for_deck(self, x: int, y: int):
        for ship in self.ship_list:
            for x_coord, y_coord in ship:
                is_deck_nearby = bool(abs(x - x_coord) <= 1 and abs(y - y_coord) <= 1)
                is_deck_nearby_diagonally = bool(abs(x - x_coord) == 1 and abs(y - y_coord) == 1)

                if is_deck_nearby and not is_deck_nearby_diagonally:
                    ship.append((x, y))  # deck relates to existing ship
                    return

        self.ship_list.append([(x, y)])  # new ship with one deck
        return

    def _validate_file_line(self, line_counter, line):
        if line_counter == 0:
            self.first_line_len = len(line.strip())

        elif self.first_line_len != len(line.strip()):
            raise ValueError('len of lines must be equal, but something wrong with {}-th line'.format(line_counter))

    def _validate_ships_location(self):
        for ship in self.ship_list:

            x_ship_detector = set()
            y_ship_detector = set()

            for x, y in ship:
                x_ship_detector.add(x)
                y_ship_detector.add(y)
            if len(x_ship_detector) != 1 and len(y_ship_detector) != 1:  # then ship isn't located on one line
                raise ValueError('Ships are too close')

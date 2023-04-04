class LevelReader:
    level_path = './levels/level'
    level_suffix = '.lvl'

    @staticmethod
    def get_int_array_from_file(level_number):
        file_name = LevelReader.level_path + str(level_number) + LevelReader.level_suffix
        array = []
        with open(file_name, 'r') as f:
            for line in f:
                array.append([int(x) for x in line.split()])
        return array

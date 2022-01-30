
from fileinput import filename


class Parser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        lines = []
        with open(self.file_path) as f:
            line = f.readline()

            lines.append(self._strip_user(line.rstrip('\n')))
            while line:
                line = f.readline()
                # Have to change the lecture name
                if line == '\n' or not line or not line.startswith('Sanja Fidler: '):
                    continue

                formatted_line = self._strip_user(line.rstrip('\n'))

                lines.append(formatted_line)
        return lines

    @staticmethod
    def _strip_user(text):
        for i in range(len(text)):
            if text[i] == ':':
                return text[i+2:]

    @staticmethod
    def export(lines, filename):
        with open(filename, 'w') as f:
            f.write(" ".join(lines))


if __name__ == "__main__":
    print("Parse")
    parser = Parser('test.txt')
    parser.export(parser.parse(), 'formatted.txt')
    # print(parser.parse())

    # print(" ".join(parser.parse()))

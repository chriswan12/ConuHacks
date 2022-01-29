
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
                if line == '\n' or not line or not line.startswith('Sanja Fider: '):
                    continue

                formatted_line = self._strip_user(line.rstrip('\n'))

                lines.append(formatted_line)
        return lines

    @staticmethod
    def _strip_user(text):
        for i in range(len(text)):
            if text[i] == ':':
                return text[i+2:]


if __name__ == "__main__":
    print("Parse")
    parser = Parser('test.txt')
    print(parser.parse())

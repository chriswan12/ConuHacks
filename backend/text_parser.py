
class Parser:
    def __init__(self, file_path, speaker=None):
        self.file_path = file_path
        self.speaker = speaker

    def parse(self):
        lines = []
        with open(self.file_path) as f:
            line = f.readline()

            lines.append(self._strip_user(line.rstrip('\n')))
            while line:
                line = f.readline()
                # Have to change the lecture name

                # for zoom meetings with speaker
                if self.speaker:
                    if line == '\n' or not line or not line.startswith(self.speaker + ': '):
                        continue
                elif not self.speaker:
                    if line == '\n' or not line:
                        continue
                formatted_line = self._strip_user(line.rstrip('\n'))

                lines.append(formatted_line)
        return " ".join(lines)

    @staticmethod
    def _strip_user(text):
        for i in range(len(text)):
            if text[i] == ':':
                return text[i+2:]
        return text

    @staticmethod
    def export(text, filename):
        with open(filename, 'w') as f:
            f.write(text)


if __name__ == "__main__":
    print("Parse")
    parser = Parser('test.txt', 'Sanja Fidler')
    parser.export(parser.parse(), 'formatted.txt')


class Emitter:
    def __init__(self, fullPath):
        self.fullPath = fullPath
        self.header = ""
        self.code = ""
        self.indent_level = 0  # To manage indentation

    def emit(self, code):
        self.code += self._indent(code)

    def emitLine(self, code):
        self.code += self._indent(code) + '\n'

    def headerLine(self, code):
        self.header += code + '\n'

    def _indent(self, code):
        return '    ' * self.indent_level + code

    def writeFile(self):
        try:
            with open(self.fullPath, 'w') as outputFile:
                outputFile.write(self.header + self.code)
        except Exception as e:
            print(f"Error writing to file {self.fullPath}: {e}")

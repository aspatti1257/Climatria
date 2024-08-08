
# Relies on a credentials.txt file being at the specified directory. Format:
# username=<USERNAME>
# password=<PASSWORD>
# returns the fully parsed username/pw as a tuple.
class CredentialParser:

    def __init__(self, directory):
        self.__directory = directory

    def fetch_credentials(self) -> tuple:
        input_file = open(self.__directory)
        return tuple([line.split("=")[1].strip() for line in input_file.readlines()])


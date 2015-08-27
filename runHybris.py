import os, sys, getpass, subprocess, ConfigParser, StringIO


class ControlProps:
    @staticmethod
    def read_properties_file(file_path):
        with open(file_path) as f:
            config = StringIO.StringIO()
            config.write('[dummy_section]\n')
            config.write(f.read())
            config.seek(0, os.SEEK_SET)

            cp = ConfigParser.SafeConfigParser()
            cp.readfp(config)

        return dict(cp.items('dummy_section'))


class Hybris:
    folder = ""
    insts = []
    version = 0
    debug = False

    # List all directories in a folder
    @staticmethod
    def listHybrisInstalations():
        dirs = os.listdir(Hybris.folder)
        lst = []
        count = 0

        for file in dirs:
            if (file != ".DS_Store"):
                count = count + 1
                lst.append(file)
                print (str(count) + ' - ' + file)

        Hybris.insts = lst

        return lst

    @staticmethod
    def callHybris():
        # Prepare shell command to be executed
        if Hybris.debug:
            command = Hybris.folder + "/" + str(
                Hybris.insts[Hybris.version - 1]) + "/hybris/bin/platform/./hybrisserver.sh debug"
        else:
            command = Hybris.folder + "/" + str(
                Hybris.insts[Hybris.version - 1]) + "/hybris/bin/platform/./hybrisserver.sh"
            print "Starting hybris from command: " + command

        subprocess.call([command], shell=True)

        return None


class ConsoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == '__main__':
    # Start console with default color
    print ConsoleColors.ENDC

    # Get current folder and load properties file
    props = ControlProps.read_properties_file(os.path.dirname(os.path.realpath(__file__)) + '/config.properties')

    try:
        checkCowsay = subprocess.call("cowsay Hi $USER! Lets play hybris...", shell=True)

        if (checkCowsay != 0):
            cowsayInstall = raw_input("Wanna install cowsay? Just install, it s cool! [yes] or no: ")

            if cowsayInstall.lower() in {"y", "yes", "yea", "yeah", "si", "go", "aye", "sure", "ja", "sim", ""}:
                subprocess.call("sudo gem install cowsay", shell=True)

    except:
        pass

    # Request an specific folder, otherwise get the default one.
    Hybris.folder = raw_input(
        "Please enter the folder where hybris installations are located: \n[Default: " + props['yfolder'] + "]\n")
    if (Hybris.folder == ""):
        Hybris.folder = props['yfolder']

    Hybris.listHybrisInstalations()
    Hybris.version = input("Which hybris version you wanna run? ")

    # Check if debug mode is necessary
    try:
        if (str(sys.argv[1]) == "debug"):
            Hybris.debug = True

    except IndexError:
        print ConsoleColors.WARNING + "WARNING:\nError handling arguments. Don't worry, keep going..."
        print ConsoleColors.ENDC

        yn = raw_input("Wanna debug? Please enter 'Yes' or 'No': [Default=No] ")

        if yn.lower() in {"y", "yes", "yea", "yeah", "si", "go", "aye", "sure", "ja", "sim"}:
            Hybris.debug = True
        else:
            print ConsoleColors.BOLD + "Debug set to false!"
            Hybris.debug = False
            print ConsoleColors.ENDC

        Hybris.callHybris()

    else:
        Hybris.callHybris()

    # End app with default color
    print ConsoleColors.ENDC

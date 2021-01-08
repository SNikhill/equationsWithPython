try:
    from PyInquirer import prompt
    from os import scandir
except ImportError:
    print("Importation error")
    exit()


def scan_dir(path_to_dir: str) -> object:
    """The purpose of this function is to scan a passed in directory.

    :param path_to_dir: Path to the directory that is to be scanned
    :return: Iterator of DirEntry Object. Basically, an object that
    holds the details of all the contents in the directory whose path
    was passed in.
    """
    files = scandir(path_to_dir)
    return files


def find_program_files(path_to_dir: str) -> dict:
    """The purpose of the function is to scan the passed in directory
    for program files that is, the files that are meant to be computed.

    :param path_to_dir: Path to the directory where the programs are to be searched
    :return: A dictionary with Display Name of the program as key and the path to the program as Value
    """
    all_files = scan_dir(path_to_dir)
    programs = {}
    for file in all_files:
        if not file.is_dir() and file.name.endswith(".py") and file.name != "main.py":
            programs[file.name.replace(".py", "").replace("-", " ")] = file.name

    return programs


def prompt_user(available_programs: list) -> dict:
    """The purpose of this function is to prompt the user with the
    available programs.

   :param available_programs: A list with the names of all the available programs
   :return: A dictionary with the answer of the user as Value
   """
    questions = [
        {
            'type': 'list',
            'name': 'program_to_run',
            'message': 'Please, Select the Program that you want to Compute',
            'choices': available_programs
        }
    ]
    answers = prompt(questions)
    return answers


def execute_program(name_of_program: str):
    """The purpose of this function is to execute the program
    that the user has selected.

    :param name_of_program: Name of the program that is to be run
    :return:
    """
    try:
        print(name_of_program)
        __import__(name_of_program)
        exec(name_of_program)
    except ModuleNotFoundError:
        print("Sorry but, it seems like the desired program is currently not available")
        exit()
    except ImportError:
        print("Sorry but, the program could not run at the moment")
        exit()
    except RuntimeError:
        print("Sorry buy, the program could not run at the moment")
        exit()


def initiate_sequence(path_to_dir: str):
    """The purpose of this function is to initiate the sequence
    that is, to start the execution of this program (equationWithPython).

    :param path_to_dir: Path to the directory that is holding all of the programs
    :return:
    """
    available_programs_details = find_program_files(path_to_dir)
    answer_of_user = prompt_user([*available_programs_details])['program_to_run']
    execute_program(available_programs_details[answer_of_user])


initiate_sequence(".")

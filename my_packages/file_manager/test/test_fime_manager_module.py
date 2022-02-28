from my_packages.file_manager import file_manager_module
from my_packages.file_manager.file_manager_module import FileManagerModule

testFolder = 'tests'

def test_init_instance_with_folder():
    file_manager = FileManagerModule(testFolder)
    assert file_manager.working_directory != ''

def test_init_instance_without_folder():
    file_manager = FileManagerModule('')
    assert file_manager.working_directory != ''

def test_dir_exist():
    file_manager = FileManagerModule('')
    assert file_manager.dirExist()

def test_dir_exist():
    file_manager = FileManagerModule(testFolder)
    assert file_manager.dirExist('non-existing-dir') == False

def test_create_folder():
    file_manager = FileManagerModule(testFolder)
    assert file_manager.dirCreate('pytest-folder')
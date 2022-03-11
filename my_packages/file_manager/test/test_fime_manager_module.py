from my_packages.file_manager import file_manager_module
from my_packages.file_manager.file_manager_module import FileManagerModule

test_folder = 'tests'
common_file_manager = FileManagerModule(test_folder)

def test_init_instance_with_folder():
    assert common_file_manager.working_directory != ''

def test_init_instance_without_folder():
    file_manager = FileManagerModule('')
    assert file_manager.working_directory != ''

def test_dir_exist():
    file_manager = FileManagerModule('')
    assert file_manager.dirExist(test_folder)

def test_dir_non_exist():
    assert common_file_manager.dirExist('non-existing-dir') == False

def test_create_folder():
    assert common_file_manager.dirCreate('pytest-folder')

def test_get_dir_content():
    common_file_manager.fileWrite('test_dir_content_1.txt','Test 1\n')
    common_file_manager.fileWrite('test_dir_content_2.txt','Test 2\n')
    common_file_manager.fileWrite('test_dir_content_3.txt','Test 3\n')
    content = common_file_manager.dirGetContent()
    assert len(content) > 0

def test_create_file():
    assert common_file_manager.fileWrite('text.txt','Test text!\n')

def test_file_exist():
    file_name = 'empty-text.txt'
    common_file_manager.fileWrite(file_name,'')
    assert common_file_manager.fileExist(file_name)

def test_file_not_exist():
    assert common_file_manager.fileExist('not-existing.file.txt') == False

def test_get_file_content():

    file_name = 'file-to-get-content.txt'

    common_file_manager.fileWrite(file_name,'This is a text,\n')
    common_file_manager.fileWrite(file_name,'this is another text\n')
    common_file_manager.fileWrite(file_name,'and this is the end!\n')

    file_content = common_file_manager.fileGetContent(file_name)

    assert len(file_content) > 0 and isinstance(file_content , str)

def test_get_file_content_as_list():

    file_name = 'file-to-get-content-as-list.txt'

    common_file_manager.fileWrite(file_name,'1\n')
    common_file_manager.fileWrite(file_name,'2\n')
    common_file_manager.fileWrite(file_name,'3\n')

    file_content = common_file_manager.fileGetContent(file_name , True)

    assert len(file_content) > 0 and isinstance(file_content , list)

def test_file_copy():

    origin_file = 'origin-file.txt'
    destiny_file = 'destiny-file.txt'
    file_content = 'This is the content of origin file'

    common_file_manager.fileWrite(origin_file,file_content)
    common_file_manager.fileCopy(origin_file , destiny_file)
    assert common_file_manager.fileExist(origin_file) and common_file_manager.fileExist(destiny_file)
    assert common_file_manager.fileGetContent(origin_file) == common_file_manager.fileGetContent(destiny_file)
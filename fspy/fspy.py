"""Main module."""


class FileSystem():

    def __init__(self) -> None:
        self.current_directory = self.Directory("", "/", None)

    class FSNode:

        def __init__(self, name: str, path: str, parent):
            self.name = name
            self.path = path
            self.parent = parent

    class Directory(FSNode):

        def __init__(self, name: str, path: str, parent):
            super().__init__(name, path, parent)
            self.children = {}

        def find_fs_node(self, fs_node_name: str, node_paths):
            for child_node_name in self.children.keys():
                child = self.children[child_node_name]
                if child_node_name == fs_node_name:
                    node_paths.append(self.children[child_node_name].path)
                if hasattr(child, 'children'):
                    child.find_fs_node(fs_node_name, node_paths)

    class File(FSNode):

        def __init__(self, name: str, path: str, parent):
            super().__init__(name, path, parent)
            self.contents = None

        def print_contents(self) -> None:
            print(self.contents)

    def make_directory(self, new_d_name: str) -> None:
        new_path = self.current_directory.path + new_d_name + "/"
        new_d = self.Directory(new_d_name, new_path, self.current_directory)
        self.current_directory.children[new_d_name] = new_d

    def move_up_one_directory(self, dir_name: str) -> None:
        self.current_directory = self.current_directory.children[dir_name]

    def move_to_parent(self) -> None:
        if self.current_directory.path != "/":
            self.current_directory = self.current_directory.parent

    def delete_directory(self, d_name: str) -> None:
        del self.current_directory.children[d_name]

    def make_file(self, file_name: str) -> None:
        new_path = self.current_directory.path + file_name + "/"
        new_file = self.File(file_name, new_path, self.current_directory)
        self.current_directory.children[file_name] = new_file

    def delete_file(self, file_name: str) -> None:
        del self.current_directory.children[file_name]

    def move_file(self, file_name: str, d_name: str):
        moving_file = self.current_directory.children[file_name]
        source_dir = self.current_directory.children[d_name]
        source_dir.children[file_name] = moving_file.copy()
        self.delete_file(file_name)

    def find_fs_node(self, fs_node_name: str) -> list:
        node_paths = []
        self.current_directory.find_fs_node(fs_node_name, node_paths)
        return node_paths

    def write_to_file(self, file_name: str, file_contents):
        given_file = self.current_directory.children[file_name]
        given_file.contents = file_contents

    def read_from_file(self, file_name: str):
        test_file = self.current_directory.children['test.txt']
        return test_file.contents

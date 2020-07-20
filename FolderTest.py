import os


class FolderTest:
    def message(self):
        file_list = ['C:/test1/', 'C:/test1/']
        files_list = []
        for file_path in file_list:
            files_list.extend(self.folderToAbsFlePath(file_path))
        print(files_list)

    def folderToAbsFlePath(self, folder):
        files_list = []
        if os.path.isdir(folder):
            for content in os.walk(folder):
                for contentAt2 in content[2]:
                    files_list.append(os.path.join(content[0], contentAt2)
                                      .replace('\\', '/'))
        else:
            files_list.append(folder)
        return files_list


def main():
    folderTest = FolderTest()
    folderTest.message()


if __name__ == '__main__':
    main()

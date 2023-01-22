# Command line for the win

- Your first challenge is to print "hello world" on the terminal in a single command.

  - `echo 'hello world'`

* Print the current working directory.

  - `pwd`

* List names of all the files in the current directory, one file per line.

  - `ls`

* There is a file named access.log in the current directory. Print the contents.

  - `cat access.log`

* Print the last 5 lines of "access.log".

  - `cat access.log | tail -n 5`

* Create an empty file named take-the-command-challenge in the current working directory.

  - `touch take-the-command-challenge`

* Create a directory named tmp/files in the current working directory

  - `mkdir -p tmp/files`

* Copy the file named take-the-command-challenge to the directory tmp/files

  - `cp take-the-command-challenge tmp/files`

* Move the file named take-the-command-challenge to the directory tmp/files

  - `mv take-the-command-challenge tmp/files`

* A symbolic link is a type of file that is a reference to another file.

  Create a symbolic link named take-the-command-challenge that points to the file tmp/files/take-the-command-challenge.

  - `ln -s tmp/files/take-the-command-challenge take-the-command-challenge`

* Delete all of the files in this challenge directory including all subdirectories and their contents.
  Hint: There are files and directories that start with a dot ".", "rm -rf \*" won't work here!

  - `rm -r * .*`

* There are files in this challenge with different file extensions. Remove all files with the .doc extension recursively in the current working directory.

  - `rm **/*.doc`

* There is a file named access.log in the current working directory. Print all lines in this file that contains the string "GET".

  * `cat access.log | grep "GET"`

* Print all files in the current directory, one per line (not the path, just the filename) that contain the string "500".`

  - `ls | grep -lR "500"`

- Print the relative file paths, one path per line for all filenames that start with "access.log" in the current directory.

  - `ls -r access.log*`

- Print all matching lines (without the filename or the file path) in all files under the current directory that start with "access.log" that contain the string "500".

  Note that there are no files named access.log in the current directory, you will need to search recursively.

  - `ls | grep -rh 500`

- Extract all IP addresses from files that start with "access.log" printing one IP address per line.

  - `grep -ro ^[0-9.]*`

- Count the number of files in the current working directory. Print the number of files as a single integer.

  - `find . -type f| wc -l `

- Print the number of lines in access.log that contain the string "GET".

  - `cat "access.log" | grep "GET" | wc -l`

- The file split-me.txt contains a list of numbers separated by a ; character. Split the numbers on the ; character, one number per line.

  - `cat split-me.txt | tr ";" "\n"`

- Print the numbers 1 to 100 separated by spaces.

  - `echo {1..100}`

- This challenge has text files (with a .txt extension) that contain the phrase "challenges are difficult". Delete this phrase from all text files recursively.

  Note that some files are in subdirectories so you will need to search for them.

  - `sed -i "challenges are difficult" **/*.txt`

- The file sum-me.txt has a list of numbers, one per line. Print the sum of these numbers.

  - `awk '{s=s+$1}END{print s}' sum-me.txt`

- Print all files in the current directory recursively without the leading directory path.

  - `find . -type f -printf "%f\n"`

- Rename all files removing the extension from them in the current directory recursively.

  - `mv * .*`

- The files in this challenge contain spaces. List all of the files (filenames only) in the current directory but replace all spaces with a '.' character.

  - `ls | sed 's/\ /\./g' `

- In this challenge there are some directories containing files with different extensions. Print all directories, one per line without duplicates that contain one or more files with a ".tf" extension.

  - `dirname **/*tf | sort -u`

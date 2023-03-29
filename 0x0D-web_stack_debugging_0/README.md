# 0x0D. Web stack debugging #0
This is the first debugging series, and I have given a broken/bugged webstacks, the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, I've learned how to figure out what is going on and fix it manually.

## Task
[0-give_me_a_page](https://github.com/Bantamlak12/alx-system_engineering-devops/blob/master/0x0D-web_stack_debugging_0/0-give_me_a_page): In this first debugging project, I run Apache on the container to return a page containing `Hello Holberton` when querying the root of it.

To install the docker container `docker run -p 8080:80 -d -it holbertonschool/265-0`

To see running docker processes `docker ps`

To run the docker container `docker exec -ti 76f44c0da25e /bin/bash`

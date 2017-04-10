#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# C LANGUAGE create temp/notes.txt
# 

def ft_create_notes_manual():
	show_header_menu("C language: create notes.txt")
	ft_create_notes("")
	raw_input("\npress ENTER")

def ft_create_notes(project_path):
	if len(project_path) > 0:
		main_folder = project_path + "/temp"
		ft_create_folder(main_folder)
		name = main_folder + "/" + "notes.txt"
	else:
		main_folder = os.getcwd() + "/temp"
		ft_create_folder(main_folder)
		name = main_folder + "/" + "notes.txt"
	if ft_create_file(name) == True:
		f = open(name, "a+")
		f.write("notes...\n")
		f.close()
		if len(project_path) > 0:
			print project_path + "/" + "notes.txt" + " created"
		else:
			print name + " created"
	else:
		print name, "file alredy exist"

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# C LANGUAGE create main.c
# 

def ft_create_main_manual():
	show_header_menu("C language: create main.c")
	ft_create_main("")
	raw_input("\npress ENTER")

def ft_create_main(project_path):
	if len(project_path) > 0:
		main_folder = project_path + "/src/project"
		ft_create_folder(main_folder)
		name = main_folder + "/" + "main.c"
	else:
		name = 'main.c'
	if ft_create_file(name) == True:
		f = open(name, "a+")
		f.write(
'''/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: akalmyko <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/03/17 17:44:18 by akalmyko          #+#    #+#             */
/*   Updated: 2017/03/17 18:02:48 by akalmyko         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../lib/libft/libft.h"

int\tmain(void)
{
\tft_printf("fly, bird, fly!\\n");
\treturn (0);
}
''')
		f.close()
		if len(project_path) > 0:
			print project_path + "/" + "main.c" + " created"
		else:
			prj_path = os.getcwd()
			print str(prj_path) + "/" + name + " created"
	else:
		print name, "file alredy exist"


#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# C LANGUAGE create Makefile
# 

def ft_create_makefile_manual():
	show_header_menu("C language: create Makefile")
	ft_create_makefile("")
	raw_input("\npress ENTER")

def ft_create_makefile(project_path):
	if len(project_path) > 0:
		name = project_path + "/" + "Makefile"
	else:
		name = 'Makefile'
	if ft_create_file(name) == True:
		f = open(name, "a+")
		f.write(
'''# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    birds                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalmyko <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/03/17 22:34:25 by akalmyko          #+#    #+#              #
#    Updated: 2017/03/17 22:34:35 by akalmyko         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

.PHONY: all clean fclean re

NAME = birds
SRCF = src/
PRJ = $(SRCF)project
LIBFT = $(SRCF)lib/
LIB = $(LIBFT)libft.a
CC = /usr/bin/gcc
FLAGS = -Wall -Wextra -Werror
RMF = /bin/rm -rf
CFILES = $(shell find $(PRJ) -name "*.c")
OFILES = $(CFILES:$(PRJ)/%.c=%.o)
GRN = \\033[1;32m
RED = \\033[1;31m
WHT = \\033[1;37m
CLN = \\033[m

all: $(NAME)

$(NAME):
	@make -C $(LIBFT)
	@echo "$(NAME) compiling... \c"
	@$(CC) $(FLAGS) $(CFILES) -c
	@$(CC) $(FLAGS) $(OFILES) $(LIB) -o $(NAME)
	@echo "$(GRN)created$(CLN)"

clean:
	@make -C $(LIBFT) clean
	@echo "$(NAME) cleaning... \c"
	@$(RMF) $(OFILES)
	@echo "$(WHT)cleaned$(CLN)"

fclean:
	@make -C $(LIBFT) fclean
	@echo "$(NAME) fcleaning... \c"
	@$(RMF) $(OFILES)
	@$(RMF) $(NAME)
	@echo "$(WHT)fcleaned$(CLN)"

re: fclean all

''')
		f.close()
		if len(project_path) > 0:
			print project_path + "/" + "Makefile" + " created"
		else:
			prj_path = os.getcwd()
			print str(prj_path) + "/" + name + " created"
	else:
		print name, "file alredy exist"

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# C LANGUAGE create .gitignore
# 

def ft_create_gitignore_manual():
	show_header_menu("C language: create .gitignore file")
	ft_create_gitignore("")
	raw_input("\npress ENTER")

def ft_create_gitignore(project_path):
	git = ".gitignore"
	if len(project_path) > 0:
		name = project_path + "/" + git
	else:
		name = git
	if ft_create_file(name) == True:
		print name, "created"
	else:
		print name, "already exist"

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# C LANGUAGE copy libft
# 

def ft_copy_libft_manual():
	default_path = "/nfs/2016/a/akalmyko/w/libft_last/"
	show_header_menu("C language: copy libft")
	while True:
		show_header_message("where is you libft files?")
		ft_option(0, "back to main menu")
		ft_option(1, "default path:" + default_path)
		ft_option(2, "set path")
		user_input = ft_input_number(2)
		if (user_input == 0):
			break
		elif (user_input == 1):
			ft_copy_libft(default_path, "")
			break
		elif (user_input == 2):
			print "input new path for libft"
			new_path = ft_input_string()
			if ft_copy_libft(new_path, "") == True:
				break
	raw_input("\npress ENTER")

def ft_copy_libft(libft_path, project_path):
	if len(libft_path) == 0:
		libft_path = "/nfs/2016/a/akalmyko/w/libft_last/"
	if not os.path.exists(libft_path):
		print "bad path"
		return False
	if len(project_path) > 0:
		dest = project_path + '/src/lib'
		shutil.copytree(libft_path, dest)
		print dest + "libft here"
	else:
		src_folder = os.getcwd() + '/src'
		if not os.path.exists(src_folder):
			ft_create_folder(src_folder)
			dest = os.getcwd() + '/src/lib'
			shutil.copytree(libft_path, dest)
		else:
			dest = os.getcwd() + '/src/lib'
			if os.path.exists(dest):
				print "libft already there"
			else:
				shutil.copytree(libft_path, dest)
				print dest + "libft here"
	return True

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# C LANGUAGE create src folder
# 

def ft_create_src_folder_manual():
	show_header_menu("C language: create /src folder")
	ft_create_src_folder("")
	raw_input("\npress ENTER")

def ft_create_src_folder(project_path):
		if len(project_path) > 0:
			name = project_path + "/src"
			text = name
		else:
			name = "src"
			prj_path = os.getcwd()
			text = str(prj_path) + "/" + name 
		if ft_create_folder(name) == True:
			print text + " created"
			return (text)
		else:
			print text, "alredy exist"

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# C LANGUAGE create author file
# 

def ft_create_author_file_manual():
	show_header_menu("C language: create author file")
	ft_create_author_file("")
	raw_input("\npress ENTER")

def ft_create_author_file(project_path):
	if len(project_path) > 0:
		name = project_path + "/" + "author"
	else:
		name = 'author'
	if ft_create_file(name) == True:
		f = open(name, "a+")
		f.write("akalmyko\n")
		f.close()
		if len(project_path) > 0:
			print project_path + "/" + "author" + " created"
		else:
			prj_path = os.getcwd()
			print str(prj_path) + "/" + name + " created"
	else:
		print name, "file alredy exist"

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# C LANGUAGE create the project folder
# 

def ft_create_project_folder_manual():
	show_header_menu("C language: create the project folder")
	show_header_message("input the folder name")
	ft_create_project_folder()
	raw_input("\npress ENTER")

def ft_create_project_folder():
	while True:
		name = ft_input_string()
		if ft_create_folder(name) == True:
			prj_path = os.getcwd()
			text = str(prj_path) + "/" + name 
			print text + " created"
			return (text)
		print name, "folder alredy exist, try another name"

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# C LANGUAGE automatic mode
# 

def ft_c_language_automatic():
	
	print "enter project name"
	project_path = ft_create_project_folder()
	ft_create_author_file(project_path)
	ft_create_src_folder(project_path)
	ft_copy_libft("", project_path)
	ft_create_gitignore(project_path)
	ft_create_makefile(project_path)
	ft_create_main(project_path)
	ft_create_notes(project_path)
	raw_input("\npress ENTER")

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# C LANGUAGE MENU
# 

def ft_c_language_menu():
	show_header_menu("C language")
	ft_option(0, "back to the main menu")
	ft_option(1, "automatic mode, with all steps")
	ft_option(2, "create the project folder")
	ft_option(3, "create author file")
	ft_option(4, "create src folder")
	ft_option(5, "copy libft to src/lib")
	ft_option(6, "create main.c")
	ft_option(7, "create Makefile")
	ft_option(8, "create temp/notes.txt")
	ft_option(9, "create .gitignore")

def ft_c_language():
	arguments = 9
	while True:
		ft_c_language_menu()
		user_input = ft_input_number(arguments)
		if (user_input == 0):
			break
		elif (user_input == 1):
			ft_c_language_automatic()
		elif (user_input == 2):
			ft_create_project_folder_manual()
		elif (user_input == 3):
			ft_create_author_file_manual()
		elif (user_input == 4):
			ft_create_src_folder_manual()
		elif (user_input == 5):
			ft_copy_libft_manual()
		elif (user_input == 6):
			ft_create_main_manual()
		elif (user_input == 7):
			ft_create_makefile_manual()
		elif (user_input == 8):
			ft_create_notes_manual()
		elif (user_input == 9):
			ft_create_gitignore_manual()

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# BASH LANGUAGE create script.sh
# 

def ft_create_scriptsh_manual():
	show_header_menu("BASH language: create script.sh")
	ft_create_scriptsh("")
	raw_input("\npress ENTER")

def ft_create_scriptsh(project_path):
	script = "script.sh"
	if len(project_path) > 0:
		name = project_path + "/" + script
	else:
		name = script
	if ft_create_file(name) == True:
		print name, "created"
		f = open(name, "a+")
		f.write("#!/bin/zsh\n\n")
		f.close
	else:
		print name, "already exist"

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# PYTHON LANGUAGE create script.py
# 

def ft_create_scriptpy_manual():
	show_header_menu("Python language: create script.py")
	ft_create_scriptpy("")
	raw_input("\npress ENTER")

def ft_create_scriptpy(project_path):
	script = "script.py"
	if len(project_path) > 0:
		name = project_path + "/" + script
	else:
		name = script
	if ft_create_file(name) == True:
		print name, "created"
		f = open(name, "a+")
		f.write("#! /usr/bin/python\n# -*- coding: utf-8 -*-\n\n")
		f.close
	else:
		print name, "already exist"

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# create folder
# 

def ft_create_folder(name):
	if os.path.exists(name):
		return False
	else:
		os.makedirs(name)
		return True

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# create file
# 

def ft_create_file(name):
	if os.path.exists(name):
		return False
	else:
		f = open(name,"w+")
		f.close
		return True

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# USER INPUT and checker
# 

def ft_input_number(max_num):
	while True:
		if max_num > 0:
			text = '\nEnter your choice [0 - ' + str(max_num) + '] '
		else:
			text = '\nEnter your choice [0] '
		u_input = raw_input(text)
		if u_input.isdigit() and int(u_input, 10) >= 0 and int(u_input, 10) <= max_num:
			print ""
			break
		print "wrong input, try again"
	return (int(u_input, 10))

def ft_input_string():
	while True:
		u_input = raw_input("input here: ")
		if len(u_input) > 0:
			return (u_input)
		print "bad imput"

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# BASH MENU
# 

def ft_bash_language_menu():
		show_header_menu("BASH language")
		ft_option(0, "go to the main menu")
		ft_option(1, "create script.sh")

def ft_bash_language():
	while True:
		ft_bash_language_menu()
		user_input = ft_input_number(1)
		if (user_input == 0):
			break
		elif (user_input == 1):
			ft_create_scriptsh_manual()
#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# PYTHON MENU
#

def ft_python_language_menu():
	show_header_menu("Python language")
	ft_option(0, "go to the main menu")
	ft_option(1, "create script.py")

def ft_python_language():
	while True:
		ft_python_language_menu()
		user_input = ft_input_number(1)
		if (user_input == 0):
			break
		elif (user_input == 1):
			ft_create_scriptpy_manual()

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# MAIN MENU
#

def ft_choose_the_project_menu():
	show_header_menu("Main menu")
	show_header_message("In which language will the project be?")
	ft_option(0, "EXIT")
	ft_option(1, "C language")
	ft_option(2, "bash script")
	ft_option(3, "python language")

def ft_choose_the_project():
	while True:
		ft_choose_the_project_menu()
		user_input = ft_input_number(3)
		if (user_input == 0):
			print "bye bye then. exit"
			break
		elif (user_input == 1):
			ft_c_language()
		elif (user_input == 2):
			ft_bash_language()
		elif (user_input == 3):
			ft_python_language()

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# MENU headers
# 

def show_header_menu(name):
	os.system('clear')
	print "--------------------------------------------"
	print "   ", name
	print "--------------------------------------------\n"

def show_header_message(message):
	print message, "\n"

def ft_option(num, name):
	text = "[" + str(num) + "] " + name
	print text

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
# main method
#
		
def main():
	ft_choose_the_project()
	# exit(0)

if __name__ == "__main__":
    main()

#
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
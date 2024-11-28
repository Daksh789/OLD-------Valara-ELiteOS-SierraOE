import os
import shutil
import subprocess
import platform
from datetime import datetime


# Helper function to clear screen
def clear_screen() :
    os.system ( 'cls' if os.name == 'nt' else 'clear' )


# Custom Commands

# Show current date and time
def show_date() :
    current_time = datetime.now ( ).strftime ( "%Y-%m-%d %H:%M:%S" )
    print ( f"Current Date & Time: {current_time}" )


# Show system info (free memory, disk usage, etc.)
def show_info() :
    if platform.system ( ) == "Windows" :
        free_space = shutil.disk_usage ( "C:" ).free // (2 ** 30)
        print ( f"Free Space on C: {free_space} GB" )
        print (
            f"Available memory: {os.sysconf ( 'SC_PAGE_SIZE' ) * os.sysconf ( 'SC_PHYS_PAGES' ) / (1024. ** 3):.2f} GB"
            )
    else :
        disk = subprocess.check_output ( "df -h" , shell=True ).decode ( "utf-8" )
        memory = subprocess.check_output ( "free -h" , shell=True ).decode ( "utf-8" )
        print ( f"Disk Usage:\n{disk}\nMemory Usage:\n{memory}" )


# Show the terminal version
def show_version() :
    print ( "Custom Terminal Version: 1.1" )


# Show help for commands
def show_help() :
    print ( "\nAvailable Commands:" )
    print ( "1. ls/cd/mkdir/rm - Basic file operations" )
    print ( "2. copy/move      - File operations (Windows Mode)" )
    print ( "3. cp/mv/cat/pwd  - File operations (Bash Mode)" )
    print ( "4. echo           - Display messages" )
    print ( "5. clear          - Clear the terminal screen" )
    print ( "6. date           - Show current date and time" )
    print ( "7. info           - Show system info (disk usage, memory, etc.)" )
    print ( "8. version        - Show terminal version" )
    print ( "9. exit           - Exit the terminal" )
    print ( "10. help          - Display this help menu" )


# Windows (MSDOS) Commands
def windows_commands(command) :
    if command == "cls" :
        clear_screen ( )
    elif command == "dir" :
        print ( "\n".join ( os.listdir ( ) ) )
    elif command.startswith ( "del " ) :
        file = command.split ( " " )[ 1 ]
        try :
            os.remove ( file )
            print ( f"{file} deleted." )
        except FileNotFoundError :
            print ( f"{file} not found." )
    elif command.startswith ( "mkdir " ) :
        dirname = command.split ( " " )[ 1 ]
        os.makedirs ( dirname , exist_ok=True )
        print ( f"Directory {dirname} created." )
    elif command.startswith ( "copy " ) :
        src , dest = command.split ( " " )[ 1 ] , command.split ( " " )[ 2 ]
        shutil.copy ( src , dest )
        print ( f"Copied {src} to {dest}" )
    elif command.startswith ( "move " ) :
        src , dest = command.split ( " " )[ 1 ] , command.split ( " " )[ 2 ]
        shutil.move ( src , dest )
        print ( f"Moved {src} to {dest}" )
    elif command.startswith ( "type " ) :
        file = command.split ( " " )[ 1 ]
        try :
            with open ( file , 'r' ) as f :
                print ( f.read ( ) )
        except FileNotFoundError :
            print ( f"{file} not found." )
    elif command == "exit" :
        print ( "Exiting..." )
        return False
    elif command == "help" :
        show_help ( )
    elif command == "date" :
        show_date ( )
    elif command == "info" :
        show_info ( )
    elif command == "version" :
        show_version ( )
    else :
        print ( f"Unknown command: {command}" )
    return True


# Bash (Ubuntu/macOS) Commands
def bash_commands(command) :
    if command == "ls" :
        print ( "\n".join ( os.listdir ( ) ) )
    elif command.startswith ( "cd " ) :
        try :
            os.chdir ( command.split ( " " )[ 1 ] )
        except FileNotFoundError :
            print ( "Directory not found." )
    elif command.startswith ( "mkdir " ) :
        dirname = command.split ( " " )[ 1 ]
        os.makedirs ( dirname , exist_ok=True )
        print ( f"Directory {dirname} created." )
    elif command.startswith ( "rm " ) :
        file = command.split ( " " )[ 1 ]
        try :
            os.remove ( file )
            print ( f"{file} removed." )
        except FileNotFoundError :
            print ( f"{file} not found." )
    elif command.startswith ( "cp " ) :
        src , dest = command.split ( " " )[ 1 ] , command.split ( " " )[ 2 ]
        shutil.copy ( src , dest )
        print ( f"Copied {src} to {dest}" )
    elif command.startswith ( "mv " ) :
        src , dest = command.split ( " " )[ 1 ] , command.split ( " " )[ 2 ]
        shutil.move ( src , dest )
        print ( f"Moved {src} to {dest}" )
    elif command.startswith ( "cat " ) :
        file = command.split ( " " )[ 1 ]
        try :
            with open ( file , 'r' ) as f :
                print ( f.read ( ) )
        except FileNotFoundError :
            print ( f"{file} not found." )
    elif command == "pwd" :
        print ( os.getcwd ( ) )
    elif command == "clear" :
        clear_screen ( )
    elif command == "exit" :
        print ( "Exiting..." )
        return False
    elif command == "help" :
        show_help ( )
    elif command == "date" :
        show_date ( )
    elif command == "info" :
        show_info ( )
    elif command == "version" :
        show_version ( )
    else :
        print ( f"Unknown command: {command}" )
    return True


# Select terminal mode
def switch_mode() :
    print ( "Select terminal mode: " )
    print ( "1. Windows (MSDOS)" )
    print ( "2. Ubuntu/macOS (Bash)" )
    mode = input ( "Enter choice: " ).strip ( )

    if mode == "1" :
        return windows_commands
    elif mode == "2" :
        return bash_commands
    else :
        print ( "Invalid choice, defaulting to Bash." )
        return bash_commands


# Main terminal
def terminal() :
    clear_screen ( )
    print ( "===========================================" )
    print ( "             Custom Terminal               " )
    print ( "===========================================" )
    mode = switch_mode ( )
    print ( "Terminal started. Type 'exit' to quit." )

    while True :
        command = input ( f"{os.getcwd ( )}$ " ).strip ( )
        if not mode ( command ) :
            break


if __name__ == "__main__" :
    terminal ( )

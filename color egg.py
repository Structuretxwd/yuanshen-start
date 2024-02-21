import time

def display_loading_screen():
    print("**************************")
    print("*                        *")
    print("*         原神            *")
    print("*                        *")
    print("**************************")
    time.sleep(4)

def display_welcome_message():
    print("欢迎来到原神世界！")
    time.sleep(1)

def load_game():
    print("游戏加载中...")
    time.sleep(7)

def start_game():
    print("游戏启动中...")
    time.sleep(2)
    print("游戏已启动！")

def main():
    display_loading_screen()
    display_welcome_message()
    load_game()
    start_game()

if __name__ == "__main__":
    main()

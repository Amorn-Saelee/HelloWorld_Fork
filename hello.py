# ใช้ ANSI Escape Sequences สำหรับใส่สี (รองรับใน Terminal ส่วนใหญ่)
BLUE = '\033[94m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_ocean_scene():
    print(f"{BOLD}{CYAN}Hello World! Welcome to the Ocean.{RESET}\n")

    # ภาพเรือ (ปรับปรุงการจัดวาง)
    ship = f"""{YELLOW}
                |    |    |
               )_)  )_)  )_)
              )___))___))___)\\
             )____)____)_____)\\\\
           _____|____|____|____\\\\\\__
    {BLUE}------- \                   / ---------
      ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
        ^^^^      ^^^^     ^^^    ^^
              ^^^^      ^^^{RESET}
    """
    
    # ภาพประภาคาร (เพิ่มเข้าไปใหม่)
    lighthouse = f"""{YELLOW}
             |\\
            /  \\
           |____|
           |    |
           | [ ]| {RESET}{BOLD}* Lighting the way...{RESET}{YELLOW}
           |    |
          /______\\
         |________|
    """

    print(ship)
    print("-" * 40)
    print(lighthouse)

if __name__ == "__main__":
    print_ocean_scene()
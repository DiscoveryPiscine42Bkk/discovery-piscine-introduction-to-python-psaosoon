import sys

def main():
    if len(sys.argv) != 3:
        print("none")
        return
    
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        # +1 เพื่อรวม end ด้วย
        print(list(range(start, end + 1)))
    except ValueError:
        # กรณีมีคนใส่ค่าที่ไม่ใช่ตัวเลข เช่น 'a'
        print("none")

if __name__ == "__main__":
    main()
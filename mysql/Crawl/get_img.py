import requests
import processBook

processBook.getBooks()
all_book = processBook.all_book

# 获取所有书本的图片
def getImg():
    already = []
    id = 0
    for book in all_book:
        if book['title'] not in already:
            url = book['img']  # 获取图片的地址
            img_content = requests.get(url).content  # 获取图片二进制数据
            img_path = "./img/" + f"{id}" + ".jpg"
            with open(img_path, "wb") as f:
                f.write(img_content)
            id += 1
            already.append(book['title'])

if __name__ == "__main__":
    getImg()

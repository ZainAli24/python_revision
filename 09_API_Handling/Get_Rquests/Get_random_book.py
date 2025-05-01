import requests

def fetch_random_book():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        book_description  = data["data"]["volumeInfo"]["description"]
        book_tumbnail  = data["data"]["volumeInfo"]["imageLinks"]["smallThumbnail"]
        PDFs  = data["data"]["accessInfo"]["pdf"]["acsTokenLink"]

        return [book_description, book_tumbnail, PDFs]
    else:
        raise Exception("Sorry! Failed to fetch Book Data.")
    

def main():
    try:
        lists = fetch_random_book()
        print(f"Book Description is: {lists[0]} \n\n\n Book Tumbnail is: {lists[1]} \n\n\n And PDF is : {lists[2]}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()


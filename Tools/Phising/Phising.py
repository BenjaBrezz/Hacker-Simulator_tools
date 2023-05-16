import pytesseract
from PIL import Image

interests = {
    "Family and Relationships": ['Dating', 'Family', 'Fatherhood', 'Friendship', 'Marriage', 'Motherhood', 'Parenting', 'Weddings'],
    "Shopping and Fashion": ['Clothing', 'Cosmetics', 'Coupons', 'Dresses', 'Fragrances', 'Handbags', 'Jewelry', 'Malls', 'Shoes', 'Sunglasses', 'Tattoos', 'Toys'],
    'Food and Drink': ['Baking', 'Barbecue', 'Beer', 'Chocolate', 'Coffee', 'Coffeehouses', 'Desserts', 'Juice', 'Pizza', 'Recipes', 'Tea', 'Veganism', 'Wine'],
    "Business": ['Advertising', 'Agriculture', 'Architecture', 'Aviation', 'Banking', 'Business', 'Construction', 'Design', 'Economics', 'Engineering', 'Design', 'Entrepreneurship', 'Finance', 'Investment', 'Insurance', 'Management', 'Marketing', 'Online', 'Retail', 'Sales', 'Science'],
    "Entertainment": ['Bars', 'Books', 'Comics', 'Concerts', 'Dancehalls', 'Documentary', 'Festivals', 'Games', 'Literature', 'Magazines', 'Manga', 'Movies', 'Music', 'Newspapers', 'Nightclubs', 'Parties', 'Plays', 'Poker', 'Talkshows', 'Theatre']
}

def process_image():
    file_path = input("Enter the image file path: ")
    image = Image.open(file_path)

    text = pytesseract.image_to_string(image)
    print('OCR Result:', text)

    category = find_most_repeated_category(text)
    print('Category with the most repetitions:', category)

def find_most_repeated_category(text):
    if not isinstance(text, str):
        print('Invalid input: text must be a string')
        return None  # or handle the error appropriately

    category_counts = {}

    for category, keywords in interests.items():
        count = 0

        for keyword in keywords:
            count += text.lower().count(keyword.lower())

        category_counts[category] = count

    most_repeated_category = max(category_counts, key=category_counts.get)
    return most_repeated_category

process_image()

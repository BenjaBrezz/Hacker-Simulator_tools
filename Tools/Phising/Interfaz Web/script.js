// Inicia Tesseract.js
const { createWorker } = Tesseract;
const worker = createWorker({
    logger: m => console.log(m),
});

const interests = {
    "Family and Relationships": ['Dating', 'Family', 'Fatherhood', 'Friendship', 'Marriage', 'Motherhood', 'Parenting', 'Weddings'],
    "Shopping and Fashion": ['Clothing', 'Cosmetics', 'Coupons', 'Dresses', 'Fragrances', 'Handbags', 'Jewelry', 'Malls', 'Shoes', 'Sunglasses', 'Tattoos', 'Toys'],
    'Food and Drink': ['Baking', 'Barbecue', 'Beer', 'Chocolate', 'Coffee', 'Coffeehouses', 'Desserts', 'Juice', 'Pizza', 'Recipes', 'Tea', 'Veganism', 'Wine'],
    "Business": ['Advertising', 'Agriculture', 'Architecture', 'Aviation', 'Banking', 'Business', 'Construction', 'Design', 'Economics', 'Engineering', 'Design', 'Entrepreneurship', 'Finance', 'Investment', 'Insurance', 'Management', 'Marketing', 'Online', 'Retail', 'Sales', 'Science'],
    "Entertainment": ['Bars', 'Books', 'Comics', 'Concerts', 'Dancehalls', 'Documentary', 'Festivals', 'Games', 'Literature', 'Magazines', 'Manga', 'Movies', 'Music', 'Newspapers', 'Nightclubs', 'Parties', 'Plays', 'Poker', 'Talkshows', 'Theatre']
};

function processImage() {
    var input = document.getElementById('imageInput');
    var file = input.files[0];
    var reader = new FileReader();

    reader.onload = function (e) {
        var image = new Image();
        image.src = e.target.result;

        image.onload = function () {
            Tesseract.recognize(image)
                .then(({ data: { text } }) => {
                    console.log('OCR Result:', text);

                    // Llame a la función para encontrar la categoría más repetida
                    var category = findMostRepeatedCategory(text);

                    // Mostrar el resultado en la página
                    var resultElement = document.getElementById("result");
                    resultElement.textContent = "Interés: " + category;
                })
                .catch(error => {
                    console.error('Error durante el proceso de OCR:', error);
                });
        };

        image.onerror = function () {
            console.log("Error al cargar la imagen");
        };
    };

    reader.readAsDataURL(file);
}

function findMostRepeatedCategory(text) {
    if (typeof text !== 'string') {
        console.error('Entrada no válida: el texto debe ser una cadena');
        return null; // o gestiona el error de forma adecuada
    }

    var categoryCounts = {};

    for (var category in interests) {
        var keywords = interests[category];
        var count = 0;

        for (var i = 0; i < keywords.length; i++) {
            var keyword = keywords[i];
            var regex = new RegExp(keyword, 'gi'); // Actualiza el patrón de expresión regular

            var matches = text.match(regex);

            if (matches) {
                count += matches.length;
            }
        }

        categoryCounts[category] = count;
    }

    var mostRepeatedCategory = Object.keys(categoryCounts).reduce(function (a, b) {
        return category
        Counts[a] > categoryCounts[b] ? a : b;
    });
    return mostRepeatedCategory;
}

// Esperar a que el documento termine de cargarse
document.addEventListener('DOMContentLoaded', function () {
    var imageInput = document.getElementById('imageInput');
    imageInput.addEventListener('change', processImage);
});


// Obtener elementos del DOM
const inputLabel = document.getElementById('inputLabel');
const decryptButton = document.getElementById('decryptButton');
const resultElement = document.getElementById('result');
const languageSelectLabel = document.getElementById('languageSelectLabel');
const inputElement = document.getElementById('input');
const languageSelect = document.getElementById('languageSelect');

// Objeto de traducción
const translations = {
  English: {
    inputLabel: 'Encrypted String:',
    inputPlaceholder: 'Enter the encrypted string...',
    decryptButton: 'Decrypt',
    languageSelectLabel: 'Select Language:',
    resultCopied: 'Copied to clipboard! ',
    resultNoMatch: 'Nothing copied to clipboard. No matches.',
  },
  Español: {
    inputLabel: 'Cadena Cifrada:',
    inputPlaceholder: 'Ingresa la cadena cifrada...',
    decryptButton: 'Descifrar',
    languageSelectLabel: 'Seleccionar Idioma:',
    resultCopied: '¡Copiado en el portapapeles!',
    resultNoMatch: 'No se ha copiado NADA en el portapapeles. No hay coincidencias.',
  },
};

// Función para cambiar el idioma
function setLanguage(selectedLanguage) {
  const translation = translations[selectedLanguage];

  // Actualizar textos
  inputLabel.textContent = translation.inputLabel;
  inputElement.placeholder = translation.inputPlaceholder;
  decryptButton.textContent = translation.decryptButton;
  languageSelectLabel.textContent = translation.languageSelectLabel;

  // Limpiar resultado
  resultElement.textContent = '';

  // Actualizar atributo lang en el select
  languageSelect.setAttribute('lang', selectedLanguage);
}

// Evento de cambio de idioma
languageSelect.addEventListener('change', function () {
  const selectedLanguage = this.value;
  setLanguage(selectedLanguage);
});

// Función de descifrado
function decrypt() {
  const string = inputElement.value;
  let output = '';
  const arr = string.split(':');
  for (const arrObj of arr) {
    if (
      arrObj.split('').every((c) => c.match(/\d/) || c.toUpperCase().match(/[ABCDEF]/))
    ) {
      output += arrObj + ':';
    }
  }
  if (output) {
    output = output.slice(0, -1);
    navigator.clipboard.writeText(output);
    resultElement.textContent = translations[languageSelect.value].resultCopied + output;
  } else {
    resultElement.textContent =
      translations[languageSelect.value].resultNoMatch;
  }
  inputElement.value = '';
}

// Evento de clic en el botón
decryptButton.addEventListener('click', decrypt);

document.addEventListener('DOMContentLoaded', function () {
    
    //Filtro nombre de perfume 
    document.getElementById('product_search').addEventListener('input', function() {
        const searchTerm = this.value.toLowerCase(); 
        const products = document.querySelectorAll('.parfum_card');

        products.forEach(function(product) {
            const productName = product.querySelector('h3').textContent.toLowerCase();

            if (productName.includes(searchTerm) ) {
                product.style.display = 'flex'; 
            } else {
                product.style.display = 'none'; 
            }
        });
    });
    // ---------------------------------
    
    // Filtro por notas
    const noteCards = document.querySelectorAll('.notes_card');

        // Añadir evento 'click' a cada tarjeta de nota
    noteCards.forEach(noteCard => {
        noteCard.addEventListener('click', function () {
            const noteName = this.querySelector('p').innerText.trim();
            filterByNote(noteName);
        });
    });

        // Función para filtrar fragancias según la nota seleccionada
    function filterByNote(noteName) {
        // Obtener todas las tarjetas de fragancias
        const fragranceCards = document.querySelectorAll('.parfum_card');

        fragranceCards.forEach(card => {
            // Obtener los datos de las notas desde los atributos data-*
            const topNotes = card.getAttribute('data-top-notes').split(',');
            const middleNotes = card.getAttribute('data-middle-notes').split(',');
            const baseNotes = card.getAttribute('data-base-notes').split(',');

            // Verificar si la nota seleccionada está presente en alguna de las categorías
            if (topNotes.includes(noteName) || middleNotes.includes(noteName) || baseNotes.includes(noteName)) {
                card.style.display = 'flex';  // Mostrar la tarjeta si coincide con la nota
            } else {
                card.style.display = 'none';  // Ocultar la tarjeta si no coincide
            }
        });
    }

    
    //Filtro por time

    const timeOfDayContainer = document.querySelectorAll('.time_of_day_container')
    
    //Evento clic para cada tarjeta de time of day
    timeOfDayContainer.forEach(timeCard => {
        timeCard.addEventListener('click', function () {
            filterByTime(timeCard);
        });
    });

    //Filtrado por time
    function filterByTime(timeCard) {
        const selectedTime = timeCard.getAttribute('data-time').toLowerCase().trim(); // Convertir a minúsculas y quitar espacios adicionales
        const fragranceCards = document.querySelectorAll('.parfum_card');
        
        fragranceCards.forEach(card => {
            const time = card.getAttribute('data-time').toLowerCase().trim(); // Convertir a minúsculas y quitar espacios adicionales
            console.log('Card Time:', time); // Verificar el valor de cada tarjeta
    
            if (time === selectedTime) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    }
    

    //Filtrado por season

    const seasonsOfYearContainer = document.querySelectorAll('.seasons_of_year_container')

    seasonsOfYearContainer.forEach(seasonCard =>{
        seasonCard.addEventListener('click', function () {
            filterBySeason(seasonCard)
        });
    });

    function filterBySeason(seasonCard) {
        const selectedSeason = seasonCard.getAttribute('data-season').toLowerCase().trim();
        const fragranceCards = document.querySelectorAll('.parfum_card');
        
        fragranceCards.forEach(card => {
            const season = card.getAttribute('data-season').toLowerCase().trim();
            console.log('Card Season:', season)
            if (season === selectedSeason) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        
        });
    }

    const resetButton = document.getElementById('reset-filter');  // Asumiendo que tienes un botón con este ID
    if (resetButton) {
        resetButton.addEventListener('click', function () {
            showAllFragrances();
        });
    }

    function showAllFragrances() {
        const fragranceCards = document.querySelectorAll('.parfum_card');
        fragranceCards.forEach(card => {
            card.style.display = 'flex';
        });
    }


}); //--
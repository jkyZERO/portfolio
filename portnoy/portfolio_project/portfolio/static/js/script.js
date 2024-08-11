document.addEventListener('DOMContentLoaded', function() {

    const deleteLinks = document.querySelectorAll('a[href*="delete"]');
    // Находим все ссылки, в которых в href содержится "delete"
    
    deleteLinks.forEach(link => {
        // Проходим по каждой найденной ссылке
        
        link.addEventListener('click', function(e) {
            // Добавляем обработчик события на клик по ссылке

            if (!confirm('Are you sure you want to delete this item?')) {
                // Показываем пользователю окно подтверждения

                e.preventDefault();
                // Если пользователь нажал "Отмена", предотвращаем переход по ссылке
            }
        });
    });
})

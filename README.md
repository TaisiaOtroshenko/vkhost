# vkhost
Тренируюсь в vk API 

Цель - жмыхнуться и украсть закрытые сообщеньки 😉

План: скачать все сообщеньки пользователя, найти недоступные и попытаться восстановить, что получится, потом скачать и вернуть будто не трогали

Чем уже набаловались:
*   тыкали функции в vk_try_msg.py
*   решили прочитать переписочки vk_save_txt.py читаемо, но запускаем руками
*   решили скачать, типа потом разберемся что с этим делать, vk_save_json.py но скачивается коряво и долго и данных много 
    зато поставили скачивание в бесконечность. можно любоваться как красиво тикают id'шники
*   дошли лапки до скриптов vk_save_scripts.py скачивает за пару секунд до 900 сообщений. и формат доступен для последующей обработки (осталось обработать, лол)
*   выбрали id'шники всех отстутсвующих сообщений в vk_save_missing_id_scripts.py
*   попробовали восстановить их в vk_restore.py иииии
и восстанавливать нечего.
продолжать потеряло смысл.

Текущий этап - больше не интересно. завершен.
можно по фану еще прочитать что все-таки я скачала, но обработка данных не так интересна, как их вскрытие

Итоги проекта:
хорошая новость - проект успешно завершен
хорошая новость - вк пофиксило баги пятилетней давности (уязвимость, приводящяя к повышению привилегий)
хорошая новость - недавно удаленные сообщения можно восстановить (решение проблемы "удалить у себя" по ошибке)
плохая новость - давно удаленные сообщения достать невозможно (более полугода)


самое важное:
НЕ БУДЕТ РАБОТАТАТЬ без файла vk_tokens.py в текущей папке содержащего ваш id_me и access_token_me взятый с сайта vkhost
инструкцию я не дам, мне впадлу писать
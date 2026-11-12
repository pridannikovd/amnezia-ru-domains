# Amnezia RU domain feed for AWG Manager

Текстовая копия публичного доменного списка
[lib4u/amnezia-tunneling-ru/amnezia.json](https://github.com/lib4u/amnezia-tunneling-ru).
На входе готовый JSON проекта, на выходе `domains.txt`: один домен в строке.
IP-списки `amnezia-ip.json` и `amnezia-ip-lite.json` здесь не используются.

GitHub Actions проверяет источник ежедневно в 01:30 UTC и коммитит изменившийся
текстовый список. Расписание GitHub может запускаться с задержкой. AWG Manager
сам скачивает `domains.txt` по расписанию подписок. Если загрузка, JSON или
проверка размеров некорректны, последняя опубликованная версия сохраняется.

Адрес подписки:

`https://raw.githubusercontent.com/pridannikovd/amnezia-ru-domains/main/domains.txt`

Репозиторий предназначен только для общедоступного списка и конвертера.
В нём нет конфигурации роутера, адресов VPN-сервера, паролей, VPN-ключей
и индивидуальных исключений. Локальные исключения хранятся в AWG Manager.

Исходные данные и метод их сборки принадлежат исходному проекту и его источникам:
[v2fly/domain-list-community](https://github.com/v2fly/domain-list-community).
Это адаптация формата для подписок AWG Manager, а не самостоятельная база доменов.

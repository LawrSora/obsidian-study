---
курс: 2
дисциплина: ОБД
tags:
  - бэкенд/бд
---
# :luc_database:SQL

## Введение
<div class="green-div">

<strong>SQL</strong> <i class="icon-database"></i> — язык для управления реляционными базами данных.<br>
<strong>Ключевые функции</strong>:  
<ul>
<li>Создание структур данных <i class="icon-table"></i></li>
<li>Запросы с фильтрацией и сортировкой</li>
<li>Управление правами доступа <i class="icon-lock"></i></li>
</ul>
</div>

> [!tip]- Диалекты SQL  
> Популярные реализации:  
> - <span class="internal-link">[[MySQL]]</span> (веб-приложения)  
> - <span class="internal-link">[[PostgreSQL]]</span> (сложные проекты)

---
## Основы CRUD

```sql
-- Создание таблицы
CREATE TABLE Products (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Выборка данных
SELECT * FROM Products WHERE price > 1000;
```

<div class="boring-div">

<strong>Базовые операции</strong> <i class="icon-tools"></i>:  
<ul>
<li><code>INSERT</code> — добавление записей</li>
<li><code>UPDATE</code> — изменение данных</li>
<li><code>DELETE</code> — удаление строк</li>
</ul>

</div>

---
## SQL в веб-разработке

### Безопасность
> [!warning]- Инъекции  
> Всегда используйте:  
> - Параметризованные запросы  
> - [[Тестирование ПО|тестирование]] 
### Интеграция
- **ORM**: Связь с Python  и PHP 
- **Миграции**: Версионное управление схемой 
---
## Пример: Соединение таблиц

```sql
SELECT Users.name, Orders.total 
FROM Users 
INNER JOIN Orders ON Users.id = Orders.user_id;
```

<div class="boring-div">

<strong>Типы JOIN</strong> <i class="icon-link"></i>:  
<ul>
<li><code>INNER</code> — общие данные</li>
<li><code>LEFT</code> — все записи из левой таблицы</li>
</ul>

</div>

---

## Связи с другими темами


> [!note]- Для веб-приложений  
> SQL — основа для хранения данных в <span class="internal-link">[[Информационная система|информационных системах]]</span>.

---

## Ссылки для графа
- [[База данных|базы данных]]  
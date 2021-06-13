# structure_of_organizations
Это тестовое задание

Ссылка на док файл со скриншотами https://docs.google.com/document/d/1wP2zIOsPbdVWbCCkxT7Ry-NjcCRIqDmL7AAbUDhlNM4/edit?usp=sharing

Приложение состоит из 4 под-приложений:
- common
- organizations
- departments
- employees

Модели и поля в приложении common:
BaseModel является абстарактной моделью для всех моделей
- uid (Уникальный идентификатор) UUIDField // Замена обычному ID для полей в БД. Что уменьшает вероятность дублирования полей при использовании GenericForeignKey и GenericManyToManyKey
- is_active (Является ли запись активной) BooleanField
- created (Дата и время создания записи) DateTimeField
BaseCatalog является абстарактной моделью для всех моделей. Используется при создании моделей каталогов, которые содержат наименования
- name (Наименование) CharField
- code (Код) CharField // при необходимости фильтрации по уникальным названиям в моделях

Модели и поля в приложении organizations:
Organization
- name (Название организации) CharField
- co_organizations (Список организаций предков) ManyToMany на себя

Модели и поля в приложении departments:
DepartmentCatalog(Наименования департаментов) Наследуется от BaseCatalog
Department (Департамент)
- department_name(Наименование департамента) ForeignKey на DepartmentCatalog
- organization(Организация) ForeignKey на Organization // Принадлежность к организации
- co_department(Департамент предок) ForeignKey на себя // Если текущий депатамент является подчиненным департаментом департамента предка.
- head_of_department(Глава департамента) ForeignKey На EmployeeDepartmentRelation // Указывающая кто является главой департамента и в какой должности.

Модели и поля в приложении employees:
Employee(Сотрудник) // Модель служит для расширения стандартной User модели джанго. Может быть дополнена дополнительной информацией по сотрудникам
- user(Пользователь) OneToOneKey указывающая на пользователя
Position(Наименования должностей) Наследуется от BaseCatalog
EmployeeDepartmentRelation(Принадлежность сотрудника к департаменту) // Данная модель позволяет установить связь сотрудника с Департаментом, который принадлежит той или иной организации. За счет ForeignKey можно к одному сотруднику указывать множество депаратментов и должностей
- employee(Cотрудник) ForeignKey на Employee
- department(Департамент) ForeignKey на Department 
- position(Должность) ForeignKey на Position. Может быть пустым

Эндпоинты для получения данных. Все через метод GET
- api/organizations/ (Для получения всех организаций из Бд)

- api/organizations/<uid>/ Для получения организации по уникальному идентификатору

- api/departments/ (Для получения всех департаментов из Бд)

- api/departments/<uid>/ Для получения департаментов по уникальному идентификатору

- api/employees/positions/  (Для получения всех наименований должностей и их уидов из Бд)

- api/employees/  (Для получения всех сотрудников из Бд)

- api/employees/<uid>/ Для получения сотрудников по уникальному идентификатору



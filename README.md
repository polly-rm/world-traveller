# World Traveller Project

Проектът представя функционалността на приложение за споделяне и популяризиране на информация за различни дестинации по целия свят.

## Описание
Всеки потребител може да влезе в приложението и да разгледа детайлите за публикуваните места и дестинации. Всеки има достъп и до карта с изобразени забележителности в повечето градове по света, както и навигация за филтриране на забележителностите в някои от европейските столици. Потребителите могат да се регистрират, да качват информация и снимки на места, които са посетили, и съответно могат да редактират или изтриват постовете си. Освен това те могат да коментират или „харесват“ с бутона Like постове на други потребители.

## Техническо изпълнение
•	Проектът е изпълнен с Django 3.2.5.
•	Използваната база данни е PostgreSQL ORDBMS.
•	Изображенията се съхраняват в storage cloud в Cloudinary.
•	Проектът е разделен в няколко модула.

## Структура

# MODULE world_traveller_auth: за регистрация на потребители
Изпълнена е sign up/ sign in/ sign out функционалност с използване на Extended Django User. Потребителят се регистрира с имейл и парола.

![2](https://user-images.githubusercontent.com/81371141/128712718-c080bd2e-b357-447d-bc49-bc90d8c43723.png)

## Models
•	WorldTravellerUserModel: с атрибути: email, is_staff, date_joined

## Forms
•	SignUpForm: наследява UserCreationForm и филтрира показваните полета: email, password1, password2
•	SignInForm: наследява AuthenticationForm

## Managers
•	WorldTravellerUserManager: наследява BaseUserManager

## Views
### Class-based Views
•	SignUpView: за регистрация
•	SignInView: за влизане
•	SignOutView: за изход


# MODULE profile: за създаване на профил
Изпълнено е автоматично създаване на профил при регистриране на потребител, в който може да бъде попълнена допълнителна информация за потребителя, както и да бъде прикачена профилна снимка. При попълване на всички полета, профилът е 100% завършен. Преди това потребителят е известяван чрез сигнал, че профилът му не е напълно завършен.

![3](https://user-images.githubusercontent.com/81371141/128712757-32f466e8-34d8-48d4-881f-4833e24991ce.png)

## Models
•	Profile: с атрибути: first_name, last_name, age, about_me, profile_image, user с OneToOneField connection и property, което показва процентите на ниво на завършеност на профила.

## Forms
•	ProfileForm: форма, която изключва полетата ‘user’ и ‘is_complete’, за да не бъдат показвани и променя стила на изобразяване на полетата чрез widgets attributes.

## Views
### Function-based Views:
•	profile_details: показва детайли за профила на потребител, както и качените от него дестинации, ако има такива
•	delete_profile: за изтриване на профил на потребител, което изтрива цялата информация за потребителя, както и неговите постове, коментари и лайкове.

## Signals
•	user_created: сигнал, който се изпълнява след регистриране на потребител и създава автоматично профил на потребителя
•	check_is_complete: сигнал, който проверява нивото на завършеност на профила

## Templatetags:
•	profile_complete_notification: темплейт таг за известяване за незавършен профил. Известието изчезва, веднъж щом профилът е завършен напълно, т.е при попълване на всички полета.


# MODULE places: за създаване, редактиране, изтриване на публикации, показване на детайлите им, коментиране и харесване

![4](https://user-images.githubusercontent.com/81371141/128712793-93fa4987-ee79-412e-b73a-478aadcbe4b1.png)

## Models: 
•	Place: с атрибути: name, location, description, image, created_on; ForeignKey- user
•	Comment: с атрибути: text, created_on; ForeignKey- place, ForeignKey- user 
•	Like: ForeignKey- place, ForeignKey- user 
•	Images: с атрибути: image; ForeignKey- place

## Forms:
•	PlaceForm – изключва полето ‘user’, за да не се показва
•	EditPlaceForm – наследява PlaceForm и променя полето ‘name’ на read-only чрез widgets attrs
•	CommentForm – за коментар; променя стилът на полето на текста чрез widgets attrs

## Views
### Class-based Views:
•	PlaceListView: за показване на всички места
•	EditPlaceView: за редактиране на пост
•	DeletePlaceView: за изтриване на пост
•	PlaceDetailsView: за показване на детайлите на публикация; показва коментарите, подредени по време на публикуване, дава възможност на други потребители да харесват и коментират 
•	CommentPlaceView: за коментиране на публикация

### Function-based Views:
•	create_place: за създаване на публикация; създава се ImageFormset, който дава възможност да се качват няколко снимки при наличие на едно ImageField
•	like_place: за даване и отнемане на лайк на публикация


# MODULE common: за визуализиране на начална страница 

![1](https://user-images.githubusercontent.com/81371141/128712831-efdac7ac-23a0-4b78-96d4-343d9b3ad52d.png)

## Views:
### Class-Based Views:
•	LandingPageTemplateView: за визуализиране на начална страница
•	MapPageTemplateView: за препращане към карта с геокодер, за въвеждане на адрес и откриване на местоположенията на различните места

# PACKAGE core
## Mixins:
•	BootstrapFormMixin: за bootstrap на формите; наследява се от формите и по този начин към всичките им полета се добавя стил с class ‘form-control’ чрез widgets attrs

## Validators:
•	validate_text_starts_with_capital: custom валидатор, който проверява дали дадено поле започва с главна буква. Ако не, се raise-ва ValidationError.

# TEMPLATES
Използвани са: Template Inheritance и Custom Template Tag.

•	landing_page.html
•	map.html
## Directory: world_traveller_auth:
•	sign_in.html
•	sign_out.html
•	sign_up.html
## Directory profiles:
•	profile_details.html
•	profile_delete.html
## Directory places:
•	place_create.html
•	place_edit.html
•	place_delete.html
•	place_details.html
•	place_list.html
## Directory common:
•	base.html
•	header.html
•	footer.html
•	navigation.html
## Directory tags:
•	profile_complete_notification.html

# TESTING
## World_traveller auth Tests: 
### Views:
•	test_sign_in_view
•	test_sign_up_view
•	test_sign_out_view
## Profiles Tests: 
### Views:
•	test_profile_details_view
•	test_delete_profile_view
## Places Tests: 
### Views:
•	test_comment_place_view
•	test_create_place_view
•	test_delete_place_view
•	test_edit_place_view
•	test_like_place_view
•	test_place_details_view
•	test_place_list_view
### Forms:
•	test_place_form
### Models:
•	test_place_model
## Core Tests:
•	test_custom_validators

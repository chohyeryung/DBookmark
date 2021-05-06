# DBookmark
models -> admin -> views -> templates -> urls
- 프로젝트 시작
    - django-admin startproject config .
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py runserver
    
- bookmark 앱 시작
    - python manage.py startapp bookmark
    - 'bookmark', in INSTALLED_APPS
    
- bookmark/models Bookmark
    - python manage.py makemigrations bookmark
    - python manage.py migrate
    - \_\_str\_\_()
  
- bookmark/admin Bookmark

- List Bookmark
  - bookmark/views BookmarkListView
  - bookmark/templates/bookmark/bookmark_list.html
  - urls; bookmark/urls bookmark:list
  
- Add Bookmark
  - bookmark/views BookmarkCreateView
  - bookmark/templates/bookmark/bookmark_create.html, bookmark_list.html
  - bookmark/urls bookmark:add
  
- Bookmark Detail
  - bookmark/views BookmarkDetailView
  - bookmark/templates/bookmark bookmark_detail.html, bookmark_list.html
  - bookmark/urls bookmark:detail
  
- Update Bookmark
  - bookmark/views BookmarkUpdateView
  - bookmark/templates/bookmark bookmark_update.html, bookmark_list.html
  - bookmark/urls bookmark:update
  - bookmark/models get_absolute_url() in Bookmark
  
- Delete Bookmark
  - bookmark/views BookmarkDeleteView
  - bookmark/templates/bookmark bookmark_confirm_delete.html, bookmark_list.html
  - bookmark/urls bookmark:delete
  
- 기능 완성 🤝🐱‍👤
- config/templates/base.html, extends, block title, block content
  
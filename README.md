# Django

## Open preview README.md

```bash
$ Ctrl + Shift + V
```

## Cài đặt Django

- Sử dụng pip để cài đặt Django. Mở cửa sổ cmd, từ cửa sổ cmd gõ lệnh:

```bash
$ pip install django
```

## Tạo mới project với Django

```bash
$ django-admin startproject mysite
```

- Chạy thử sever để coi ok chưa nhá !
- Từ cửa sổ cmd, di chuyển vào trong thư mục project (mysite) và khởi động server với lệnh:

```bash
$ cd mysite
$ python manage.py runserver

```
## Generated models from database:

```bash
$ python3 manage.py inspectdb --database=data_db > backend/models.py

```
## Activate model
- Đầu tiên chúng ta cần phải báo cho project của chúng ta biết là app của chúng ta đã được cài đặt. Bằng cách câu lệnh makemigrations, bạn đã thông báo cho Django biết đã có sự thay đổi với các model của bạn và các thay đổi sẽ được lưu như là 1 migration.

```bash
$ python3 manage.py makemigrations

```
- Bây giờ chạy câu lệnh:

```bash

python3 manage.py migrate
```


## Tích hợp vuejs với Django bằng cách sử dụng Vue CLI độc lập

- Một cách khác để xen kẽ Vue là thiết lập một thể hiện Vue độc ​​lập trên một máy chủ riêng biệt. Điều này được thực hiện bằng cách thiết lập dự án Vue bằng CLI và lấy dữ liệu từ ứng dụng Django của bạn bằng API. Để bắt đầu với điều này, bạn cần cài đặt Vue bằng webpack:

```bash
$ npm install -g vue-cli
$ vue init webpack django-vue
$ cd django-vue
$ npm install
$ npm run dev

```

- Điền thông tin của tên dự án, mô tả, vv.. khi bạn tạo. "npm run serve" sẽ khởi động máy chủ web cục bộ mà bạn có thể kiểm tra bằng cách mở http: // localhost: 8080 / trong trình duyệt của bạn.

- Bây giờ bạn đã sẵn sàng để bắt đầu lấy dữ liệu từ ứng dụng Django của bạn. Điều này không được đề cập trong hướng dẫn này, nhưng một gợi ý là nhìn vào Axios. Đây là một thư viện trợ giúp để giao tiếp với máy chủ bằng Ajax.


## Tích hợp vuejs với Django bằng cách sử dụng API Axios    




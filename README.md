## Thư mục file hệ thống, cài đặt chung cho toàn server : [*eLearning/*](https://github.com/longnp030/BaiTapLonWeb/tree/master/eLearning)
[***settings.py***](https://github.com/longnp030/BaiTapLonWeb/blob/master/eLearning/settings.py) : settings của toàn server

## Thư mục code chính : [***lms/***](https://github.com/longnp030/BaiTapLonWeb/tree/master/lms)
[***/files/***](https://github.com/longnp030/BaiTapLonWeb/tree/master/lms/files) : thư mục chứa file bài giảng\
[***/images/users/***](https://github.com/longnp030/BaiTapLonWeb/tree/master/lms/images/users) : thư mục chứa ảnh đại diện của người dùng\
[***/migrations/*** ](https://github.com/longnp030/BaiTapLonWeb/tree/master/lms/migrations): thư mục chứa các log file thay đổi CSDL\
[***/static/lms/***](https://github.com/longnp030/BaiTapLonWeb/tree/master/lms/static/lms) : thư mục chứa CSS file\
[***/templates/***](https://github.com/longnp030/BaiTapLonWeb/tree/master/lms/templates) : thư mục chứa HTML files\
\
[***admin.py***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/admin.py) : cài đặt setting của quản trị viên\
[***forms.py***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/forms.py) : các class tạo forms ( ví dụ: form đăng ký, form đăng nhập, form bài giảng, ...)\
[***models.py***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/models.py) : các bảng của CSDL\
[***tests.py***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/models.py) : tạo test case để kiểm thử hệ thống\
[***urls.py***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/urls.py) : các đường dẫn đến các trang của website\
[***views.py***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/views.py) : trực quan hóa các trang của website

## Thư mục chứa các file HTMLs : [*lms/templates/*](https://github.com/longnp030/BaiTapLonWeb/tree/master/lms/templates)
[***/courses/***](https://github.com/longnp030/BaiTapLonWeb/tree/master/lms/templates/courses) : thư mục chứa HTML liên quan đến khóa học ( ví dụ: chi tiết khóa học, chi tiết môn học, tạo môn học, đăng ký học, ...)\
&nbsp;&nbsp;&nbsp;&nbsp;[***course_detail.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/courses/course_detail.html) : chi tiết khóa học ( khi người dùng enroll vào khóa học rồi)\
&nbsp;&nbsp;&nbsp;&nbsp;[***course_overview.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/courses/course_overview.html) : tổng quan khóa học ( khi người dùng chưa enrol vào khóa học)\
&nbsp;&nbsp;&nbsp;&nbsp;[***create.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/courses/create.html) : tạo khóa học mới\
&nbsp;&nbsp;&nbsp;&nbsp;[***create_lect.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/courses/create_lect.html) : tạo bài học trong 1 khóa học\
&nbsp;&nbsp;&nbsp;&nbsp;[***dashboard.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/courses/dashboard.html) : danh sách khóa học mà giáo viên dạy, hoặc người học đã enroll vào\
&nbsp;&nbsp;&nbsp;&nbsp;[***enroll.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/courses/enroll.html) : người dùng đăng ký học khóa học\
&nbsp;&nbsp;&nbsp;&nbsp;[***modify_comps.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/courses/modify_comps.html) : chỉnh sửa thành phần của khóa học, bài giảng\
\
[***/lms/***](https://github.com/longnp030/BaiTapLonWeb/tree/master/lms/templates/lms) : thư mục chứa HTML liên quan đến trang chủ, người dùng, ...\
&nbsp;&nbsp;&nbsp;&nbsp;[***index.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/lms/index1.html) : trang chủ\
&nbsp;&nbsp;&nbsp;&nbsp;[***user_profile.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/lms/user_profile.html) : trang cá nhân người dùng\
\
[***/registration/***](https://github.com/longnp030/BaiTapLonWeb/tree/master/lms/templates/registration) : thư mục chứa HTML liên quan đến đăng ký\
&nbsp;&nbsp;&nbsp;&nbsp;[***login.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/registration/login.html) : trang đăng nhập\
&nbsp;&nbsp;&nbsp;&nbsp;[***register.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/registration/register.html) : trang đăng ký\
&nbsp;&nbsp;&nbsp;&nbsp;[***teacher_register.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/registration/teacher_register.html) : trang đăng ký với tư cách giáo viên\
&nbsp;&nbsp;&nbsp;&nbsp;[***password_change_form.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/registration/password_change_form.html): trang đổi mật khẩu\
&nbsp;&nbsp;&nbsp;&nbsp;[***password_change_done.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/registration/password_change_done.html): trang thông báo đổi mật khẩu thành công\
&nbsp;&nbsp;&nbsp;&nbsp;[***password_reset_form.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/registration/password_reset_form.html): trang đặt lại mật khẩu\
&nbsp;&nbsp;&nbsp;&nbsp;[***password_reset_done.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/registration/password_reset_done.html): trang thông báo đã gửi email xác nhận đặt lại mật khẩu\
&nbsp;&nbsp;&nbsp;&nbsp;[***password_reset_confirm.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/registration/password_reset_confirm.html): trang điền mật khẩu mới\
&nbsp;&nbsp;&nbsp;&nbsp;[***password_reset_complete.html***](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/templates/registration/password_reset_complete.html): trang thông báo đặt lại mật khẩu thành công

## Thư mục chứa file CSS : [*lms/static/lms/style.css*](https://github.com/longnp030/BaiTapLonWeb/blob/master/lms/static/lms/style.css)
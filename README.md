## Thư mục file hệ thống, cài đặt chung cho toàn server : *eLearning/*
***settings.py*** : settings của toàn server

## Thư mục code chính : ***lms/***
***/files/*** : thư mục chứa file bài giảng\
***/images/users/*** : thư mục chứa ảnh đại diện của người dùng\
***/migrations/*** : thư mục chứa các log file thay đổi CSDL\
***/static/lms/*** : thư mục chứa CSS file\
***/templates/*** : thư mục chứa HTML files\
\
***admin.py*** : cài đặt setting của quản trị viên\
***forms.py*** : các class tạo forms ( ví dụ: form đăng ký, form đăng nhập, form bài giảng, ...)\
***models.py*** : các bảng của CSDL\
***tests.py*** : tạo test case để kiểm thử hệ thống\
***urls.py*** : các đường dẫn đến các trang của website\
***views.py*** : trực quan hóa các trang của website\

## Thư mục chứa các file HTMLs : *lms/templates/*
***/courses/*** : thư mục chứa HTML liên quan đến khóa học ( ví dụ: chi tiết khóa học, chi tiết môn học, tạo môn học, đăng ký học, ...)\
		*course_detail.html* : chi tiết khóa học ( khi người dùng enroll vào khóa học rồi)\
		*course_overview.html* : tổng quan khóa học ( khi người dùng chưa enrol vào khóa học)\
		*create.html* : tạo khóa học mới\
		*create_lect.html* : tạo bài học trong 1 khóa học\
		*dashboard.html* : danh sách khóa học mà giáo viên dạy, hoặc người học đã enroll vào\
		*enroll.html* : người dùng đăng ký học khóa học\
		*modify_comps.html* : chỉnh sửa thành phần của khóa học, bài giảng\
***/lms/*** : thư mục chứa HTML liên quan đến trang chủ, người dùng, ...\
	    *index.html* : trang chủ\
		*user_profile.html* : trang cá nhân người dùng\
***/registration/*** : thư mục chứa HTML liên quan đến đăng ký\
		*login.html* : trang đăng nhập\
		*register.html* : trang đăng ký\
		*teacher_register.html* : trang đăng ký với tư cách giáo viên\

## Thư mục chứa file CSS : *lms/static/lms/style.css*
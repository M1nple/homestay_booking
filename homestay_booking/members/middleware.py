# file này tạo ra để có thể lấy ảnh avatar mọi trang template mà kh cần render lại trong views.py
# B1: tạo file này
# B2: thêm  "members.middleware.UserProfileMiddleware", vào MIDDLEWARE = [...]

from members.models import UserProfile
class UserProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # ✅ Lưu function xử lý request tiếp theo

    def __call__(self, request):
        if request.user.is_authenticated:
            request.user.user_profile = UserProfile.objects.filter(user=request.user).first()  # ✅ Gán user_profile vào request
        else:
            request.user.user_profile = None  # ✅ Nếu user chưa đăng nhập, user_profile = None

        response = self.get_response(request)  # ✅ Xử lý request tiếp theo
        return response  # ✅ Trả về response cuối cùng
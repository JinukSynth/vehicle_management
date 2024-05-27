from django.db import models

class Vehicle(models.Model):
    license_number = models.CharField(max_length=20)  # 차량 번호
    price = models.BigIntegerField()  # 차량 가격
    capacity = models.IntegerField()  # 승차 인원
    license_plate_price = models.BigIntegerField()  # 번호판 가격
    release_date = models.DateField()  # 출고일자
    insurance_fee = models.IntegerField()  # 보험비
    vehicle_name = models.CharField(max_length=100)  # 차량 이름
    monthly_maintenance_cost = models.IntegerField()  # 정비비(월)
    manufacturer = models.CharField(max_length=100)  # 제조사
    daily_tuning_cost = models.IntegerField()  # 튜닝비(일)
    vehicle_form = models.CharField(max_length=100)  # 차량 형식
    monthly_depreciation_cost = models.IntegerField()  # 감가상각비(월)
    model_year = models.IntegerField()  # 모델 연도
    depreciation_base_year = models.IntegerField()  # 감가 기준 년도
    vin_number = models.CharField(max_length=17)  # 차대 번호
    installment = models.CharField(max_length=100)  # 할부
    engine_type = models.CharField(max_length=20)  # 원동기 형식
    driver_name = models.CharField(max_length=100)  # 담당 기사
    regular_inspection_date = models.DateField()  # 정기 점검일
    is_active = models.BooleanField(default=True)  # 사용 여부
    registration_certificate = models.ImageField(upload_to='vehicle_certificates/')  # 차량 등록증 파일 이름
    
    has_led_display = models.BooleanField(default=False)  # 전광판 유무
    has_karaoke = models.BooleanField(default=False)  # 노래방 유무
    has_water_heater = models.BooleanField(default=False)  # 온수기 유무
    has_refrigerator = models.BooleanField(default=False)  # 냉장고 유무
    has_usb = models.BooleanField(default=False)  # USB 유무
    has_tv = models.BooleanField(default=False)  # TV 유무

    def __str__(self):
        return f"{self.license_number} - {self.vehicle_name}"  # 객체를 문자열로 표현할 때 차량 번호와 이름 출력


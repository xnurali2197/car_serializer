class CarSerializer(serializers.ModelSerializer):
    car_age = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'brand', 'year', 'car_age']

    def get_car_age(self, obj):
        return 2026 - obj.year

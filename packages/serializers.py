from rest_framework import serializers
from .models import TransportOption, HotelOption, GuideOption, Package


class TransportOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportOption
        fields = '__all__'


class HotelOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelOption
        fields = '__all__'


class GuideOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideOption
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):
    transport = TransportOptionSerializer(read_only=True)
    hotel = HotelOptionSerializer(read_only=True)
    guide = GuideOptionSerializer(read_only=True)

    class Meta:
        model = Package
        fields = [
            'id', 'title', 'from_location', 'to_location',
            'start_date', 'end_date', 'travelers_count', 'budget',
            'total_cost', 'status', 'created_at',
            'transport', 'hotel', 'guide',
            'preferences'
        ]


class PackageCreateSerializer(serializers.ModelSerializer):
    transport_id = serializers.PrimaryKeyRelatedField(queryset=TransportOption.objects.all(), required=False, allow_null=True)
    hotel_id = serializers.PrimaryKeyRelatedField(queryset=HotelOption.objects.all(), required=False, allow_null=True)
    guide_id = serializers.PrimaryKeyRelatedField(queryset=GuideOption.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Package
        fields = [
            'title', 'from_location', 'to_location',
            'start_date', 'end_date', 'travelers_count', 'budget',
            'transport_id', 'hotel_id', 'guide_id',
            'preferences'
        ]

    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("Start date must be before end date.")
        return data

    def create(self, validated_data):
        # Get user ID from Supabase Auth (you'll need to implement this based on your auth setup)
        user_id = self.context['request'].user.id  # Adjust based on your auth implementation
        preferences = validated_data.get('preferences', {})
        transport = validated_data.pop('transport_id', None)
        hotel = validated_data.pop('hotel_id', None)
        guide = validated_data.pop('guide_id', None)

        total = 0
        if transport and not preferences.get('skip_transport', False):
            total += transport.price
        if hotel and not preferences.get('skip_hotel', False):
            nights = (validated_data['end_date'] - validated_data['start_date']).days
            total += hotel.price * nights
        if guide and not preferences.get('skip_guide', False):
            days = (validated_data['end_date'] - validated_data['start_date']).days
            total += guide.price * days

        pkg = Package.objects.create(
            user_id=user_id,  # Changed from user to user_id
            transport=transport,
            hotel=hotel,
            guide=guide,
            total_cost=total,
            **validated_data
        )
        return pkg
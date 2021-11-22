from rest_framework import serializers, validators
from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    
    reviews = ReviewSerializer(many=True,read_only=True)
    
    class Meta:
        model = WatchList
        fields = "__all__"
        

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        

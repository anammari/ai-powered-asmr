from faker import Faker
fake = Faker()

# Generate data for Video Information dimension
def generate_video_info():
    return {
        'video_id': fake.unique.random_number(digits=5),
        'channel_id': fake.random_number(digits=5),
        'audio_track_id': fake.random_number(digits=5),
        'playlist_id': fake.random_number(digits=5),
        'title': fake.sentence(),
        'description': fake.text(),
        'published_at': fake.date_time_this_year(),
        'thumbnail_url': fake.image_url(),
        'category_id': fake.random_number(digits=2),
        'length_seconds': fake.random_int(min=30, max=3000)
    }

# Generate data for Channel Information dimension
def generate_channel_info():
    return {
        'channel_id': fake.unique.random_number(digits=5),
        'name': fake.name(),
        'description': fake.text(),
        'country_code': fake.country(),
        'joined_date': fake.date_this_century(),
        'subscriber_count': fake.random_number(digits=5),
        'view_count': fake.random_number(digits=6),
        'video_count': fake.random_number(digits=4)
    }

# Generate data for User Information dimension
def generate_user_info():
    return {
        'user_id': fake.unique.random_number(digits=5),
        'username': fake.user_name(),
        'profile_image_url': fake.image_url(),
        'joined_date': fake.date_this_century()
    }

# Generate data for Comments dimension
def generate_comments():
    return {
        'comment_id': fake.unique.random_number(digits=5),
        'video_id': fake.random_number(digits=5),
        'author_id': fake.random_number(digits=5),
        'text': fake.text(),
        'likes': fake.random_number(digits=3),
        'published_at': fake.date_time_this_year()
    }

# Generate data for Playlist Information dimension
def generate_playlist_info():
    return {
        'playlist_id': fake.unique.random_number(digits=5),
        'title': fake.sentence(),
        'description': fake.text(),
        'channel_id': fake.random_number(digits=5),
        'created_at': fake.date_this_century(),
        'modified_at': fake.date_this_century(),
        'privacy_status': fake.random_element(elements=('public', 'private', 'unlisted'))
    }

# Generate data for Audio Tracks dimension
def generate_audio_tracks():
    return {
        'audio_track_id': fake.unique.random_number(digits=5),
        'title': fake.sentence(),
        'uploader_channel_id': fake.random_number(digits=5),
        'duration_seconds': fake.random_int(min=30, max=1800),
        'license': fake.random_element(elements=('standard', 'creative_commons')),
        'audio_codec': fake.random_element(elements=('mp3', 'wav', 'aac')),
        'bitrate': fake.random_number(digits=5),
        'sample_rate': fake.random_number(digits=5)
    }

# Generate data for Tags dimension
def generate_tags():
    return {
        'tag_id': fake.unique.random_number(digits=5),
        'term': fake.word()
    }
    
# Generate data for the Video Tags dimension
def generate_video_tags():
    return {
        'tag_id': fake.random_number(digits=5),
        'video_id': fake.random_number(digits=5)
    }

# Generate data for Countries dimension
def generate_countries():
    return {
        'country_code': fake.country_code(),
        'name': fake.country()
    }

# Generate data for Categories dimension
def generate_categories():
    return {
        'category_id': fake.unique.random_number(digits=2),
        'name': fake.word()
    }

# Generate data for Facts: Views Per Day, Likes Per Day, Dislikes Per Day, Favorites Per Day, Comments Per Day
def generate_video_activity():
    return {
        'video_id': fake.random_number(digits=5),
        'date': fake.date_this_year(),
        'views': fake.random_number(digits=5),
        'likes': fake.random_number(digits=4),
        'dislikes': fake.random_number(digits=3),
        'favorites': fake.random_number(digits=3),
        'comments': fake.random_number(digits=4)
    }
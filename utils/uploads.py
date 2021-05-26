import os
import uuid
import time
from functools import partial


def get_upload_filename(user, filename):
    return f'photos/%s/%s_%s' % str(user.first_name), (str(time()).replace('.', '_'), filename)


def user_directory_path(instance, filename):
    return 'attachment_files/user_{0}/{1}'.format(instance.user.id, filename)


def generate_random_name(instance, filename, path):
    path = path
    user = instance.user
    modified_path = path + '/{0}/attachments'.format(user)
    extension = "." + filename.split('.')[-1]
    filename = str(uuid.uuid4().hex) + extension

    return os.path.join(modified_path, filename)


def upload_to(path):
    return partial(generate_random_name, path=path)


def generate_random_image_name(instance, filename, path):
    """
        Generate random filename base on input
    """
    path = path
    modified_path = path + '/profile_pictures'
    extension = "." + filename.split('.')[-1]
    filename = str(uuid.uuid4().hex) + extension

    return os.path.join(modified_path, filename)


def image_upload_to(path):
    """
        Partial update file to a buffer object before validation
        and upload.
    """
    return partial(generate_random_image_name, path=path)

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator


class CustomUser(AbstractUser):
    username = models.CharField(
        ('username'),
        max_length=40,
        unique=True,
        help_text=(
            'Required. 40 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator()],

        error_messages={
            'unique': ("このユーザーネームはすでに使用されています。"),
        },
    )
    description = models.TextField(verbose_name='プロフィール', null=True, blank=True, max_length=400)
    # photo = ResizedImageField(verbose_name='写真', size=[200, 200], crop=['middle', 'center'], blank=True, null=True, upload_to='images/account')
    # photo_small = ImageSpecField(source='photo',
    #                              processors=[ResizeToFill(50, 50)],
    #                              format='JPEG',)


    class Meta:
        verbose_name_plural = 'CustomUser'


class MindMap(models.Model):
    owner_id = models.ForeignKey("CustomUser", verbose_name='オーナー', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='タイトル', max_length=30)
    # writers = models.ManyToManyField("CustomUser", verbose_name='編集者')
    # style = models.ForeignKey("Template", verbose_name='テンプレート')


# class Templates(models.model):
#   title = models.CharField(verbose_name='タイトル', max_length=30)
#   owner = models.ForedignKey("CustomUser", verbose_name='オーナー', on_delete=models.CASCADE)
#   structure = (
#     ("tree", "tree"),
#     ("free", "free")
#   )
#   backgroundcolor = models.IntegerField()
    def __str__(self):
        return self.title


class Topic(models.Model):
    map_id = models.ForeignKey("MindMap", verbose_name="マップ", on_delete=models.CASCADE)
    parent_id = models.ForeignKey("self", verbose_name="親トピック", on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(max_length=400)

    def __str__(self):
        return self.text
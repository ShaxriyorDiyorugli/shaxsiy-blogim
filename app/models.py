from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Name of Category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=500,unique=True, verbose_name='Name of Post')
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated Date')
    is_publish = models.BooleanField(default=True, verbose_name='Publish')
    views = models.IntegerField(default=0, verbose_name='Views')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name='Post')
    name = models.CharField(max_length=100, verbose_name='Name')
    body = models.TextField(verbose_name='Comment')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return f"{self.name} → {self.post.title}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_at']


class ProjectCategory(models.Model):
    title = models.CharField(unique=True, max_length=100, verbose_name='Project Name')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project Category'
        verbose_name_plural = 'Project Categories'

class Projects(models.Model):
    title = models.CharField(verbose_name='Name of Project', max_length=100, unique=True)
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Update at')
    is_publish = models.BooleanField(default=True, verbose_name='Publish')
    views = models.IntegerField(default=0, verbose_name='Views')
    project = models.ForeignKey(
    ProjectCategory,
    on_delete=models.CASCADE,
    related_name='projects_set',
    verbose_name='Project Category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

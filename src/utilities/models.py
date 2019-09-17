from django.db import models
from django.contrib.contenttypes.models import ContentType
#from django.http import HttpResponse
from django.template import Template, Context
#from django.utils.safestring import mark_safe


EXPORTTEMPLATE_MODELS = [
    'company', 'api_key', 'process_file',
]


class DateTimedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ExportTemplate(models.Model):
    content_type = models.ForeignKey(
        ContentType, limit_choices_to={
            'model__in': EXPORTTEMPLATE_MODELS})
    name = models.CharField(max_length=200)
    template_code = models.TextField()
    mime_type = models.CharField(max_length=15, blank=True)
    file_extension = models.CharField(max_length=15, blank=True)

    class Meta:
        ordering = ['content_type', 'name']
        unique_together = [
            ['content_type', 'name']
        ]

    def __unicode__(self):
        return u'{}: {}'.format(self.content_type, self.name)

    def to_response(self, context_dict, filename):
        """
        Render the template to an HTTP response, delivered as a named file attachment
        """
        template = Template(self.template_code)
        mime_type = 'text/plain' if not self.mime_type else self.mime_type
        response = HttpResponse(
            template.render(Context(context_dict)),
            content_type=mime_type
        )
        if self.file_extension:
            filename += '.{}'.format(self.file_extension)
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(
            filename)
        return response

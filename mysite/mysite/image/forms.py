from django import forms
from django.core.files.base import ContentFile
from slugify import slugify
from urllib import request
from .models import Image

class ImageForm(forms.ModelForm):
	class Meta:
		model=Image
		fields=('title','url','description')

	def clean_url(self):
		url=self.cleaned_data['url']
		valid_extensions=['jpg','jpeg','png']
		extension= url.rsplit('.', 1)[1].lower()
		if extension not in valid_extensions:
			raise forms.ValidationError("The given Url does not match valid "
										"image extension.")
		return url

	def save(self,force_insert=False,force_update=False,commit=True):
		print(2.5)
		image=super(ImageForm,self).save(commit=False)
		print(2.6)
		image_url=self.cleaned_data['url']
		print(2.8)
		image_name='{0}.{1}'.format(slugify(image.title),
									image.url.rsplit('.',1)[1].lower())
		response=request.urlopen(image_url)
		print(2.9,image_name,image_url,ContentFile(response.read()))
		image.image.save(image_name,ContentFile(response.read()),save=False)
		print(3.6,commit)
		if commit:
			print(3.3)
			image.save()
		return image


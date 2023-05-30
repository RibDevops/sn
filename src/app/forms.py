from django import forms
from app.models import *
 
 
# creating a form
class NumeracaoForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Numeracao
 
        # specify fields to be used
        fields = [
            "id_tipo",
            "numero_doc",
            "description_doc",
        ]

# class TipoForm(forms.ModelForm):
#     class Meta:
#         model = Tipo
#         fields = [
#             "id_tipo",
#             "numero_doc",
#             "description_doc",
#         ]

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['tipo_doc', 'description_tipo']


    #     id = models.AutoField(primary_key=True)
    # tipo_doc = models.IntegerField()
    # description_tipo =
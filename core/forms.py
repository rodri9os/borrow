#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 11:37:03 2018

@author: rodrigos
"""

from django import forms
from .models import Endereco, Pessoa, Status, Item, Cessao, Emprestimo

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class CessaoForm(forms.ModelForm):
    class Meta:
        model = Cessao
        fields = '__all__'

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = '__all__'

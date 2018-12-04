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

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item

class CessaoForm(forms.ModelForm):
    class Meta:
        model = Cessao

class Emprestimo(forms.ModelForm):
    class Meta:
        model = Emprestimo

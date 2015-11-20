# -*- coding:utf-8 -*-
from django.shortcuts import render
1 change


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import *

def search_form(request):
    return render_to_response('search_form.html')
    
def main(request):
    return render_to_response('main.html')
    
def allbooks(request):
    books = Book.objects.order_by('isbn')
    return render_to_response('allbooks.html',{'books':books})

    
def search(request):
    errors = []
    if 'author' in request.GET:
        author = request.GET['author']
        if not author:
            errors.append('Enter a search term.')
        else:
            books = Book.objects.filter(authorID__name=author)
            if not books:
                return render_to_response('search_noresults.html',
                                          {'author_name':author})
            else:
                return render_to_response('search_results.html',
                                          {'books': books})
    return render_to_response('search_form.html',
        {'errors': errors })
        

def bookmessage(request):
    if 'ISBN' in request.GET:
        isbn = request.GET['ISBN']
        book = Book.objects.filter(isbn=isbn)
        return render_to_response('bookmessage.html',
        {'book': book[0]})
        
def add(request):
    errors = []
    if 'isbn' in request.GET:
        isbn = request.GET['isbn']
        if not isbn:
            errors.append('Enter isbn.')
        elif len(isbn)>13:
            errors.append('isbn is too long')
        else:
            books = Book.objects.filter(isbn=isbn)
            if not books:
                title = request.GET['title']
                authorID = request.GET['authorID']
                publisher = request.GET['publisher']
                publishDate = request.GET['publishDate']
                price = request.GET['price']
                a_name = request.GET['author_name']
                a_age = request.GET['author_age']
                a_country = request.GET['author_country']
                if title and authorID and publisher and publishDate and price and a_name and a_age and a_country:
                    if a_age.isdigit():
                    	author = Author.objects.filter(authorID=authorID)
                    	if not author:
                        	a = Author(authorID = authorID,
                           	name = a_name,
                           	age = a_age,
                           	country = a_country)
                        	a.save()
                        	b = Book(isbn = isbn,
                         	title = title,
                         	authorID = a,
                        	publisher = publisher,
                         	publishDate = publishDate,
                         	price = price)
                        	b.save()
                    	else:
                        	b = Book(isbn = isbn,
                         	title = title,
                         	authorID = author,
                         	publisher = publisher,
                         	publishDate = publishDate,
                         	price = price)
                        	b.save()
                    else:
                        errors.append('年龄栏只能填数字')
                else:
                    errors.append('please perfect imformation')
            else:
                return render_to_response('alreadyhave.html',
                                          {'isbn': isbn})
    return render_to_response('add.html',
        {'errors': errors })

def update(request):
    errors = []
    if 'isbn' in request.GET:
        isbn = request.GET['isbn']
        if not isbn:
            errors.append('Enter isbn.')
        elif len(isbn)>13:
            errors.append('isbn is too long')
        else:
            books = Book.objects.filter(isbn=isbn)
            if not books:
                errors.append('there is no such book in the library')
            else:
                title = request.GET['title']
                publisher = request.GET['publisher']
                publishDate = request.GET['publishDate']
                price = request.GET['price']
                #authorID = request.GET['author_ID']
                a_name = request.GET['author_name']
                a_age = request.GET['author_age']
                a_country = request.GET['author_country']
                if title:
                    books[0].title = title
                    books[0].save()
                if publisher:
                    books[0].publisher = publisher
                    books[0].save()
                if publishDate:
                    books[0].publishDate = publishDate
                    books[0].save()
                if price:
                    books[0].price = price
                    books[0].save()
                if a_name:
                    books[0].authorID.name = a_name
                    books[0].authorID.save()
                if a_age:
                    if a_age.isdigit():
                    	books[0].authorID.age = a_age
                    	books[0].authorID.save()
                    else:
                        errors.append('年龄栏只能填数字')
                if a_country:
                    books[0].authorID.country = a_country
                    books[0].authorID.save()
    return render_to_response('update.html',
        {'errors': errors })
        
def delete(request):
    if 'isbn' in request.GET:
        isbn = request.GET['isbn']
        book = Book.objects.get(isbn=isbn)
        book.delete()
    books = Book.objects.order_by('isbn')
    return render_to_response('allbooks.html',{'books':books})

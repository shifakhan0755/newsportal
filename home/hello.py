
"""    all_crosses = CareerModel.objects.get(id=id)
    if request.method == "POST":
        if ('exist' in request.POST):
            print('Post')
            checks = request.Post['exist']"""


'''if request.method == 'POST':
        updatedata = Brands.objects.get(id=id)
        updatedata.name = request.post['name']
        updatedata.save()
    else:
        return redirect('brands-list')'''

"""if 'is_private' in request.POST:
    is_private = request.POST['is_private']
    return HttpResponse(is_private)
else:
    is_private = False
    return HttpResponse(is_private)"""



def complete_inventory( warehouse_1, x, warehouse_2, y ) :
	a=list(filter(lambda x:x != 0, warehouse_1))
	b=list(filter(lambda y:y != 0, warehouse_2))
	c=a+b
	s = c.sort()
	print(s)
complete_inventory([1,2,3,0,0,0],[4,5,6],1,2)
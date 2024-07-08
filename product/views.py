from django.shortcuts import render , redirect , get_object_or_404
from .models import ProductUpdate
from django.urls import reverse
from .forms import ProductUpdateForm

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def product_list(request):
    """
    context data
        - 현재 페이지의 데이터(Page객체)
        - 현재 페이지가 속한 page group의 시작페이지, 끝페이지 번호
        - 시작 페이지의 이전/끝 페이지 다음페이지가 있는지 여부.
        - 시작 페이지의 이전/끝 페이지 다음페이지 번호
    """
    paginate_by = 10 # Page당 데이터 개수
    page_group_count = 10 # 한 Page group 당 page수.

    # 사용자가 조회한 페이지(현재페이지) 
    current_page = int(request.GET.get("page" , 1)) 
    # DB에서 상품들을 모두 조회
    p_list = ProductUpdate.objects.all().order_by("-pk")
    print(len(p_list))
    # Paginate객체 생성 
    paginator = Paginator(p_list , paginate_by)

    # current_page가 속한 page group의 시작페이지, 끝 페이지 조회.
    start_idx = int((current_page - 1 ) / page_group_count) * page_group_count 
    end_idx = start_idx + page_group_count
    
    page_range = paginator.page_range[start_idx:end_idx]

    # context data dictionary 에 template 에 전달할 값들 추가
    context_data = {
        "page_range" : page_range,
        "p_list" : paginator.page(current_page)
    }

    start_page = paginator.page(page_range[0]) # group 시작
    end_page = paginator.page(page_range[-1])  # group 끝

    # 시작페이지가 이전/다음페이지가 있는지 조회
    has_previous = start_page.has_previous()
    has_next = end_page.has_next()

    # 이전/다음페이지가 있다면
    if has_previous:
        context_data['has_previous'] = has_previous
        context_data['previous_page_no'] = start_page.previous_page_number

    if has_next:
        context_data['has_next'] = has_next
        context_data['next_page_no'] = end_page.next_page_number

    return render(request , "product/product_list.html" , context_data)


# 상품 정보

def product_info(request , product_id):

    product = ProductUpdate.objects.get(pk=product_id)
    return render(request, "product/product_info.html", {"product":product})

    print("없는 제품입니다.")

# 상품 등록
@login_required 
def product_create(request):
    if request.method == "GET":
        return render(request, "product/product_create.html" , {"form":ProductUpdateForm})
    elif request.method == "POST":
        form = ProductUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("product:product_list"))
        else :
            return render(request, "product/product_create.html",{"form":form})

# 상품 수정을 띄울화면
@login_required 
def product_edit(request):
    return render(request , "product/product_edit.html")

# 상품 수정
@login_required 
def product_fix(request , product_id):
    product = get_object_or_404(ProductUpdate, pk=product_id)
    if request.method == 'GET' :
        form = ProductUpdateForm(instance=product)
        
        return render(request , "product/product_edit.html" , {"form":form, "product_id":product_id})

    elif request.method =='POST':
        form = ProductUpdateForm(request.POST , request.FILES,instance=product)
        if form.is_valid():
            # print(form.pk , form.price)
            form.save()
            return redirect(reverse("product:product_info",args=[product_id]))
        else:
            return render(request , "product/product_edit.html" , {"form":form})

# 상품 삭제
@login_required 
def product_del(request , product_id):
    product = ProductUpdate.objects.get(pk=product_id)
    product.delete()
    return redirect(reverse("product:product_list"))

# 상품 조회
def product_search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        product = ProductUpdate.objects.filter(product_name__contains=searched)
        for i in product:
            print(i.product_name)
        print(searched)
        return render(request, 'product/product_search.html' , {'searched' : searched,'products':product})
    else:
        return render(request , 'product/product_search.html')
    
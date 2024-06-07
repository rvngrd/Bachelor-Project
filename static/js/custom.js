function sendArticleComment(articleId) {
    let comment = $('#commentText').val()
    let parentId = $('#parent_id').val();
    $.get('/articles/add-article-comment', {
        article_id: articleId,
        article_comment: comment,
        parent_id: parentId
    }).then(res => {
        // location.reload();
        // $('#comments_area').html('نظر شما پس از بازبینی ثبت خواهد شد');
        if (comment === "") {
            alert("لطفاً متن پیام را وارد نمایید");
        } else {
            document.getElementById('comments_area').innerText = "نظر شما پس از بازبینی ثبت خواهد شد";
            document.getElementById('comments_area').scrollIntoView({behavior: "smooth"});
            $('#commentText').val('');
            $('#parentId').val('');
        }
        // document.getElementById('comments_area').classList.add("alert alert-success");
    });
}

function fillParentId(parentId) {
    $('#parent_id').val(parentId);
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});
}

function filterProducts() {
    // debugger;
    let filterPrice = $('#sl2').val();
    let start_price = filterPrice.split(',')[0];
    let end_price = filterPrice.split(',')[1];
    $('#start_price').val(start_price);
    $('#end_price').val(end_price);
    $('#filter_form').submit();
}

function fillPage(page) {
    $('#page').val(page);
    $('#filter_form').submit();
}

function Contact() {
    let message = $('#message').val();
    let title = $('#title').val();
    let email = $('#email').val();
    let full_name = $('#full_name').val();

    if (message !== "" && title !== "" && email !== "" && full_name !== "") {
        alert('پیام شما ثبت شد');
    } else {
        alert('فیلد های خواسته شده را پر کنید');
    }
}

function showLargeImage(imageSrc) {
    $('#main_image').attr('src', imageSrc);
    $('#show_large_image_modal').attr('href', imageSrc);
}

function addProductToOrder(productId) {
    const productCount = $('#product-count').val();
    $.get('/order/add-to-order?product_id=' + productId + '&count=' + productCount).then(res => {
        Swal.fire({
            title: "اعلان",
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: "#3085d6",
            confirmButtonText: res.confirm_button_text
        }).then((result) => {
            if (result.isConfirmed && res.status === 'not_auth') {
                window.location.href = '/login';
            }
        });
    })
}

function removeOrderDetail(detailId) {
    $.get('/user/remove-order-detail?detail_id=' + detailId).then(res => {
        if (res.status === 'success') {
            Swal.fire({
                title: "اعلان",
                text: 'کالای مورد نظر با موفقیت حذف شد',
                icon: 'success',
                showCancelButton: false,
                confirmButtonColor: "#3085d6",
                confirmButtonText: 'حله'
            });
            $('#order-detail-content').html(res.body);
        }
    })
}
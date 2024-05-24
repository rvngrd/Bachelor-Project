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
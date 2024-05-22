function sendArticleComment(articleId) {
    var comment = $('#commentText').val()
    var parentId = $('#parent_id').val();
    $.get('/articles/add-article-comment', {
        article_id: articleId,
        article_comment: comment,
        parent_id: parentId
    }).then(res => {
        location.reload();
    });
}

function fillParentId(parentId) {
    $('#parent_id').val(parentId);
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});
}
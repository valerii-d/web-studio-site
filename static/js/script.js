$(document).ready(function(){
    $('table tr:gt(0)').each(function(row){
    var status=$(this).find('#status').html();
    switch(status){
        case 'processing':
            status='table-primary';
            break;
        case 'deviation':
            status='table-danger';
            break;
        case 'development':
            status='table-warning';
            break;
        default:
            status="table-success";
            break;
    }
    $(this).addClass(status);
});
})
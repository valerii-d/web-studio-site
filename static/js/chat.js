$(document).ready(function () {
    chatId=$('.contact').attr('chat-id');
    //Work with WebSocket
    var url=`ws://${window.location.host}/ws/chat/${chatId}/`;
    var chatSocket=new WebSocket(url);
    function send_message(e){
        var data=JSON.parse(e.data);
        $('#chat').append(
            `<li>
                <div class="content">
                    <div class="message">
                        <div class="bubble">
                            <p>${data['message']}</p>
                        </div>
                    </div>
                    <span>${data['created'].substring(0, 10)}</span>
                </div>
        </li>`);
    }
    $('.contact').click(function (e) {
        e.preventDefault();
        $.ajax({
            type: 'GET',
            async: true,
            url: this.href,
            success: function (data) {
                chatSocket.close();
                chatSocket=new WebSocket(`ws://${window.location.host}/ws/chat/${data['chat_id']}/`);
                chatSocket.onmessage=send_message;
                $('#chat li').remove();
                $('#info-user h5').remove();
                $('#info-user span').remove();
                id = data['sender_id'];
                chatId=data['chat_id'];
                $('#info-user').append(
                    `<h5>${data['receiver_f']}  ${data['receiver_l']} </h5>
                    <span>${data['receiver_email']} </span>`
                )
                data['results'].forEach(function (message) {
                    if (id !== message['user_id']) {
                        $('#chat').append(
                            `<li>
                            <img src="../../static/img/avatars/user.svg" alt="avatar">
                                <div class="content">
                                    <div class="message">
                                        <div class="bubble">
                                            <p>${message['message']}</p>
                                        </div>
                                    </div>
                                    <span>${message['created'].substring(0, 10)}</span>
                                </div>
                            </li>`);
                    } else {
                        $('#chat').append(
                            `<li>
                                <div class="content">
                                    <div class="message">
                                        <div class="bubble">
                                            <p>${message['message']}</p>
                                        </div>
                                    </div>
                                    <span>${message['created'].substring(0, 10)}</span>
                                </div>
                            </li>`);
                    }
                });
            },
            dataType: 'json',
        });
    });
    chatSocket.onmessage=send_message;
    chatSocket.onclose=function(e){
        console.error('Chat socket closed unexpectedly');
    }
    //send
    $('#sender-form').submit(function(e){
        e.preventDefault();
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        var message=$('#message').val();
        $.ajax({
            type: 'POST',
            async: true,
            url: `/chat/${chatId}/`,
            data: { csrfmiddlewaretoken: csrftoken,message:message},
            success: function(data){
                     chatSocket.send(JSON.stringify({
                    'message':data['message'],
                    'created':data['created'].substring(0, 10),
                }));
                $('#message').val('');
            },
            dataType: 'json',
        });
    });
});
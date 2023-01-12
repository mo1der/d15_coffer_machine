<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link href="https://fonts.googleapis.com/css2?family=Raleway" rel="stylesheet">
    <link rel="stylesheet" href="../static/css/styles.css">
</head>
<body>
<div class="wrapper">
    <div class="top">
        <div class="title"><h1>Mo1der Best Blog - POST DETAILS</h1></div>
    </div>



        <div class="content">
            <div class="card">
                <h2>{{post_title}}</h2>
                <p class="text">{{post_content}}</p>
                <a href="{{ url_for('show_post', num=blog_post["id"]) }}">text</a>
            </div>
        </div>




</div>
</body>
<footer>
    <p>Made with ♥️in London.</p>
</footer>
</html>
$(document).ready(function () {
    $("form").on("submit", function (event) {
        $.ajax({
            type: "GET",
            url: "/get_birmd",
            dataType: "json",
        }).done(function (data) {
            $("#birmd-name").text(data["birmd_name"]);
        });
        event.preventDefault();
    });
});

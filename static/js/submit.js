$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: "/get_birmd",
        dataType: "json",
    }).done(function (data) {
        $("#birmd-name").text(data["birmd_name"]);
    });

    $("form").on("submit", function (event) {
        $.ajax({
            type: "GET",
            url: `/get_birmd?temp=${$("#temperature").val()}`,
            dataType: "json",
        }).done(function (data) {
            $("#birmd-name").text(data["birmd_name"]);
        });
        event.preventDefault();
    });
});

$(document).ready(function() {
    // TODO load in automatically without needing a click
    $("#browse_title").click(function() {
        console.log("click");
        $.ajax({
            url: "/entry/list/2020",
            success: function(result) {
                console.log(result);
            }
        });
    });
    $("#btn-random-entry").click(function() {
        $.ajax({
            url: "/entry/random",
            success: function(result) {
                entry_array = result["entry"]
                $("#random_date").text(entry_array[0])
                $("#random_entry_text").text(entry_array[1])
            } 
        })
    });
    $("#form_search").submit(function(event) {
        // TODO validate
        const search = $("#form_search input").val();
        console.log("searching: " + search);
        $.ajax({
            url:"/entry/search/" + search,
            success: function(result) {
                console.log(result);
            }
        });
        event.preventDefault();
    });
});
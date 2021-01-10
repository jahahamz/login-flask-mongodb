// JQuery to submit data, could use Vue or React instead
$("form[name=signup_form]").submit(function(e) {
    
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/signup/",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            // Command + Shift + R to force reload and solve cache issues in the browser
            //console.log(resp);
            window.location.href = "/dashboard/";

        },
        error: function(resp) {
            //console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }

    });

    e.preventDefault();

});

// Login submit
$("form[name=login_form]").submit(function(e) {
    
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/login/",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            // Command + Shift + R to force reload and solve cache issues in the browser
            //console.log(resp);
            window.location.href = "/dashboard/";

        },
        error: function(resp) {
            //console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }

    });

    e.preventDefault();

});
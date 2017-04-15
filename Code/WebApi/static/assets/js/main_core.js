/**
 * Created by theo on 4/13/17.
 */


$("#urlgo").click(function (e) {
    e.preventDefault();
    datau = $("#url").val();
    console.log(datau)
    $.ajax({
        type: "POST",
        url: "./nanonetsurl",
        data: $('#canard').serialize(),
        success: function (data) {
            parseandload(data);
        }

    });
    return false;
})

function readURL(input) {
    var form = new FormData();

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
        document.getElementById("canardlocal").style.margin = "0px";
        var temp = document.getElementById("blah");
        temp.style.visibility = "visible";
        temp.style.float = "right";
        temp.style.display = "inline";
        temp.style.border = "solid 2px";
        temp.style.height = "110px";
        temp.style.width = "120px";
        temp.style.marginRight = "130px";
        console.log('------------------------------------');

        form.append("local", input.files[0]);
        //console.log($('#imgInp').val());
        $.ajax({
            type: "POST",
            url: "./nanonetslocal",
            enctype: 'mulipart/form-data',
            processData: false,
            contentType: false,
            data: form,
            success: function (data) {
                parseandload(data);
            }
        });

    }
    return true;
}

$("#imgInp").change(function () {
    readURL(this);
    return false;
});


function parseandload(data) {
    console.log("success");
    console.log(data);
    temp = JSON.parse(data);
    var bob = ["barChart", "lineChart", "pieChart", "scatterPlot"];
    var bobby = temp.result[0].prediction;
    console.log("-------------------");
    console.log(bobby);
    var aa;
    for (var i = 0; i < bob.length; i++) {
        console.log(bobby[i].probability)
        aa = document.getElementById(bobby[i].label);
        tempo = (bobby[i].probability * 100);
        if (tempo < 1) {
            tempo = 1;
        }
        console.log(tempo);
        console.log(bob[i]);
        aa.style.width = tempo + "%";
    }
}
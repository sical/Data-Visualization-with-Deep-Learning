/**
 * Created by theo on 4/13/17.
 */


$("#urlgo").click(function (e) {
    showload();
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
    showload();
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
        doneload();
    }
}


    function pos(element) {
        var top = 0, left = 0;
        do {
            top += element.offsetTop || 0;
            left += element.offsetLeft || 0;
            element = element.offsetParent;
        } while (element);

        return {
            top: top,
            left: left
        };
    }

    var canvas = document.getElementById('myCanvas');
    var ctx = canvas.getContext('2d');
    var canard = document.getElementById('temp');
    var pos = pos(canard);
    var painting = document.getElementById('paint');
    var paint_style = getComputedStyle(painting);
    canvas.width = parseInt(paint_style.getPropertyValue('width'));
    canvas.height = parseInt(paint_style.getPropertyValue('height'));
    canvas.style.border = "solid 5px";

    var mouse = {x: 0, y: 0};
    canvas.addEventListener('mousemove', function (e) {
        mouse.x = e.pageX - this.offsetLeft - pos.left;
        mouse.y = e.pageY - this.offsetTop - pos.top + $('#topBar').height();
    }, false);

    ctx.lineWidth = 3;
    ctx.lineJoin = 'round';
    ctx.lineCap = 'round';
    ctx.strokeStyle = '#00cc99';

    canvas.addEventListener('mousedown', function (e) {
        ctx.beginPath();
        ctx.moveTo(mouse.x, mouse.y);

        canvas.addEventListener('mousemove', onPaint, false);
    }, false);

    canvas.addEventListener('mouseup', function () {
        canvas.removeEventListener('mousemove', onPaint, false);
    }, false);

    var onPaint = function () {
        ctx.lineTo(mouse.x, mouse.y);
        ctx.stroke();
    };

    $('#canvasbtnclear').click(function () {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        return false;
    })

    function dataURLtoBlob(dataurl) {
    var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
    while(n--){
        u8arr[n] = bstr.charCodeAt(n);
    }
    return new Blob([u8arr], {type:mime});
}


    $('#canvasbtngo').click(function () {
        var img = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");
        var blob = dataURLtoBlob(img);
        var form = new FormData();
        console.log(img);
        showload();

        form.append("local", blob);
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

    })

function showload() {
   var temp = document.getElementById("loading");
    temp.style.visibility ="visible";
}

function doneload() {
    var temp = document.getElementById("loading");
    temp.style.visibility ="hidden";
}
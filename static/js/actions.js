function clean_data() {
    $.getJSON('./clean_data', function (data) {
        $("#show_result_text1").text(data)
    });
}

function show_EDA_Chart() {
    $.getJSON('./show_EDA_Chart', function (data) {
        if (data) {
            for (let i = 0; i < data.length; i++) {
                console.log(data[i].base64_str)
                $('#chartImg' + (i + 1)).attr("src", data[i].base64_str)
            }
        }
    });
}

function train_data() {
    $.getJSON('./train_data', function (data) {
        if (data) {
            $("#show_result_text2").text(data)
        }
    });
}

function forecasts() {
    $.getJSON('./forecasts', {
        'temperature':$('#temperature').val(),
        'humidity':$('#humidity').val(),
        'wind_speed': $('#wind_speed').val(),
        'noise_level': $('#noise_level').val(),
        'precipitation':$('#precipitation').val(),
        'solar_radiation':$('#solar_radiation').val(),
    }, function (data) {
        if (data) {
            $("#show_result_text3").text("The Air quality is " + data)
        }
    });
}



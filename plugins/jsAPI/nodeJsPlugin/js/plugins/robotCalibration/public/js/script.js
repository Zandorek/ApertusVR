var apiEndPoint = 'http://localhost:3000/api/v1/';
var apiEndPointNode = apiEndPoint + 'nodes/';
var nodeName = 'robotRootNode';

function getNodePosition(nodeName) {
    console.log('getting Node position: ', nodeName);
    doGetRequest(apiEndPointNode + nodeName + '/position', function(res){
        var pos = res.data.items[0].position;
        console.log(pos);
        $('#posX').val(pos.x.trim());
        $('#posY').val(pos.y.trim());
        $('#posZ').val(pos.z.trim());
    });
}

function setNodePosition(nodeName) {
    console.log('setting Node position: ', nodeName);
    var pos = {
        x: $('#posX').val(),
        y: $('#posY').val(),
        z: $('#posZ').val()
    };
    doPostRequest(apiEndPointNode + nodeName + '/position', pos, function(res){
        console.log(res);
    });
}

function getNodeOrientation(nodeName) {
    console.log('getting Node orientation: ', nodeName);
    doGetRequest(apiEndPointNode + nodeName + '/orientation', function(res){
        var ori = res.data.items[0].orientation;
        console.log(ori);

        $('#quatW').val(ori.w.trim());
        $("#quatWRange").slider("value", ori.w.trim());

        $('#quatX').val(ori.x.trim());
        $("#quatXRange").slider("value", ori.x.trim());

        $('#quatY').val(ori.y.trim());
        $("#quatYRange").slider("value", ori.y.trim());

        $('#quatZ').val(ori.z.trim());
        $("#quatZRange").slider("value", ori.z.trim());
    });
}

function setNodeOrientation(nodeName, value) {
    console.log('setting Node orientation: ', nodeName);
    var ori = {
        w: $('#quatW').val(),
        x: $('#quatX').val(),
        y: $('#quatY').val(),
        z: $('#quatZ').val()
    };
    doPostRequest(apiEndPointNode + nodeName + '/orientation', ori, function(res){
        console.log(res);
    });
}

function doGetRequest(apiEndPointUrl, callback) {
    $.get(apiEndPointUrl, function(res) {
        console.log(res);
        callback(res);
    });
}

function doPostRequest(apiEndPointUrl, data, callback) {
    $.post(apiEndPointUrl, data, function(res) {
        console.log(res);
        callback(res);
    }, "json");
}

function showToast(text, timeOutMs) {
    $('#snackbar').html(text);
    $('#snackbar').addClass('show');
    setTimeout(function(){
        $('#snackbar').removeClass('show');
    }, timeOutMs);
}

function copyToClipboard(elementId) {
    var element = document.getElementById(elementId);
    element.select();
    document.execCommand('Copy');
    showToast('Text Copied: ' + element.value, 3000);
}

function pasteFromClipboard(elementId) {
    var element = document.getElementById(elementId);
    element.focus();
    element.select();
    document.execCommand('Paste');
}

function resetPos() {
    console.log('resetPos');

    $('#posX').val(0);
    $('#posY').val(0);
    $('#posZ').val(0);

    setNodePosition(nodeName);
}

function resetQuat() {
    console.log('resetQuat');

    $('#quatW').val(1);
    $("#quatWRange").slider("value", 1);

    $('#quatX').val(0);
    $("#quatXRange").slider("value", 0);

    $('#quatY').val(0);
    $("#quatYRange").slider("value", 0);

    $('#quatZ').val(0);
    $("#quatZRange").slider("value", 0);

    setNodeOrientation(nodeName);
}

$(document).ready(function(){

    $('[data-toggle="tooltip"]').tooltip();

    $( ".input-range" ).slider({
        min: -1,
        max: 1,
        value:0,
        step: 0.00000001,
        slide: function( event, ui ) {
            var focused = document.activeElement;
            if (focused.classList.contains('ui-slider-handle')) {
                $("#" + $(this).data("input-handler")).prop('value', ui.value);
                setNodeOrientation(nodeName);
            }
        }
    });

    $(".input-range-var").bind('keyup change', function(e){
        console.log('quat bind: ', $(this).val());
        var focused = document.activeElement;
        if (focused.classList.contains('input-range-var')) {
            $("#" + $(this).data("input-range")).slider("value", $(this).val());
            setNodeOrientation(nodeName);
        }
    });


    $(".input-pos").bind('keyup change', function(e){
        console.log('pos bind: ', $(this).val());
        setNodePosition(nodeName);
    });

    $("#nodeName").change(function(){
        nodeName = $(this).val();
    });

    $('#nodeName').val(nodeName);
    getNodePosition(nodeName);
    getNodeOrientation(nodeName);
});
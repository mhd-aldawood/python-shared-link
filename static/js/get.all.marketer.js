$("#idForm").submit(function(e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.


    var actionUrl = '/marketerUuid';

//    $.ajax({
//        type: "POST",
//        url: actionUrl,
//        data: form.serialize(), // serializes the form's elements.
//        success: function(data)
//        {
//          alert(data); // show response from the php script.
//        }
//    });
console.log('test')
});
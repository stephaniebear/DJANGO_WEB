$(document).ready(function () {
  // $(this).val()
  // console.log($(this).val())
  
  //########## Remark ##########
  $("input[name='specs_general']").change(function(){
    if($("input[name='specs_general']:checked").val() == 0){
      $('#specs_general').after('<div class="form-group" id="general_remark"><input type="text" class="form-control" name="general_remark" placeholder="Remark"></div>')
    }
    else{
      $('#general_remark').remove()
    }
  })

  $("input[name='specs_elec_general']").change(function(){
    if($("input[name='specs_elec_general']:checked").val() == 0){
      $('#specs_elec_general').after('<div class="form-group" id="elec_general_remark"><input type="text" class="form-control" name="elec_general_remark" placeholder="Remark"></div>')
    }
    else{
      $('#elec_general_remark').remove()
    }
  })

  $("input[name='specs_elec_techniques']").change(function(){
    if($("input[name='specs_elec_techniques']:checked").val() == 0){
      $('#specs_elec_techniques').after('<div class="form-group" id="elec_techniques_remark"><input type="text" class="form-control" name="elec_techniques_remark" placeholder="Remark"></div>')
    }
    else{
      $('#elec_techniques_remark').remove()
    }
  })

  $("input[name='specs_network_general']").change(function(){
    if($("input[name='specs_network_general']:checked").val() == 0){
      $('#specs_network_general').after('<div class="form-group" id="network_general_remark"><input type="text" class="form-control" name="network_general_remark" placeholder="Remark"></div>')
    }
    else{
      $('#network_general_remark').remove()
    }
  })

  $("input[name='specs_network_techniques']").change(function(){
    if($("input[name='specs_network_techniques']:checked").val() == 0){
      $('#specs_network_techniques').after('<div class="form-group" id="network_techniques_remark"><input type="text" class="form-control" name="network_techniques_remark" placeholder="Remark"></div>')
    }
    else{
      $('#network_techniques_remark').remove()
    }
  })
  //############################

  $('#office_provinces').change(function(){
    if($('#office_provinces').val() == '0'){
      $('#office_name').html('')
      $('#office_name').append('<option value="0">- Please Select Office Name -</option>')
      $('#office_name').attr('disabled','True')
      console.log($('#office_provinces').val())

      $('#office_type_A').removeAttr('checked','checked')
      $('#office_type_B').removeAttr('checked','checked')
      $('#office_type_C').removeAttr('checked','checked')
      return
    }

    let office_province = $('#office_provinces').val()
    $.ajax({
      url: '/getProvinceName/',
      type: 'GET',
      dataType: 'json',
      data: {
        province_name : office_province
      },
      success: function( response ){
        console.log(response)
        $('#office_name').removeAttr('disabled','True')
        $('#office_name').html('')
        $('#office_name').append('<option value="0">- Please Select Office Name -</option>')
        for(let i = 0; i < response.length ; i++){
          $('#office_name').append('<option value="'+ response[i].fields.name +'">'+ response[i].fields.name +'</option>')
        }
      }
    })
  })

  $('#office_name').change(function(){
    if($('#office_name').val() == '0'){
      console.log('office_name == 0')
      $('#office_type_A').removeAttr('checked','checked')
      $('#office_type_B').removeAttr('checked','checked')
      $('#office_type_C').removeAttr('checked','checked')
      return
    }
    let office_name = $('#office_name').val()
    console.log(office_name)
    $.ajax({
      url: '/getOfficeType/',
      type: 'GET',
      dataType: 'json',
      data: {
        office_name : office_name
      },
      success: function( response ){
        let office_type = response[0].fields.types
        console.log(office_type)

        function RemoveAttr (){
          console.log('Remove')
          $('#office_type_A').removeAttr('checked','checked')
          $('#office_type_B').removeAttr('checked','checked')
          $('#office_type_C').removeAttr('checked','checked')
        }
        if(office_type == 'A'){
          RemoveAttr()
          $('#office_type_A').attr('checked','checked')
          $('#office_type_B').removeAttr('checked','checked')
          $('#office_type_C').removeAttr('checked','checked')
        }
        else if(office_type == 'B'){
          RemoveAttr()
          $('#office_type_B').attr('checked','checked')
          $('#office_type_A').removeAttr('checked','checked')
          $('#office_type_C').removeAttr('checked','checked')
        }
        else if(office_type == 'C'){
          RemoveAttr()
          $('#office_type_C').attr('checked','checked')
          $('#office_type_A').removeAttr('checked','checked')
          $('#office_type_B').removeAttr('checked','checked')
        }
        else{
          $('#office_type_A').removeAttr('checked','checked')
          $('#office_type_B').removeAttr('checked','checked')
          $('#office_type_C').removeAttr('checked','checked')
        }
      }
    })
  })
})
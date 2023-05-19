QUnit.test("errors should be hidden on keypress", function (assert) 
    {
      $('input[name="text"]').trigger('keypress');
      $('.has-error').hide();
      assert.equal($('.has-error').is(':visible'), false);
  });
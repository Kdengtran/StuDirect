let f = function(str, start, end) {

    // For each parameter, its `.value` contains
    // either its value in the type you've declared,
    // or it's `undefined`.  This is a good place to
    // extract the `.value`s and assign default
    // values.
    str = str.value;
    start = start.value;
    end = end.value;
  
    // Your function should return the exact type
    // you've declared for the `result` in
    // `glide.json`, or `undefined` if there's an
    // error or no result can be produced, because a
    // required input is `undefined`, for example.

    test = $.ajax({
      type:'GET',
      url: "flask/app.py",
      data: { param: 'donut'}
    })

    console.log(test)
    // call adam.js for the thing I want to send to Glide
    // 

    // this is the thing I want to send to Glide
    // return a string (e.g. job poster ID)

    // 

    return str.substring(start, end);
  }

// create api request (asynchronous)
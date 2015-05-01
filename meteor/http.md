# HTTP package

http requests should be conducted server side to avoid cross domain policy issues.

    Meteor.http.get(url, function(error, result) {
      console.log(result);
      return result;
    });
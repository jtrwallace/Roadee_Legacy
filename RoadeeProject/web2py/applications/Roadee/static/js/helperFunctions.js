function get_something(OBJECT, dataName, controllerURL, unique_id) {
    $.ajax(controllerURL,
        {
            data: {
                unique_id: unique_id //request.vars.unique_id
            },
            method: 'POST',
            success: function (data) {
                OBJECT.set(dataName, data);
            },
            error: function(data) {
                return "Server Error"
            }
        }
    );
}

function add_something(OBJECT, dataName, controllerURL, data) {
    $.ajax(controllerURL,
        {
            data: {
                data: OBJECT.get(data) //request.vars.data
            },
            method: 'POST',
            error: function(data) {
                return "Server Error"
            }
        }
    );
}

//
function delete_something(OBJECT, dataName, controllerURL, unique_id) {
    $.ajax(controllerURL,
        {
            data: {
                unique_id: unique_id //request.vars.unique_id
            },
            method: 'POST',
            error: function(data) {
                return "Server Error"
            }
        }
    );
}

//Check if an object has a specific key value pair.
function hasValue(obj, key, value) {
    return obj.hasOwnProperty(key) && obj[key] === value;
}

//Check if a list has a specific value.
function findWithAttr(array, attr, value) {
    for(var i = 0; i < array.length; i += 1) {
        if(array[i][attr] === value) {
            return i;
        }
    }
}

//To retrieve the time in UTC string format
function get_UTC_String() {
    var date = new Date();
    return date.toUTCString();
}

//Makes the date more readable and in user's time zone.
function get_pretty_time() {
    var date = new Date();
    var full_date = date.toString();
    var split_date = full_date.split(" ");
    var split_time = split_date[4].split(":");
    return split_date[1] + " " + split_date[2] + " " + split_time[0] + ":" + split_time[1];
}
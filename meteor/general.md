# Meteor Notes

### Attaching events to templates

    Template.templateName.events({
      "submit .elementClassName": function(event) {
      
      }
    });

events object is key:value pairs where you can attach functions to the following events:

    click
    dblclick
    focus
    blur
    change
    mouseenter
    mouseleave
    mousedown
    mouseup
    keydown
    kepress
    keyup
Event properties + methods
    type // the event's type, like "click", "blur" or "keypress"
    target // originating dom eleemnt
    currentTarget // element andling the event
    which // for mouse events, the number of the mousebutton, for key events, char or key code
    stopPropagation(), stopImmediatePropagation() // prevent event from propagating to other elements
    preventDefault() // prevent default (duh!)
    isPropagationStopped(), isImmediatePropagationStopped()
    isDefaultPrevented() // returns whether preventDefault()
    
currentTarget() is always the element attached to the event. event.target can be a child element a parent, eg.

'click p': function(event) {
  var paragraph = event.currentTarget // always going to be the <p>
  var clickedElement = event.target // could be the <p>, could be a child like a span element
}

if a selector matches multiple elements that an event bubbles to, it'll be called multiple times.


### Mongo Collections

constructor
CollectionName = new Mongo.collection("collectionName");

collection methods
Question: what is an upsert?


CollectionName.find({});
CollectionName.findOne({});
CollectionName.insert({});
CollectionName.update({});
CollectionName.remove({});
CollectionName.allow({});
CollectionName.deny({});

#### Cursors
Create a cursor with find({});

So... 
        var topPosts = CollectionName.find({}, {sort: -1, limit: 5});
        var count = 0;
        topPosts.forEach(function(post) {
            console.log("title " + count + ": " + post.title);
            count++;
        });

### Mongo Query Operators
MongoDB Query Operators are "meta" operators that let you modify query behavior or output. 
#### Operators
$set replaces the value of a field w the specified value
        { $set: {<field>: <val>, ...}}
$ne selects documents where the value of the field is not equal to the specified value

## Session
Global object on the client that can store key:value pairs.
Session is reactive, meaning it'll rerender if template data changes.

##### Session.set(key, val)

Can be called on an object of keys and values ie
Session.set({
    a: "foo",
    b: "bar"
})

##### Session.setDefault(key, val)

Will set a variable in a session if it's not set already, otherwise works the same as Session.set()

##### Session.get(key)

Retrieves the value of a session variable.

##### Session.equals(key, val)
Tests if a variable is equal to a value



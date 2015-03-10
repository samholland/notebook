# Lists 

Making a Sass list:

    $list-of-classnames: ('.class-1', '.class2', '.class3');

Looping:

    @for $i from 1 through length($list-of-classnames) {
      $ornament: nth($list-of-classnames, $i); 
      #{$class-item} {
        /* include sass here */
      }
    }
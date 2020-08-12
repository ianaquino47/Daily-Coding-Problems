# This problem was asked by Facebook.

# Given a function f, and N return a debounced f of N milliseconds.

# That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds.

const debounced = function(f, milliseconds) {
  let defer;

  return function() {
    if (defer) {
      clearTimeout(defer);
    }

    defer = setTimeout(f, milliseconds)
  }
}
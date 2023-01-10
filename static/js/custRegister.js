/**
 * Validates customer registration form. Frontend implementation. Note frontend can be gotten around,
 * hence this is also validated on backend.
 * @returns Whether the form is valid or not
 */
function validateCustomerForm() {
  const form = document.forms['custRegisterForm'];
  // Form fields
  (fname = form['fname']),
    (lname = form['lname']),
    (password = form['password']),
    (confirmPassword = form['confirmPassword']),
    (dob = form['dob']),
    (email = form['email']),
    (confirmEmail = form['confirmEmail']),
    (phone = form['phone']),
    (shippingAddr = '');

  let valid = true;
  // Begin checks
  if (!nameCheck(fname.value)) {
    valid = false;
    addError('First Name');
  } else removeError('First Name');

  if (!nameCheck(lname.value)) {
    valid = false;
    addError('Last Name');
  } else removeError('Last Name')
  return valid;
}

function nameCheck(name) {
  if (typeof name !== String && name === '') {
    return false;
  }
  return true;
}

/**
 * Adds an error h3 and appends to body that error. Does not add if error already there
 * @param {String} item The field we wish to add an error for
 */
function addError(item) {
  if(document.getElementById(item + 'Error')) return `Error for ${item} already on page.`
  const msgElement = document.createElement('h3');
  msgElement.id = item + 'Error';
  msgElement.textContent = `Check the ${item} field for any errors.`;
  document.body.appendChild(msgElement);
}

function removeError(item) {
  document.body.removeChild(document.getElementById(item + 'Error'));
  // document.createElement('input').inn
}
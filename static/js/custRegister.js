/**
 * Validates customer registration form. Frontend implementation. Note frontend can be gotten around,
 * hence this is also validated on backend.
 * @returns Whether the form is valid or not
 */
function validateCustomerForm() {
  const form = document.forms['custRegisterForm'];
  // Form fields
  const fname = form['fname'].value,
    lname = form['lname'].value,
    password = form['password'].value,
    confirmPassword = form['confirmPassword'].value,
    dob = form['dob'].value,
    email = form['email'].value,
    confirmEmail = form['confirmEmail'].value,
    phone = form['phone'].value,
    shippingAddr = '';

  let valid = true;

  // Begin checks
  if (!nameCheck(fname)) {
    valid = false;
    addError('First Name');
  } else removeError('First Name');

  if (!nameCheck(lname)) {
    valid = false;
    addError('Last Name');
  } else removeError('Last Name');

  if (confirmPassword !== password) {
    valid = false;
    addError('confirmPassword', 'Please confirm both passwords are the same');
  } else removeError('confirmPassword');

  if (!passwordCheck(password)) {
    valid = false;
    addError(
      'password',
      'Ensure your password is at least 8 characters ' +
        'and contains at least 1 uppercase letter, lowercase letter, number and symbol.'
    );
  } else removeError('password');

  if (!dobCheck(dob)) {
    valid = false;
    addError('Date of Birth');
  } else removeError('Date of Birth');

  if (confirmEmail !== email) {
    valid = false;
    addError('confirmEmail', 'Please confirm both emails are the same');
  } else removeError('confirmEmail');

  if (!emailCheck(email)) {
    valid = false;
    addError('Email');
  } else removeError('Email');
  return valid;
}

/**
 * Check the name
 * @param {String} name The name to check
 * @returns Boolean for if name is valid
 */
function nameCheck(name) {
  if (typeof name === 'string' && name.trim() !== '') {
    return true;
  }
  return false;
}

/**
 * Adds an error h3 and appends to body that error. Does not add if error already there
 * @param {String} item The field we wish to add an error for
 * @param {String} message The optional message we wish to display, otherwise it will show a default msg
 */
function addError(item, message) {
  if (document.getElementById(item + 'Error')) return `Error for ${item} already on page.`;
  const msgElement = document.createElement('h3');
  msgElement.id = item + 'Error';
  msgElement.textContent = message || `Check the ${item} field for any errors.`;
  document.body.appendChild(msgElement);
}

/**
 * Removes the node with id=item+'Error'
 * @param {String} item The field we wish to remove an error for
 */
function removeError(item) {
  if (document.getElementById(item + 'Error'))
    document.body.removeChild(document.getElementById(item + 'Error'));
}

/**
 * Checks whether password meets requirements: 8 chars, at least 1 uppercase and lowercase letter,
 * number and symbol
 * @param {String} password The password to check
 * @returns Boolean for whether the password is valid
 */
function passwordCheck(password) {
  // If password isn't even correct length, don't check regex
  if (password.length < 8) return false;
  /*
   * First group is a positive lookahead matching lowercase (not starting)
   * Second group is same, for uppercase letter
   * Third group is same for digits
   * Fourth group is for symbols. \W is non-alphanumeric, \S is any nonwhitespace. We add back _ since
   * \W removes the _.
   * We then finally ensure we have at least 8 of everything.
   */
  const pattern = /^(?=[^a-z]*[a-z])(?=[^A-Z]*[A-Z])(?=\D*\d)(?=[\W\S_]*[\W_])[\w\W\S_]{8,}$/;
  // Add some other checks to avoid doing regex
  return typeof password === 'string' && password.length >= 8 && pattern.test(password);
}

/**
 * Checks if date entered is valid format MM/DD/YYYY or MM-DD-YYYY.
 * @param {String} dob The date of birth to check
 * @returns Boolean for if dob is valid
 */
function dobCheck(dob) {
  /*
   * Two groups. First checks 2digits-2digits-4digits. Second does same with / instead of -
   */
  const pattern = /^([\d]{2}-[\d]{2}-[\d]{4,})|([\d]{2}\/[\d]{2}\/[\d]{4,})$/;
  // Add some other checks to avoid doing regex
  return typeof dob === 'string' && pattern.test(dob) && !isNaN(new Date(dob)?.getTime());
}

/**
 * Checks if email passed is valid format. Ex: abc@domain.com
 * @param {String} email The email to check
 * @returns Boolean if email is valid
 */
function emailCheck(email) {
  const pattern = /^\w+[\+\.\w-]*@([\w-]+\.)*\w+[\w-]*\.([a-z]{2,4}|\d+)$/;
  // Add some other checks to avoid doing regex
  return typeof email === 'string' && email.length >= 3 && pattern.test(email);
}

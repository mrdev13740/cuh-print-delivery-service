
from pyscript import document, when


# Show messages on the page
def show_message(text, message_type="error"):
    message = document.querySelector("#message")
    message.textContent = text
    message.className = "message " + message_type


# Toggle password visibility
@when("click", "#togglePassword")
def toggle_password(event):
    password_input = document.querySelector("#password")
    toggle_button = document.querySelector("#togglePassword")

    if password_input.type == "password":
        password_input.type = "text"
        toggle_button.textContent = "Hide"
        toggle_button.setAttribute("aria-label", "Hide password")
    else:
        password_input.type = "password"
        toggle_button.textContent = "Show"
        toggle_button.setAttribute("aria-label", "Show password")


# Handle login submission
@when("submit", "#loginForm")
def handle_login(event):
    event.preventDefault()

    username = document.querySelector("#username").value.strip()
    password = document.querySelector("#password").value

    if not username or not password:
        show_message("Please enter your username and password.")
        return

    show_message(
        "The form works, but backend authentication is not connected yet.",
        "success"
    )


# Handle forgot password
@when("click", "#forgotPassword")
def handle_forgot_password(event):
    event.preventDefault()

    show_message(
        "Password recovery is not connected yet. "
        "Please contact your system administrator."
    )

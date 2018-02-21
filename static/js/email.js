function sendMail(contactForm) {
    emailjs.send("gmail", "rootone", {
        "from_email": contactForm.email.value,
        "form_message": contactForm.message.value
    })
        .then(
            function (response) {
                window.message("Success", response);
            },
            function (error) {
                window.message("error", error);
            });
}
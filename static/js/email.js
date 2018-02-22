function sendMail(contactForm) {
    emailjs.send("gmail", "rootone", {
        "from_email": contactForm.email.value,
        "form_message": contactForm.message.value
    })
        .then(
            function (response) {
                swal({
                    title: "Your email has been submitted!",
                    icon: "success"
                });
            },
            function (error) {
                swal({
                    title: "There has been an error!",
                    text: "Please try again later or email example@example.com",
                    icon: "error"
                });
            });
}
<script>
    fetch("./logOut", {
        method: "POST",
        body: JSON.stringify({}),
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then((d) => d.json())
        .then((d) => {
            window.location.replace("/");
        });
</script>

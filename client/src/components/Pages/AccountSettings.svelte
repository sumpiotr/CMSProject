<script>
    let newPassword = "";

    function removeUser() {
        fetch("./removeUser", {
            method: "POST",
            body: JSON.stringify({ userId: -1, me: true }),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((d) => d.json())
            .then((d) => {
                if (d.deleted) {
                    window.location.replace("/");
                    return;
                }
                alert(d.message);
            });
    }

    function changePassword() {
        fetch("./changePassword", {
            method: "POST",
            body: JSON.stringify({ newPassword: newPassword }),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((d) => d.json())
            .then((d) => {
                alert(d.message);
                newPassword = "";
            });
    }
</script>

<section class="accountSettings">
    <div class="title">Settings</div>
    <div class="changePassword">
        <input
            bind:value={newPassword}
            type="password"
            placeholder="Enter new password"
            class="block mb-2 bg-gray-100 p-2 rounded-lg border-2 border-indigo-500 shadow-md focus:outline-none focus:border-indigo-600"
        />
        <button type="button" on:click={changePassword}>Change password</button>
    </div>

    <div><button type="button" on:click={removeUser}>Remove Account</button></div>
</section>

<style>
    .changePassword {
        display: flex;
    }

    .changePassword input {
        margin-right: 10px;
    }

    .accountSettings div {
        margin: 25px;
    }

    .accountSettings {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    button {
        padding: 5px;
    }

    .title {
        font-size: 40px;
    }
</style>

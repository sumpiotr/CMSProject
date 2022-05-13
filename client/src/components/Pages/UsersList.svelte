<script>
    import User from "../User.svelte";

    let users = [];

    function changeAdmin(id, value, me) {
        fetch("./changeAdmin", {
            method: "POST",
            body: JSON.stringify({ userId: id, value: value }),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((d) => d.json())
            .then((d) => {
                if (me && !d.admin) {
                    window.location.replace("/");
                    return;
                }
                alert(d.message);
                getUsers();
            });
    }

    function getUsers() {
        fetch("./getUsers", {
            method: "POST",
            body: JSON.stringify({}),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((d) => d.json())
            .then((d) => {
                console.log(d.users);
                users = d.users;
            });
    }

    function removeUser(userId, me) {
        fetch("./removeUser", {
            method: "POST",
            body: JSON.stringify({ userId: userId, me: me }),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((d) => d.json())
            .then((d) => {
                if (me && d.deleted) {
                    window.location.replace("/");
                    return;
                }
                alert(d.message);
                getUsers();
            });
    }

    getUsers();
</script>

<section class="users">
    {#each users as user}
        <User username={user.username} admin={user.admin} id={user.id} {changeAdmin} {removeUser} me={user.me} />
    {/each}
</section>

<style>
    .users {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
</style>

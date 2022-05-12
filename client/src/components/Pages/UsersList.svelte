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

    getUsers();
</script>

<section class="users">
    {#each users as user}
        <User username={user.username} admin={user.admin} id={user.id} {changeAdmin} me={user.me} />
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

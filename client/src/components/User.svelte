<script>
    export let username;
    export let admin;
    export let id;
    export let changeAdmin;
    export let me;
</script>

<div class="user">
    <div>{username}</div>
    <div>
        Admin: <input
            type="checkbox"
            checked={admin}
            on:change={(e) => {
                admin = !admin;
            }}
        />
    </div>
    <div><button type="button">Remove</button></div>
    <div>
        <button
            type="button"
            on:click={() => {
                if (me) {
                    if (admin) return;
                    if (!confirm("You're going to take away all your powers! Are you sure?")) return;
                }
                changeAdmin(id, admin, me);
            }}>Change Admin</button
        >
    </div>
</div>

<style>
    .user {
        display: flex;
        width: 50%;
        justify-content: space-between;
        align-items: center;
        background-color: cadetblue;
        color: white;
        margin: 10px;
    }

    .user div:nth-child(2n) {
        background-color: gray;
    }

    .user div {
        flex-basis: 100%;
        padding: 5px;
        font-size: 20px;
    }
</style>

<script>
    import { Router, Route, Link } from "svelte-navigator";
    import Tailwindcss from "./Tailwindcss.svelte";
    import { ComponentManager } from "./componentsManager.js";

    let data = { data: [], menu: { name: "Menu1", data: { children: [] } } };
    var newURL = window.location.pathname;

    fetch("./rand", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then((d) => d.json())
        .then((d) => {
            data = d;
        });
</script>

<Tailwindcss />
<main>
    <Router>
        <svelte:component this={ComponentManager.getComponentByName(data.menu.name)} data={data.menu.data} />

        {#each data.menu.data.children as menuRoute}
            <Route path={menuRoute.name}>
                <svelte:component this={ComponentManager.getComponentByName(menuRoute.name)} {data} />
            </Route>
        {/each}
    </Router>
</main>

<style>
    main {
        text-align: center;
        padding: 1em;
        max-width: 240px;
        margin: 0 auto;
    }

    h1 {
        color: #ff3e00;
        text-transform: uppercase;
        font-size: 4em;
        font-weight: 100;
    }

    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }
</style>

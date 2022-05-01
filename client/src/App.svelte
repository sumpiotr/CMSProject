<script>
    import { Router, Route, Link } from "svelte-navigator";
    import Tailwindcss from "./Tailwindcss.svelte";
    import { ComponentManager } from "./componentsManager.js";
    import Page from "./components/Pages/Page.svelte";

    let data = { pages: [], menu: { name: "Menu1", data: { children: [] } } };
    var newURL = window.location.pathname;

    fetch("./getPage", {
        method: "POST",
        body: JSON.stringify({ name: newURL }),
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
        <svelte:component this={ComponentManager.getComponentByName(data.menuType)} data={data.pages} />

        {#each data.pages as page}
            <Route path={page.path}>
                <Page pages={data.pages} path={page.path} />
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

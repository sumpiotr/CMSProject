<script>
    import Tailwindcss from "./Tailwindcss.svelte";
    import { ComponentManager } from "./componentsManager.js";

    let data = [];
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
            console.log(data);
        });
</script>

<Tailwindcss />
<main>
    {#each data as element}
        <svelte:component this={ComponentManager.getComponentByName(element.name)} data={element.data} />
    {/each}
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

<script>
    import { Router, Route, Link } from "svelte-navigator";
    import Tailwindcss from "./Tailwindcss.svelte";
    import { ComponentManager } from "./componentsManager.js";
    import Page from "./components/Pages/Page.svelte";
    import Footer from "./components/Footer.svelte";
    import { DARK_THEME, LIGHT_THEME } from "./themes";
    import ArticlePage from "./components/Pages/ArticlePage.svelte";

    let data = { pages: [], menu: { name: "Menu1", data: { children: [] } } };
    let logged = false;
    let admin = false;
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
            data = d.data;
            logged = d.logged;
            admin = d.admin;
            console.log(admin, logged);
        });

    function changeData(data) {}

    $: {
        console.log("App: ", data);
    }
</script>

<Tailwindcss />
<main class="flex flex-col min-h-screen justify-between" style={LIGHT_THEME}>
    <Router>
        <!-- Menu -->
        <svelte:component this={ComponentManager.getComponentByName(data.menuType)} bind:data={data.pages} {logged} {admin} />

        <!-- Komponenty -->
        {#each data.pages as page}
            {#if (page.login == 1 && !logged) || (page.login == 2 && logged) || page.login == 0}
                {#if (page.admin == 1 && !admin) || (page.admin == 2 && admin) || page.admin == 0}
                    <Route path={page.path}>
                        <Page pages={data.pages} path={page.path} bind:fullData={data} />
                    </Route>
                    {#if page.pageName == "Home"}
                        {#each page.data as child}
                            {#if child.name == "Articles"}
                                {#each child.data.children as article, i}
                                    <Route path={i + ""}>
                                        <ArticlePage {logged} {article} index={i} />
                                    </Route>
                                {/each}
                            {/if}
                        {/each}
                    {/if}
                {/if}
            {/if}
        {/each}

        <!-- Footer -->
        <Footer />
    </Router>
</main>

<style>
    main {
        text-align: center;
        padding: 1em;
        max-width: 240px;
        margin: 0 auto;

        display: flex;
        flex-direction: column;

        background-color: var(--background);

        --mdc-theme-primary: var(--primary);
        --mdc-theme-secondary: var(--secondary);
        --mdc-theme-background: var(--background);
        --mdc-theme-surface: var(--surface);
        --mdc-theme-error: var(--error);
        --mdc-theme-on-primary: var(--on-primary);
        --mdc-theme-on-secondary: var(--on-secondary);
        --mdc-theme-on-surface: var(--on-surface);
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

    :global(.mdc-text-field__icon),
    :global(.mdc-deprecated-list-item),
    :global(.mdc-floating-label) {
        color: var(--outline) !important;
    }

    :global(.mdc-button),
    :global(.mdc-data-table),
    :global(.mdc-data-table__header-cell),
    :global(.mdc-data-table__cell),
    :global(.mdc-notched-outline__notch),
    :global(.mdc-notched-outline__leading),
    :global(.mdc-notched-outline__trailing) {
        border-color: var(--outline) !important;
    }

    :global(.mdc-select__dropdown-icon) {
        fill: var(--outline) !important;
    }

    :global(.mdc-data-table__cell),
    :global(.mdc-data-table__header-cell),
    :global(.mdc-text-field__input),
    :global(.mdc-select__selected-text) {
        color: var(--on-surface) !important;
    }
</style>

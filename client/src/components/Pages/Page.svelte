<script>
    import { ComponentManager } from "../../componentsManager.js";
    export let pages;
    export let path;
    export let fullData;
</script>

<section>
    {#each pages as page}
        {#if page.path == path}
            {#each page.data as element}
                {#if element.name == "ArticlesPage"}
                    <svelte:component this={ComponentManager.getComponentByName(element.name)} data={element.data} {pages} bind:fullData />
                {:else}
                    <svelte:component this={ComponentManager.getComponentByName(element.name)} data={element.data} bind:fullData />
                {/if}
            {/each}
        {/if}
    {/each}
</section>

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
                <svelte:component this={ComponentManager.getComponentByName(element.name)} data={element.data} fullData={fullData}/>
            {/each}
        {/if}
    {/each}
</section>

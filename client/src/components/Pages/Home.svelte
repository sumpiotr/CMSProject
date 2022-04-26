<script>
    import { ComponentManager } from "../../componentsManager.js";
    export let data;
</script>

<section>
    {#each data.data as element}
        <svelte:component this={ComponentManager.getComponentByName(element.name)} data={element.data} />
    {/each}
</section>

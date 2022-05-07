<script>
    export let data;
    export let fullData;

    import EditElement from "./EditElement.svelte";
</script>


<div class="edit">
    Edit
    
    {#each fullData.pages as page}
        {#if page.pageName == "Home"}
            {#each page.data as element}
                <EditElement element={element} />
            {/each}
        {/if}
    {/each}
    
</div>

<style>
    .edit {
        text-align: left;
        background-color: white;
    }

    
</style>

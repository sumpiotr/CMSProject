<script>
    export let data;
    export let fullData;

    import EditElement from "./EditElement.svelte";

    import Switch from "@smui/switch";

    let isDarkMode = true;
</script>


<div class="edit">
    Edit
    <br>
    Dark Mode
    <Switch bind:checked={isDarkMode} />

    
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

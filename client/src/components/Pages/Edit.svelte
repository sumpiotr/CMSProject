<script>
    //export let data;
    export let fullData;

    export let changeData;
    //let localData = Object.assign({}, fullData);

    //deep cloning
    let localData = JSON.parse(JSON.stringify(fullData));

    import EditElement from "./EditElement.svelte";

    import Switch from "@smui/switch";
    import Button, { Label } from "@smui/button";

    let isDarkMode = true;

    $: {
        console.log("Edit local: ", localData);
        console.log("Edit full: ", fullData);
    }

    function cancel() {
        localData = JSON.parse(JSON.stringify(fullData));
    }

    function updatePage() {
        fullData = JSON.parse(JSON.stringify(localData));

        fetch("./savePage", {
            method: "POST",
            body: JSON.stringify({ newData: fullData }),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((d) => d.json())
            .then((d) => {
                console.log("updated", d);
            });

        //tutaj Piotrek
        //default.json = fullData
    }
</script>

<div class="edit">
    Dark Mode
    <Switch bind:checked={isDarkMode} />

    {#each localData.pages as page}
        {#if page.pageName == "Home"}
            {#each page.data as element}
                <EditElement bind:element />
            {/each}

            <!-- {#each Array(page.data) as _, i}
                <EditElement bind:element={page.data[i]} />
            {/each} -->
        {/if}
    {/each}
    <div class="buttons">
        <br />
        <Button on:click={() => {}}>
            <Label>Add New</Label>
        </Button>
        <br /><br /><br />
        <Button
            on:click={() => {
                cancel();
            }}
        >
            <Label>Cancel</Label>
        </Button>
        <Button
            on:click={() => {
                updatePage();
            }}
        >
            <Label>Save</Label>
        </Button>
        <br />
    </div>

    <!-- {#each fullData.pages[0].data as _, j}
        <EditElement bind:element={fullData.pages[0].data[j]} />
    {/each} -->
</div>

<style>
    .edit {
        text-align: left;
        background-color: white;
    }

    .buttons {
        margin-left: 35px;
    }
</style>

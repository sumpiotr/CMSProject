<script>
    import Paper from "@smui/paper";

    export let data;
    export let addImg;

    let selectedIndex = 0;

    function setImg(e) {
        let form = new FormData();
        form.append("img", e.target.files[0]);

        //ustawić img na podgląd

        addImg(form, data, selectedIndex);

        // fetch("/setImg", {
        //     method: "POST",
        //     body: form,
        // });
    }

    function addNewImage() {
        console.log("xxxx");
        data.images.push({ title: "New Image", description: "Description", image: "none.jpg" });
        selectedIndex = data.images.length - 1;
    }
</script>

<div class="element">
    <Paper elevation={6}>
        <h2>Image</h2>
        <select bind:value={selectedIndex}>
            {#each data.images as image, i}
                {#if selectedIndex == i}
                    <option value={i} selected>{i}</option>
                {:else}
                    <option value={i}>{i}</option>
                {/if}
            {/each}
        </select>
        <label>Title:</label>
        <input type="text" bind:value={data.images[selectedIndex].title} />
        <label>Descr:</label>
        <input type="text" bind:value={data.images[selectedIndex].description} />
        <label>New Image:</label>
        <input
            type="file"
            id="myfile"
            name="myfile"
            on:change={(e) => {
                setImg(e);
            }}
        />

        <button type="button" on:click={addNewImage}>Add Image</button>
    </Paper>
</div>

<style>
    .element {
        /* border: 1px solid black; */
        padding-left: 5px;
    }

    .element :global(.smui-paper) {
        width: calc(100% - 40px);
        height: calc(100% - 40px);
        padding: 20px;
        padding-bottom: 20px;
        padding-right: 20px;
        margin: 20px;
        display: flex;
        flex-direction: column;
    }
</style>

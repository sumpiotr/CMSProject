<script>
    //export let data;
    export let fullData;

    export let changeData;
    //let localData = Object.assign({}, fullData);

    //deep cloning
    let localData = JSON.parse(JSON.stringify(fullData));

    import EditElement from "./EditElement.svelte";
    import EditGallery from "../EditGallery.svelte";

    import Switch from "@smui/switch";
    import Button, { Label } from "@smui/button";
    import { Net } from "../../net.js";
    import GalleryImage from "../GalleryImage.svelte";

    let isDarkMode = true;

    let images = [];

    function addImg(form, data, i) {
        images.push((j) => {
            form.append("oldImage", data.images[i].image);
            console.log(form);
            fetch("./saveImg", {
                method: "POST",
                body: form,
            })
                .then((d) => d.json())
                .then((d) => {
                    data.images[i].image = d.image;
                    j++;
                    if (j >= images.length - 1) {
                        images = [];
                        fullData = JSON.parse(JSON.stringify(localData));
                        Net.updatePage(fullData);
                        return;
                    }
                    images[j](j);
                });
        });
    }

    function rotateElements(tab) {
        console.log(tab);
        let tabOfElements = [0, 0, 0, 0]
        for(let i = 0; i < localData.pages[0].data.length; i++) {
            if(localData.pages[0].data[i].name == "Slider") tabOfElements[0] = localData.pages[0].data[i];
            if(localData.pages[0].data[i].name == "Articles") tabOfElements[1] = localData.pages[0].data[i];
            if(localData.pages[0].data[i].name == "News") tabOfElements[2] = localData.pages[0].data[i];
            if(localData.pages[0].data[i].name == "Global") tabOfElements[3] = localData.pages[0].data[i];
        }
        let finalTab = [0, 0, 0, 0]

        for(let i = 0; i < localData.pages[0].data.length - 1; i++) {
            if(tab[i] == "Slider") finalTab[i] = tabOfElements[0];
            if(tab[i] == "Articles") finalTab[i] = tabOfElements[1];
            if(tab[i] == "News") finalTab[i] = tabOfElements[2];
            console.log("finalTab");
            console.log(finalTab[i]);
            finalTab[i].id = i;
        }
        finalTab[3] = tabOfElements[3];

        localData.pages[0].data = JSON.parse(JSON.stringify(finalTab))
        console.log("ROTATE: ", localData);
    }

    $: {
        console.log("Edit local: ", localData);
        console.log("Edit full: ", fullData);
    }

    function cancel() {
        localData = JSON.parse(JSON.stringify(fullData));
    }

    function updatePage() {
        if (images.length > 0) {
            images[0](0);
            return;
        }
        fullData = JSON.parse(JSON.stringify(localData));
        Net.updatePage(fullData);
        //tutaj Piotrek
        //default.json = fullData
    }
</script>

<div class="edit">
    <!-- Dark Mode
    <Switch bind:checked={isDarkMode} /> -->

    {#each localData.pages as page}
        {#if page.pageName == "Home"}
            {#each page.data as element}
                <EditElement bind:element {addImg} {rotateElements} />
            {/each}
        {:else if page.pageName == "Gallery"}
            <EditGallery bind:data={page.data[0].data} {addImg} />

            <!-- {#each Array(page.data) as _, i}
                <EditElement bind:element={page.data[i]} />
            {/each} -->
        {/if}
    {/each}
    <div class="buttons">
        <!-- <br />
        <Button on:click={() => {}}>
            <Label>Add New</Label>
        </Button> -->
        <br />
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
        /* margin-left: 35px; */
        float: right;
        margin-right: 65px;
    }
</style>

<script>
    import Paper from "@smui/paper";
    import Select, { Option } from "@smui/select";
    import Textfield from "@smui/textfield";
    import Button, { Label } from "@smui/button";
    import HelperText from "@smui/textfield/helper-text";
    import CharacterCounter from "@smui/textfield/character-counter";

    export let data;
    export let addImg;



    function setImg(e, index) {
        let form = new FormData();
        form.append("img", e.target.files[0]);

        //ustawić img na podgląd

        //addImg(form, data, selectedIndex);
        addImg(form, data, index);

        // fetch("/setImg", {
        //     method: "POST",
        //     body: form,
        // });
    }

    function addNewImage() {
        data.images.push({ title: "New Image", description: "Description", image: "none.jpg" });
        data.images = data.images; // nie zmieniać!
    }

    function deleteImg(index) {
        data.images.splice(index, 1);        
        data.images = data.images; // nie zmieniać!
    }
</script>

<div class="element">
    <Paper elevation={6}>
        <div class="options-selector">
            <div class="bigTitle">Gallery</div>
            <!-- <h2>Image</h2>
            <div class="row">
                <Select variant="filled" bind:value={selectedIndex} key={(value) => value.toString()} label="index">
                    {#each data.images as _, i}
                        <Option value={i}>{i}</Option>
                    {/each}
                </Select>
            </div> -->


            <div class="doPapera">
                {#each data.images as image, i}
                    <div class="paper">
                        <Paper elevation={6}>
                            <div class="br" />
                            <h4>Image {i + 1}:</h4>
                            <div class="br" />
                            <div class="row">
                                <input
                                    type="file"
                                    id="myfile"
                                    name="myfile"
                                    on:change={(e) => {
                                        setImg(e, i);
                                    }}
                                />
                            </div>
                            <div class="br" />
                            <div class="row">
                                <Textfield class="Textfield" variant="filled" type="text" label="Title" bind:value={data.images[i].title} />
                            </div>
                            <br />
                            <div>
                                <!-- bez labela! -->
                                <Textfield variant="outlined" textarea input$maxlength={100} class="Textfield" type="text" bind:value={data.images[i].description}>
                                    <CharacterCounter slot="internalCounter">0 / 100</CharacterCounter>
                                    <HelperText slot="helper">Description</HelperText>
                                </Textfield>
                            </div>
                            <div class="row">
                                <Button on:click={() => {deleteImg(i)}}>
                                    <Label>Delete</Label>
                                </Button>
                            </div>
                        </Paper>
                    </div>
                {/each}
            </div>
            <br />
            <div class="row">
                <Button on:click={addNewImage}>
                    <Label>Add Image</Label>
                </Button>
            </div>
        </div>
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

    .row {
        display: flex;
        flex-direction: row;
    }

    .options-selector {
        width: 100%;
        height: 100%;
        padding: 3vh 25px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .bigTitle {
        font-size: 30px;
        font-weight: bold;
        margin-bottom: 30px;
    }

    .doPapera {
        width: 100%;
        height: 100%;
        display: flex;
        flex-wrap: wrap;
        margin-left: -20px;
    }

    .paper {
        width: auto;
        height: auto;
        display: flex;
        flex-wrap: wrap;
    }

    h4 {
        font-size: 21px;
        font-weight: bold;
        margin-left: 10px;
    }

    .br {
        margin-top: 15px;
    }
</style>

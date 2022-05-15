<script>
    import Select, { Option } from "@smui/select";
    import Textfield from "@smui/textfield";
    import Button, { Label } from "@smui/button";
    import Paper from "@smui/paper";
    import HelperText from "@smui/textfield/helper-text";
    import CharacterCounter from "@smui/textfield/character-counter";
    import DataTable, { Row, Cell } from "@smui/data-table";
    import { dataset_dev } from "svelte/internal";
    import { Net } from "../../net.js";

    export let element;
    export let addImg;

    function setImg(e, i) {
        let form = new FormData();
        form.append("img", e.target.files[0]);

        //ustawić img na podgląd

        addImg(form, element.data, i);

        // fetch("/setImg", {
        //     method: "POST",
        //     body: form,
        // });
    }
</script>

<div class="element">
    {#if element.name == "Articles"}
        <Paper elevation={6}>
            <div class="options-selector">
                <table>
                    <tr>
                        <td>
                            <div class="row">
                                <Textfield class="Textfield" variant="filled" type="number" label="ID" input$max="15" input$min="0" bind:value={element.id} />
                            </div>
                        </td>
                        <td>
                            <div class="row">
                                <label for="article_color">Color&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
                                <input type="color" id="article_color" name="article_color" bind:value={element.data.color} />
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div class="row">
                                <Select variant="filled" bind:value={element.name} key={(value) => value.toString()} label="Name">
                                    <Option value="Articles">Articles</Option>
                                    <Option value="Slider">Slider</Option>
                                    <Option value="News">News</Option>
                                </Select>
                            </div>
                        </td>
                        <td>
                            <div class="row">
                                <label for="article_backgroundColor">Background Color</label>
                                <input type="color" id="article_backgroundColor" name="article_backgroundColor" bind:value={element.data.backgroundColor} />
                            </div>
                        </td>
                    </tr>
                </table>

                <br /><br />
                <div class="row">
                    <Textfield class="Textfield" variant="filled" type="number" label="Articles" input$max="3" input$min="0" bind:value={element.data.articles} />
                </div>
                <br />
                <div class="doPapera">
                    {#each element.data.children as article, i}
                        <div class="paper">
                            <Paper elevation={6}>
                                <div class="br" />
                                <!-- <p class="articleP">Article {i}:</p> -->
                                <h4>Article {i + 1}:</h4>
                                <div class="br" />
                                <div class="row">
                                    <Textfield class="Textfield" variant="filled" type="text" label="Title" bind:value={article.title} />
                                </div>
                                <br />
                                <div>
                                    <!-- bez labela! -->
                                    <Textfield variant="outlined" textarea input$maxlength={1000} bind:value={article.text}>
                                        <CharacterCounter slot="internalCounter">0 / 1000</CharacterCounter>
                                        <HelperText slot="helper">Text</HelperText>
                                    </Textfield>
                                </div>
                            </Paper>
                        </div>
                    {/each}
                </div>

                <br />
                <div class="row">
                    <Button on:click={() => {}}>
                        <Label>SHOW</Label>
                    </Button>
                </div>
            </div>
        </Paper>

        <!-- <p>{element.name}</p> -->

        <!-- <select name="selectName" id="selectName">
            <option value="articles">Articles</option>
            <option value="slider">Slider</option>
            <option value="news">News</option>
        </select> -->

        <!-- <pre>data: {JSON.stringify(element.data, undefined, 4)}</pre>

        <p>SHOW</p> -->
        <br />
    {:else if element.name == "Slider"}
        <Paper elevation={6}>
            <div class="options-selector">
                <table>
                    <tr>
                        <td>
                            <div class="row">
                                <Textfield class="Textfield" variant="filled" type="number" label="ID" input$max="15" input$min="0" bind:value={element.id} />
                            </div>
                        </td>
                        <td>
                            <div class="row">
                                <label for="article_color">Color&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
                                <input type="color" id="article_color" name="article_color" bind:value={element.data.color} />
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div class="row">
                                <Select variant="filled" bind:value={element.name} key={(value) => value.toString()} label="Name">
                                    <Option value="Articles">Articles</Option>
                                    <Option value="Slider">Slider</Option>
                                    <Option value="News">News</Option>
                                </Select>
                            </div>
                        </td>
                        <td>
                            <div class="row">
                                <label for="article_backgroundColor">Background Color</label>
                                <input type="color" id="article_backgroundColor" name="article_backgroundColor" bind:value={element.data.backgroundColor} />
                            </div>
                        </td>
                    </tr>
                </table>
                <br />
                <div class="row">
                    <Textfield class="Textfield" variant="filled" type="number" label="Duration (s)" input$max="30" input$min="1" bind:value={element.data.duration} />
                </div>
                <br />
                <div class="row">
                    <Textfield class="Textfield" variant="filled" type="number" label="Images" input$max="3" input$min="1" bind:value={element.data.images.length} />
                </div>

                <br />

                <div>
                    {#each element.data.images as _, i}
                        <input
                            type="file"
                            id="myfile"
                            name="myfile"
                            on:change={(e) => {
                                setImg(e, i);
                            }}
                        /><br />
                    {/each}
                </div>

                <br />
                <div class="row">
                    <Button on:click={() => {}}>
                        <Label>SHOW</Label>
                    </Button>
                </div>
            </div>
        </Paper>
    {:else if element.name == "News"}
        <Paper elevation={6}>
            <div class="options-selector">
                <table>
                    <tr>
                        <td>
                            <div class="row">
                                <Textfield class="Textfield" variant="filled" type="number" label="ID" input$max="15" input$min="0" bind:value={element.id} />
                            </div>
                        </td>
                        <td>
                            <div class="row">
                                <label for="article_color">Color&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
                                <input type="color" id="article_color" name="article_color" bind:value={element.data.color} />
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div class="row">
                                <Select variant="filled" bind:value={element.name} key={(value) => value.toString()} label="Name">
                                    <Option value="Articles">Articles</Option>
                                    <Option value="Slider">Slider</Option>
                                    <Option value="News">News</Option>
                                </Select>
                            </div>
                        </td>
                        <td>
                            <div class="row">
                                <label for="article_backgroundColor">Background Color</label>
                                <input type="color" id="article_backgroundColor" name="article_backgroundColor" bind:value={element.data.backgroundColor} />
                            </div>
                        </td>
                    </tr>
                </table>

                <br />
                <div class="doPapera">
                    <div class="paper">
                        <Paper elevation={6}>
                            <div class="br" />
                            <!-- <p class="articleP">Article {i}:</p> -->
                            <h4>News:</h4>
                            <div class="br" />
                            <div class="row">
                                <Textfield class="Textfield" variant="filled" type="text" label="Title" bind:value={element.data.title} />
                            </div>
                            <br />
                            <div>
                                <!-- bez labela! -->
                                <Textfield variant="outlined" textarea input$maxlength={100} bind:value={element.data.text}>
                                    <CharacterCounter slot="internalCounter">0 / 100</CharacterCounter>
                                    <HelperText slot="helper">Text</HelperText>
                                </Textfield>
                            </div>
                        </Paper>
                    </div>
                </div>
                <br />
                <h4>News image:</h4>
                <div>
                    <input type="file" id="myfile" name="myfile" /><br />
                </div>

                <br /><br /><br />
                <div class="row">
                    <Button on:click={() => {}}>
                        <Label>SHOW</Label>
                    </Button>
                </div>
            </div>
        </Paper>
    {:else}
        <p>{element.id}</p>
        <p>{element.name}</p>
        <pre>data: {JSON.stringify(element.data, undefined, 4)}</pre>
        <p>SHOW</p>
        <br />
    {/if}
</div>

<style>
    label {
        /* Other styling... */
        text-align: right;
        clear: both;
        float: left;
        margin-right: 15px;
    }

    .element {
        /* border: 1px solid black; */
        padding-left: 5px;
    }

    pre {
        margin-left: 50px;
        text-align: left;
    }

    .options-selector {
        width: 100%;
        height: 100%;
        padding: 3vh 25px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .row {
        display: flex;
        flex-direction: row;
    }

    h4 {
        font-size: 21px;
        font-weight: bold;
        margin-left: 10px;
    }

    .br {
        margin-top: 15px;
    }

    .articleP {
        margin-left: 10px;
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

    .doPapera {
        /* width: calc(50% - 60px);
        height: calc(50% - 60px); */
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
</style>

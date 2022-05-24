<script>
    import Select, { Option } from "@smui/select";
    import Textfield from "@smui/textfield";
    import Button, { Label } from "@smui/button";
    import Paper from "@smui/paper";
    import HelperText from "@smui/textfield/helper-text";
    import CharacterCounter from "@smui/textfield/character-counter";
    import { Net } from "../../net.js";
    import Switch from "@smui/switch";

    export let element;
    export let addImg;
    export let rotateElements;

    function setImg(e, index) {
        let form = new FormData();
        form.append("img", e.target.files[0]);

        //ustawić img na podgląd

        addImg(form, element.data, index);
    }

    function handle(name, min, max) {
        if (name % 1 != 0) name = Math.floor(name);
        if (name > max) name = max;
        if (name < min) name = min;
        return name;
    }

    function addNewArticle() {
        element.data.children.push({ title: "Article", category: "kat1", text: "lorem ipsum suma ipsum lorem" });
        element.data.children = element.data.children; // nie zmieniać!
    }

    function deleteArticle(index) {
        element.data.children.splice(index, 1);
        element.data.children = element.data.children; // nie zmieniać!
    }

    //element.data.descriptions[i]

    function addNewImage() {
        element.data.images.push({ image: "none.jpg", description: "Description" });
        element.data.images = element.data.images; // nie zmieniać!
    }

    function deleteImg(index) {
        element.data.images.splice(index, 1);
        element.data.images = element.data.images; // nie zmieniać!
    }

    function changePosition(i) {
        console.log(i);
        let second, third;
        if (i == 0) {
            second = 1;
            third = 2;
        }
        if (i == 1) {
            second = 0;
            third = 2;
        }
        if (i == 2) {
            second = 1;
            third = 0;
        }

        let posibilities = ["Slider", "Articles", "News"];
        if (element.data.position[i] === element.data.position[second]) {
            posibilities = posibilities.filter((item) => {
                if (item === element.data.position[i] || item === element.data.position[third]) {
                    return false;
                } else {
                    return item;
                }
            });
            element.data.position[second] = posibilities[0];
        } else if (element.data.position[i] === element.data.position[third]) {
            posibilities = posibilities.filter((item) => {
                if (item === element.data.position[i] || item === element.data.position[second]) {
                    return false;
                } else {
                    return item;
                }
            });
            element.data.position[third] = posibilities[0];
        }
        console.log("tak");

        rotateElements(element.data.position);
    }

    function sprawdzCzyRozne() {
        if (!(oldElementDataPosition[0] == "Slider" || oldElementDataPosition[0] == "Articles" || oldElementDataPosition[0] == "News")) return -1;
        for (let i = 0; i < 3; i++) {
            if (element.data.position[i] != oldElementDataPosition[i]) return i;
        }
        return -1;
    }

    let oldElementDataPosition = [];
    $: {
        if (element.data.position != undefined) {
            let ile = sprawdzCzyRozne();
            if (ile != -1) {
                changePosition(ile);
            }
            oldElementDataPosition = [...element.data.position];
        }
    }
</script>

<div class="element">
    {#if element.name == "Articles"}
        <Paper elevation={6}>
            <div class="options-selector">
                <table>
                    <tr>
                        <td>
                            <div class="bigTitle">Articles</div>
                            <!-- <div class="row">
                                <Textfield disabled class="Textfield" variant="filled" type="number" label="ID" input$min="0" input$max="10" on:change={() => {element.id = handle(element.id, 0, 10)}} bind:value={element.id} />
                            </div> -->
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
                            <!-- <div class="row">
                                <Select disabled variant="filled" bind:value={element.name} key={(value) => value.toString()} label="Name">
                                    <Option value="Articles">Articles</Option>
                                    <Option value="Slider">Slider</Option>
                                    <Option value="News">News</Option>
                                </Select>
                            </div> -->
                            <div>&nbsp;</div>
                        </td>
                        <td>
                            <div class="row">
                                <label for="article_backgroundColor">Background Color</label>
                                <input type="color" id="article_backgroundColor" name="article_backgroundColor" bind:value={element.data.backgroundColor} />
                            </div>
                        </td>
                    </tr>
                </table>

                <!-- <br /><br />
                <div class="row">
                    <Textfield class="Textfield" variant="filled" type="number" label="Articles" input$min="0" input$max="3" on:change={() => {element.data.articles = handle(element.data.articles, 0, 3)}} bind:value={element.data.articles} />
                </div> -->
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
                                <div class="br" />
                                <div class="row">
                                    <Textfield class="Textfield" variant="filled" type="text" label="Category" bind:value={article.category} />
                                </div>
                                <br />
                                <div>
                                    <!-- bez labela! -->
                                    <Textfield variant="outlined" textarea input$maxlength={1000} bind:value={article.text}>
                                        <CharacterCounter slot="internalCounter">0 / 1000</CharacterCounter>
                                        <HelperText slot="helper">Text</HelperText>
                                    </Textfield>
                                </div>
                                <div class="row">
                                    <Button
                                        on:click={() => {
                                            deleteArticle(i);
                                        }}
                                    >
                                        <Label>Delete</Label>
                                    </Button>
                                </div>
                            </Paper>
                        </div>
                    {/each}
                </div>
                <br />
                <div class="row">
                    <Button on:click={addNewArticle}>
                        <Label>Add Article</Label>
                    </Button>
                </div>
            </div>
        </Paper>
    {:else if element.name == "Slider"}
        <Paper elevation={6}>
            <div class="options-selector">
                <table>
                    <tr>
                        <td>
                            <div class="bigTitle">Slider</div>
                            <!-- <div class="row">
                                <Textfield disabled  class="Textfield" variant="filled" type="number" label="ID" input$min="0" input$max="10" on:change={() => {element.id = handle(element.id, 0, 10)}} bind:value={element.id} />
                            </div> -->
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
                            <!-- <div class="row">
                                <Select disabled variant="filled" bind:value={element.name} key={(value) => value.toString()} label="Name">
                                    <Option value="Articles">Articles</Option>
                                    <Option value="Slider">Slider</Option>
                                    <Option value="News">News</Option>
                                </Select>
                            </div> -->
                            <div style="position: inline;">
                                Autoplay:
                                <Switch bind:checked={element.data.autoplay} />
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
                {#if element.data.autoplay == true}
                    <div class="row">
                        <Textfield
                            class="Textfield"
                            variant="filled"
                            type="number"
                            label="Duration (s)"
                            input$min="1"
                            input$max="30"
                            input$step="1"
                            on:change={() => {
                                element.data.duration = handle(element.data.duration, 1, 30);
                            }}
                            bind:value={element.data.duration}
                        />
                    </div>
                    <br />
                {/if}
                <div class="doPapera">
                    {#each element.data.images as image, i}
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
                                    <Textfield class="Textfield" variant="filled" type="text" label="description" bind:value={element.data.descriptions[i]} />
                                </div>
                                <br />
                                <div class="row">
                                    <Button
                                        on:click={() => {
                                            deleteImg(i);
                                        }}
                                    >
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
    {:else if element.name == "News"}
        <Paper elevation={6}>
            <div class="options-selector">
                <table>
                    <tr>
                        <td>
                            <div class="bigTitle">News</div>
                            <!-- <div class="row">
                                <Textfield disabled  class="Textfield" variant="filled" type="number" label="ID" input$min="0" input$max="10" on:change={() => {element.id = handle(element.id, 0, 10)}} bind:value={element.id} />
                            </div> -->
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
                            <!-- <div class="row">
                                <Select disabled variant="filled" bind:value={element.name} key={(value) => value.toString()} label="Name">
                                    <Option value="Articles">Articles</Option>
                                    <Option value="Slider">Slider</Option>
                                    <Option value="News">News</Option>
                                </Select>
                            </div> -->
                            <div>
                                <input
                                    type="file"
                                    id="myfile"
                                    name="myfile"
                                    on:change={(e) => {
                                        setImg(e, 0);
                                    }}
                                /><br />
                                <!-- <div class="row">
                                    <input
                                        type="file"
                                        id="newsfile"
                                        name="newsfile"
                                        on:change={(e) => {
                                            setImg(e, 0);
                                        }}
                                    />
                                </div> -->
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
            </div>
        </Paper>
    {:else if element.name == "Global"}
        <Paper elevation={6}>
            <div class="options-selector">
                <table>
                    <tr>
                        <td>
                            <div class="bigTitle">Global</div>
                        </td>
                        <td>
                            <!-- <div class="row">
                                <label for="article_color">Color&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
                                <input type="color" id="article_color" name="article_color" bind:value={element.data.color} />
                            </div> -->
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <h4>Position:</h4>
                        </td>
                        <td>
                            <!-- <div class="row">
                                <label for="article_backgroundColor">Background Color</label>
                                <input type="color" id="article_backgroundColor" name="article_backgroundColor" bind:value={element.data.backgroundColor} />
                            </div> -->
                        </td>
                    </tr>
                </table>
                <br />
                <div class="row">
                    <Select variant="filled" bind:value={element.data.position[0]} key={(value) => value.toString()} label="1">
                        <Option value="Articles">Articles</Option>
                        <Option value="Slider">Slider</Option>
                        <Option value="News">News</Option>
                    </Select>
                </div>
                <div class="row">
                    <Select variant="filled" bind:value={element.data.position[1]} key={(value) => value.toString()} label="2">
                        <Option value="Articles">Articles</Option>
                        <Option value="Slider">Slider</Option>
                        <Option value="News">News</Option>
                    </Select>
                </div>
                <div class="row">
                    <Select variant="filled" bind:value={element.data.position[2]} key={(value) => value.toString()} label="3">
                        <Option value="Articles">Articles</Option>
                        <Option value="Slider">Slider</Option>
                        <Option value="News">News</Option>
                    </Select>
                </div>

                <br />
                <h4>Logo:</h4>
                <br />
                <div class="row">
                    <input
                        type="file"
                        id="myfile"
                        name="myfile"
                        on:change={(e) => {
                            //setImg(e, i);
                        }}
                    />
                </div>
                <br />
                <h4>Other:</h4>
                <br />
                <div class="row">
                    <Select variant="filled" bind:value={element.data.menuMode} key={(value) => value.toString()} label="Menu mode">
                        <Option value="1">1</Option>
                        <Option value="2">2</Option>
                    </Select>
                </div>
                <div class="row">
                    <Textfield class="Textfield" variant="filled" type="text" label="Company Name" bind:value={element.data.companyName} />
                </div>
                <div class="row">
                    <Textfield class="Textfield" variant="filled" type="text" label="Footer Text" bind:value={element.data.footerText} />
                </div>
            </div>
        </Paper>
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

    .bigTitle {
        font-size: 30px;
        font-weight: bold;
        margin-bottom: 30px;
    }

    table {
        width: 100%;
        table-layout: fixed;
    }
</style>

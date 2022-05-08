<script>
    import Select, { Option } from "@smui/select";
    import Textfield from "@smui/textfield";
    import Button, { Label } from "@smui/button";
    import Paper from "@smui/paper";
    import HelperText from '@smui/textfield/helper-text';
    import CharacterCounter from '@smui/textfield/character-counter';
    import DataTable, { Row, Cell } from "@smui/data-table";

    export let element;

    let value = 'articles';
    let id = 1;
    let articles = 3;
    let children = [
        { "title": "Article 1", "text": "lorem ipsum suma ipsum lorem" },
        { "title": "Article 2", "text": "lorem ipsum suma ipsum lorem" },
        { "title": "Article 3", "text": "lorem ipsum suma ipsum lorem" }
    ];
    let color = "#000000";
    let backgroundColor = "#FFFFFF";
    let textarea = "";

    let slider_value = 'slider';
    let slider_id = 0;
    let slider_color = "#000000";
    let slider_backgroundColor = "#FFFFFF";
    let slider_images = 3;

</script>


<div class="element">
    {#if element.name == "Articles"}
    
        <!-- <div>

            <label for="id">id:</label>
            <input type="number" id="id" name="id" min="0" max="10" value={element.id}>
        </div>

        <p>{element.id}</p> -->
        

        
        <Paper elevation={6}>
            <div class="options-selector">

                <table>
                    <tr>
                        <td>
                            <div class="row">
                                <Textfield
                                    class="Textfield"
                                    variant="filled"
                                    type="number"
                                    label="ID"
                                    input$max="15"
                                    input$min="0"
                                    bind:value={id}
                                />
                            </div>
                        </td>
                        <td>
                            <div class="row">
                                <!-- <Textfield
                                    class="Textfield"
                                    variant="filled"
                                    type="text"
                                    label="Color"
                                    bind:value={color}
                                /> -->
                                <label for="head">Color</label>
                                <input type="color" id="head" name="head" value="#e66465">
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div class="row">
                                <Select
                                    variant="filled"
                                    bind:value={value}
                                    key={(value) => value.toString()}
                                    label="Name"
                                >
                                    
                                    <Option value="articles">Articles</Option>
                                    <Option value="slider">Slider</Option>
                                    <Option value="news">News</Option>
                                    
                                </Select> 
                            </div>
                        </td>
                        <td>
                            <div class="row">
                                <Textfield
                                    class="Textfield"
                                    variant="filled"
                                    type="text"
                                    label="Background Color"
                                    bind:value={backgroundColor}
                                />
                            </div>
                        </td>
                    </tr>
                </table>

                
                
                <br><br>
                <div class="row">
                    <Textfield
                        class="Textfield"
                        variant="filled"
                        type="number"
                        label="Articles"
                        input$max="3"
                        input$min="0"
                        bind:value={articles}
                    />
                </div>       
                <br>
                <div class="doPapera">  
                    {#each children as article, i}
                        <div class="paper">
                            <Paper elevation={6}>
                                <div class="br"></div>
                                <!-- <p class="articleP">Article {i}:</p> -->
                                <h4>Article {i+1}:</h4>
                                <div class="br"></div>
                                <div class="row">
                                    <Textfield
                                        class="Textfield"
                                        variant="filled"
                                        type="text"
                                        label="Title"
                                        bind:value={article.title}
                                    />
                                </div>
                                <!-- <Textfield
                                    class="Textfield"
                                    variant="filled"
                                    type="text"
                                    label="Text"
                                    bind:value={article.text}
                                /> -->
                                <br>
                                <div>
                                    <!-- bez labela! -->
                                    <Textfield variant="outlined" textarea input$maxlength={100} bind:value={article.text}>
                                        <CharacterCounter slot="internalCounter">0 / 100</CharacterCounter>
                                        <HelperText slot="helper">Text</HelperText>
                                    </Textfield>
                                </div>
                            </Paper>
                        </div>
                    {/each}
                </div>
                
                <br>
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
        <br>
    {:else if element.name == "Slider"}
        <Paper elevation={6}>
            <div class="options-selector">

                <table>
                    <tr>
                        <td>
                            <div class="row">
                                <Textfield
                                    class="Textfield"
                                    variant="filled"
                                    type="number"
                                    label="ID"
                                    input$max="15"
                                    input$min="0"
                                    bind:value={slider_id}
                                />
                            </div>
                        </td>
                        <td>
                            <div class="row">
                                <Textfield
                                    class="Textfield"
                                    variant="filled"
                                    type="text"
                                    label="Color"
                                    bind:value={slider_color}
                                />
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div class="row">
                                <Select
                                    variant="filled"
                                    bind:value={slider_value}
                                    key={(slider_value) => slider_value.toString()}
                                    label="Name"
                                >
                                    
                                    <Option value="articles">Articles</Option>
                                    <Option value="slider">Slider</Option>
                                    <Option value="news">News</Option>
                                    
                                </Select> 
                            </div>
                        </td>
                        <td>
                            <div class="row">
                                <Textfield
                                    class="Textfield"
                                    variant="filled"
                                    type="text"
                                    label="Background Color"
                                    bind:value={slider_backgroundColor}
                                />
                            </div>
                        </td>
                    </tr>
                </table>

                
                
                <br><br>
                <div class="row">
                    <Textfield
                        class="Textfield"
                        variant="filled"
                        type="number"
                        label="Images"
                        input$max="3"
                        input$min="0"
                        bind:value={slider_images}
                    />
                </div>       

                <br>

                <div>
                    {#each Array(slider_images) as _, i}
                        <input type="file" id="myfile" name="myfile"><br>
                    {/each}
                </div>
                
                    
                
                

                <br>
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
        <br>
    {/if}
    
</div>

<style>
    label {
        /* Other styling... */
        text-align: right;
        clear: both;
        float:left;
        margin-right:15px;
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
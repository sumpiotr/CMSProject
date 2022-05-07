<script>
    import Select, { Option } from "@smui/select";
    import Textfield from "@smui/textfield";
    import Button, { Label } from "@smui/button";
    
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


</script>


<div class="element">
    {#if element.name == "Articles"}
    
        <!-- <div>

            <label for="id">id:</label>
            <input type="number" id="id" name="id" min="0" max="10" value={element.id}>
        </div>

        <p>{element.id}</p> -->




        <div class="options-selector">
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
            {#each children as article, i}
                <div class="br"></div>
                <p class="articleP">Article {i}:</p>
                <div class="br"></div>
                <Textfield
                    class="Textfield"
                    variant="filled"
                    type="text"
                    label="Title"
                    bind:value={article.title}
                />
                <Textfield
                    class="Textfield"
                    variant="filled"
                    type="text"
                    label="Text"
                    bind:value={article.text}
                />
            {/each}

            <br><br>
            <div class="row">
                <Textfield
                    class="Textfield"
                    variant="filled"
                    type="text"
                    label="Color"
                    bind:value={color}
                />
            </div>
            <div class="row">
                <Textfield
                    class="Textfield"
                    variant="filled"
                    type="text"
                    label="Background Color"
                    bind:value={backgroundColor}
                />
            </div>
            <br>
            <div class="row">
                <Button on:click={() => {}}>
                    <Label>SHOW</Label>
                </Button>
            </div>
        </div>

        <!-- <p>{element.name}</p> -->
        
        <!-- <select name="selectName" id="selectName">
            <option value="articles">Articles</option>
            <option value="slider">Slider</option>
            <option value="news">News</option>
        </select> -->


        <!-- <pre>data: {JSON.stringify(element.data, undefined, 4)}</pre>

        <p>SHOW</p> -->
        <br>
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
        border: 1px solid black;
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

    /* .options-selector :global(.mdc-select) {
        width: 60%;
        margin-right: 10px;
    }

    .options-selector :global(.mdc-select__anchor),
    .options-selector :global(.mdc-text-field) {
        height: 30px;
    }

    .options-selector :global(.mdc-floating-label) {
        transform: translateY(-25px) scale(0.75) !important;
    }

    .options-selector :global(.mdc-button) {
        border-radius: 100px;
    } */

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
</style>
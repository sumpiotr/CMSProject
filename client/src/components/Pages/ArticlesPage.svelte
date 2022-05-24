<script>
    import Articles from "../Articles.svelte";

    export let data;

    export let pages;

    let articleCategory = "";
    let sort;

    let articlesData = { children: [] };

    let articles = [];
    let reverse = true;

    for (let page of pages) {
        if (page.pageName == "Home") {
            for (let child of page.data) {
                if (child.name == "Articles") {
                    articles = child.data.children;
                    articlesData.children = [...articles];
                    articlesData.children.reverse();
                    break;
                }
            }
        }
    }

    function search() {
        let searchedArticles = [];
        if (articleCategory == "") {
            searchedArticles = [...articles];
            searchedArticles.reverse();
        } else {
            for (let article of articles) {
                if (article.category == articleCategory) {
                    searchedArticles.push(article);
                }
            }
        }

        if (sort == 1) {
            searchedArticles.sort((a, b) => {
                console.log(typeof a.title);
                return a.title.localeCompare(b.title);
            });
            reverse = false;
        } else {
            reverse = true;
        }

        articlesData.children = searchedArticles;
    }
</script>

<section>
    <div>
        <field>Category: </field><input type="text" bind:value={articleCategory} />
        <select bind:value={sort}>
            <option value="0">Date</option>
            <option value="1">Alphabetically</option>
        </select>
        <button type="Button" on:click={search}>Search</button>
    </div>
    <Articles data={articlesData} {articles} />
</section>

<script>
    import Comment from "../Comment.svelte";

    export let logged;
    export let article;
    export let index;

    let comments = [];

    let newCommentText = "";

    function loadComments() {
        fetch("./getComments", {
            method: "POST",
            body: JSON.stringify({ index: index }),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((d) => d.json())
            .then((d) => {
                comments = d.comments;
            });
    }

    function addComment() {
        fetch("./addComment", {
            method: "POST",
            body: JSON.stringify({ text: newCommentText, articleIndex: index }),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((d) => d.json())
            .then((d) => {
                newCommentText = "";
                loadComments();
            });
    }

    loadComments();
</script>

<div>
    <h4>{article.title}</h4>
    <br /><br />
    <div class="article">{article.text}</div>
    <br /><br /><br />
    


    {#if logged}
        <div>
            <section class="rounded-b-lg  mt-4 ">
                <form>
                    <input type="hidden" />
                    <textarea
                        class="w-full shadow-inner p-4 border-0 mb-4 rounded-lg focus:shadow-outline text-2xl"
                        placeholder="Enter comment..."
                        cols="6"
                        rows="6"
                        id="comment_content"
                        spellcheck="false"
                        bind:value={newCommentText}
                    />
                    <button type="button" on:click={addComment} class="font-bold py-2 px-4 w-full bg-purple-400 text-lg text-white shadow-md rounded-lg ">Comment </button>
                </form>

                <div id="task-comments" class="pt-4">
                    {#each comments as comment}
                        <Comment data={comment} />
                    {/each}
                </div>
            </section>
        </div>
    {:else}
        <div>Zaluguj się aby zostawić komentarz</div>
    {/if}
</div>

<style>
    .article {
        padding: 5px;
        font-size: 20px;
        text-align: left;
    }

    h4 {
        font-size: 21px;
        font-weight: bold;
    }
</style>

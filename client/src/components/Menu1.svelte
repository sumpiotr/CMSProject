<script>
    export let data;
    export let logged;
    export let admin;
    export let name;
</script>

<header class="text-gray-600 body-font">
    <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
        <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                class="w-10 h-10 text-white p-2 bg-indigo-500 rounded-full"
                viewBox="0 0 24 24"
            >
                <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
            </svg>
            <span class="ml-3 text-xl">{name}</span>
        </a>
        <nav class="md:ml-auto flex flex-wrap items-center text-base justify-center">
            {#each data as child}
                {#if (child.login == 1 && !logged) || (child.login == 2 && logged) || child.login == 0}
                    {#if (child.admin == 1 && !admin) || (child.admin == 2 && admin) || child.admin == 0}
                        <a class="mr-5 hover:text-gray-900" href="/{child.path}">{child.pageName}</a>
                    {/if}
                {/if}
            {/each}
        </nav>
    </div>
</header>

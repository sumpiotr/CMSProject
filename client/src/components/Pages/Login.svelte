<script>
    //register
    let registerError = "";
    let registerUsername;
    let registerPassword;

    function register() {
        fetch("./register", {
            method: "POST",
            body: JSON.stringify({ username: registerUsername, password: registerPassword }),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((d) => d.json())
            .then((d) => {
                registerError = d.error;
                if (!d.flag) {
                    return;
                }
                registerUsername = "";
                registerPassword = "";
            });
    }

    //login
    let loginErrorMessage = "";
    let loginUsername;
    let loginPassword;

    function login() {
        fetch("./login", {
            method: "POST",
            body: JSON.stringify({ username: loginUsername, password: loginPassword }),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((d) => d.json())
            .then((d) => {
                if (!d.flag) {
                    console.log(d.error);
                    loginErrorMessage = d.error;
                    return;
                }
                loginErrorMessage = "";
                window.location.replace("/");
            });
    }
</script>

<div class="main w-max m-auto mt-10">
    <div class="login">
        <h2 class="text-2xl mb-6">Login</h2>
        <div class="username flex border rounded text-gray-500 mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 mx-2 my-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor"
                ><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg
            >
            <input class="outline-none px-2 h-full py-2 text-lg" type="text" placeholder="username" bind:value={loginUsername} />
        </div>

        <div class="password flex border rounded text-gray-500 mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 mx-2 my-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor"
                ><path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z"
                /></svg
            >
            <input class="outline-none px-2 h-full py-2 text-lg" type="password" placeholder="password" bind:value={loginPassword} />
        </div>

        <div class="show_info text-sm mb-4 w-max text-red-400">{loginErrorMessage}</div>

        <div class="submit border rounded mb-4 bg-blue-600 text-white cursor-pointer">
            <div class="wrapper flex w-max mx-auto">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 my-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor"
                    ><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 11l3-3m0 0l3 3m-3-3v8m0-13a9 9 0 110 18 9 9 0 010-18z" /></svg
                >
                <input
                    class="outline-none px-2 h-full cursor-pointer py-2 text-lg bg-transparent"
                    type="button"
                    value="Login"
                    on:click={() => {
                        login();
                    }}
                />
            </div>
        </div>
    </div>
    <div class="register">
        <h2 class="text-2xl mb-6">Register</h2>

        <div class="username flex border rounded text-gray-500 mb-4">
            <input class="outline-none px-4 h-full py-2 text-lg" type="text" placeholder="username" bind:value={registerUsername} />
        </div>

        <div class="password flex border rounded text-gray-500 mb-4">
            <input class="outline-none px-4 h-full py-2 text-lg" type="password" placeholder="password" bind:value={registerPassword} />
        </div>

        <div class="show_info text-sm mb-4 w-max text-red-400">{registerError}</div>
        <div class="submit border rounded mb-4 bg-blue-600 text-white cursor-pointer">
            <div class="wrapper flex w-max mx-auto">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 my-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor"
                    ><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" /></svg
                >
                <input
                    class="outline-none px-2 h-full cursor-pointer py-2 text-lg bg-transparent"
                    type="button"
                    value="Register"
                    on:click={() => {
                        register();
                    }}
                />
            </div>
        </div>
    </div>
</div>

<style>
    body {
        background: white !important;
    }
</style>

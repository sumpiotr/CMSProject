import Menu1 from "./components/Menu1.svelte";
import Articles from "./components/Articles.svelte";
import Login from "./components/Pages/Login.svelte";

export class ComponentManager {
    static getComponentByName(name) {
        switch (name) {
            case "Menu1":
                return Menu1;
            case "Articles":
                return Articles;
            case "Login":
                return Login;
            default:
                return null;
        }
    }
}

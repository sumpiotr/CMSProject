import Menu1 from "./components/Menu1.svelte";
import Articles from "./components/Articles.svelte";
import Slider from "./components/Slider.svelte";
import News from "./components/News.svelte";
import Login from "./components/Pages/Login.svelte";
import Edit from "./components/Pages/Edit.svelte";
import LogOut from "./components/Pages/LogOut.svelte";
import UsersList from "./components/Pages/UsersList.svelte";
import AccountSettings from "./components/Pages/AccountSettings.svelte";
import Gallery from "./components/Pages/Gallery.svelte";
import ArticlesPage from "./components/Pages/ArticlesPage.svelte";

export class ComponentManager {
    static getComponentByName(name) {
        switch (name) {
            case "Menu1":
                return Menu1;
            case "Gallery":
                return Gallery;
            case "ArticlesPage":
                return ArticlesPage;
            case "Articles":
                return Articles;
            case "Login":
                return Login;
            case "Edit":
                return Edit;
            case "Slider":
                return Slider;
            case "News":
                return News;
            case "UsersList":
                return UsersList;
            case "AccountSettings":
                return AccountSettings;
            case "Logout":
                return LogOut;
            default:
                return null;
        }
    }
}

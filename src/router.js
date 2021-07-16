import Vue from "vue"
import Router from "vue-router"
import AppHeader from "./layout/AppHeader"
import AppFooter from "./layout/AppFooter"
import Profile from "./views/Profile.vue"
import Home from "./views/Home.vue"
import BookingForm from "./views/BookingForm.vue"
import BookingConfirm from "./views/BookingConfirm.vue"

Vue.use(Router)

export default new Router({
  linkExactActiveClass: "active",
  routes: [
    {
      path: "/",
      name: "home",
      components: {
        header: AppHeader,
        default: BookingForm,
        footer: AppFooter
      }
    },
    {
      path: "/book",
      name: "book",
      components: {
        header: AppHeader,
        default: BookingForm,
        footer: AppFooter
      }
    },
    {
      path: "/confirmation/:booking_id",
      name: "confirmation",
      components: {
        header: AppHeader,
        default: BookingConfirm,
        footer: AppFooter
      }
    },
  ],
  scrollBehavior: to => {
    if (to.hash) {
      return { selector: to.hash }
    } else {
      return { x: 0, y: 0 }
    }
  }
})
